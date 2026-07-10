from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parent.parent


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo = Path(self.temp_dir.name) / "repo"
        shutil.copytree(
            SOURCE_ROOT,
            self.repo,
            ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"),
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def run_command(
        self, *args: str, env: dict[str, str] | None = None
    ) -> subprocess.CompletedProcess[str]:
        process_env = os.environ.copy()
        if env:
            process_env.update(env)
        return subprocess.run(
            args,
            cwd=self.repo,
            env=process_env,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

    def git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return self.run_command("git", *args)

    def test_complete_template_validation_passes(self) -> None:
        result = self.run_command("./scripts/validate.sh")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_project_profile_rejects_template_placeholders(self) -> None:
        overview = self.repo / ".agents" / "project" / "overview.md"
        overview.write_text(
            overview.read_text(encoding="utf-8") + "\n<TEST_PLACEHOLDER>\n",
            encoding="utf-8",
        )
        result = self.run_command("./scripts/validate-project-profile.sh")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("project profile still contains placeholders", result.stdout)

    def test_public_safety_scans_ignored_files(self) -> None:
        token = "github_" + "pat_" + ("A" * 24)
        (self.repo / ".env").write_text(f"TOKEN={token}\n", encoding="utf-8")
        result = self.run_command("./scripts/check-public-safety.sh")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("./.env", result.stdout)

    def test_public_safety_honors_private_deny_pattern(self) -> None:
        marker = "Private" + "Customer" + "Marker"
        (self.repo / "probe.txt").write_text(marker + "\n", encoding="utf-8")
        result = self.run_command(
            "./scripts/check-public-safety.sh",
            env={"EXTRA_DENY_PATTERN": marker},
        )
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("caller-supplied private identifier", result.stdout)

    def test_link_validator_rejects_missing_reference_target(self) -> None:
        (self.repo / "probe.md").write_text(
            "[Missing image][fixture]\n\n[fixture]: absent.png\n",
            encoding="utf-8",
        )
        result = self.run_command("python3", "scripts/validate-links.py")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("missing target: absent.png", result.stdout)

    def test_link_validator_rejects_repository_escape(self) -> None:
        (self.repo / "probe.md").write_text("[Outside](../outside.md)\n", encoding="utf-8")
        result = self.run_command("python3", "scripts/validate-links.py")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("link escapes repository", result.stdout)

    def test_agent_entrypoint_validator_rejects_broken_skill_reference(self) -> None:
        skill = self.repo / ".agents" / "skills" / "api-contract" / "SKILL.md"
        skill.write_text(
            skill.read_text(encoding="utf-8").replace(
                "../../references/api-contract.md", "../../references/missing.md"
            ),
            encoding="utf-8",
        )
        result = self.run_command("python3", "scripts/validate-agent-entrypoints.py")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("missing referenced file", result.stdout)

    def test_agent_entrypoint_validator_rejects_missing_claude_import(self) -> None:
        claude = self.repo / "CLAUDE.md"
        claude.write_text(
            claude.read_text(encoding="utf-8").replace("@AGENTS.md", "# Missing import", 1),
            encoding="utf-8",
        )
        result = self.run_command("python3", "scripts/validate-agent-entrypoints.py")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("CLAUDE.md must begin with @AGENTS.md", result.stdout)

    def test_agent_entrypoint_validator_rejects_unpaired_skill(self) -> None:
        shutil.rmtree(self.repo / ".claude" / "skills" / "project-bootstrap")
        result = self.run_command("python3", "scripts/validate-agent-entrypoints.py")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("skills missing from Claude Code: project-bootstrap", result.stdout)

    def test_structure_rejects_a_tracked_local_file(self) -> None:
        local_note = self.repo / ".agents" / "local" / "private-note.md"
        local_note.write_text("machine-local note\n", encoding="utf-8")
        self.assertEqual(self.git("init", "-b", "main").returncode, 0)
        self.assertEqual(self.git("add", "-f", str(local_note.relative_to(self.repo))).returncode, 0)
        result = self.run_command("./scripts/validate-structure.sh")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("local-only files must not be tracked", result.stdout)

    def test_publish_readiness_reports_maintainer_and_git_blockers(self) -> None:
        (self.repo / ".github" / "CODEOWNERS").unlink()
        for filename in ("SECURITY.md", "CODE_OF_CONDUCT.md"):
            path = self.repo / filename
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n<!-- PUBLICATION-BLOCKER: fixture -->\n",
                encoding="utf-8",
            )
        self.assertEqual(self.git("init", "-b", "main").returncode, 0)
        result = self.run_command("python3", "scripts/validate-publish-readiness.py")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(".github/CODEOWNERS is missing", result.stdout)
        self.assertIn("publication blocker", result.stdout)
        self.assertIn("no initial commit", result.stdout)

    def test_publish_readiness_passes_for_complete_local_fixture(self) -> None:
        (self.repo / ".github" / "CODEOWNERS").write_text(
            "* @fixture-maintainers\n",
            encoding="utf-8",
        )
        for filename in ("SECURITY.md", "CODE_OF_CONDUCT.md"):
            path = self.repo / filename
            path.write_text(
                path.read_text(encoding="utf-8").replace("PUBLICATION-BLOCKER", "VERIFIED"),
                encoding="utf-8",
            )
        conduct = self.repo / "CODE_OF_CONDUCT.md"
        conduct.write_text(
            conduct.read_text(encoding="utf-8").replace(
                "Report conduct concerns privately through the maintainer-designated channel.",
                "Report conduct concerns through [the private conduct address](mailto:conduct@invalid.example).",
            ),
            encoding="utf-8",
        )

        commands = (
            ("init", "-b", "main"),
            ("config", "user.name", "Fixture Maintainer"),
            ("config", "user.email", "fixture@invalid.example"),
            ("add", "--all"),
            ("commit", "-m", "Initial fixture"),
            ("remote", "add", "origin", "https://github.com/fixture/repo.git"),
        )
        for command in commands:
            result = self.git(*command)
            self.assertEqual(result.returncode, 0, result.stdout)

        result = self.run_command("python3", "scripts/validate-publish-readiness.py")
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("local publication-readiness validation passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
