# 公开发布检查清单

[English checklist](publishing.md)

本清单用于把本地版本发布为 GitHub 公共模板。真实维护者信息配置完成前，不要把仓库可见性改为 public。

## 1. 确认公共边界

- 审查全部 Git 跟踪文件，而不只是最后一次差异。
- 执行 `./scripts/validate.sh` 和 `./scripts/test.sh`。
- 使用维护者认可的专业秘密扫描工具再扫描一次。
- 使用私下保存的正则执行 `EXTRA_DENY_PATTERN='<PRIVATE_IDENTIFIERS>' ./scripts/check-public-safety.sh`，覆盖原项目名称、域名、仓库标识和基础设施词汇。
- 确认示例完全虚构，并且没有复制私有项目的 Git 历史。

内置检查只是门禁，不能证明仓库绝对不含秘密或个人信息。

## 2. 填写维护者信息

- 将 `.github/CODEOWNERS.example` 复制为 `.github/CODEOWNERS`，用真实 GitHub 用户或团队替换示例责任人。
- 在 `CODE_OF_CONDUCT.md` 中写明受监控的私密投诉渠道，并删除对应 `PUBLICATION-BLOCKER` 注释。
- 启用 GitHub Private Vulnerability Reporting；如果不启用，就在 `SECURITY.md` 中改成受监控的私密安全联络方式。确认完成后删除对应阻塞注释。
- 复核 `SECURITY.md` 的支持版本承诺和 `CHANGELOG.md` 的发布信息。

不要为了通过检查而编造责任人或无人监控的邮箱。

## 3. 建立并保护远程仓库

- 先建立 private GitHub 仓库并配置 `origin`。
- 使用 `main` 作为默认分支；如需更换，必须同步更新工作流和文档。
- 启用 Template repository、secret scanning、push protection 和 private vulnerability reporting。
- 保护默认分支，要求验证工作流成功，并要求可信指令路径由维护者审查。
- GitHub Actions 默认保持只读权限，新增权限必须逐项说明原因。
- 关闭不使用的仓库功能，让贡献者只有清晰的支持入口。

## 4. 创建首个版本

1. 检查 `git status` 和完整跟踪文件列表。
2. 确认 Git 提交者姓名和邮箱适合公开展示。
3. 在责任人和私密报告渠道配置完成后创建初始提交。
4. 推送 private 仓库，确认远程 CI 成功。
5. 执行 `python3 scripts/validate-publish-readiness.py`；只有本地证据完整时它才会通过。
6. 使用临时仓库测试 “Use this template”。
7. 在临时仓库中填写 `.agents/project/`，验证 Codex 与 Claude Code 两个入口。
8. 完成 GitHub 设置复核后再改为 public。
9. 创建 `v0.1.0` 标签，并根据 `CHANGELOG.md` 发布 Release Notes。

## 5. 保存验证记录

记录以下内容：

- 通过的验证命令。
- 已执行的秘密和隐私检查。
- 模板生成测试结果。
- Codex 与 Claude Code 加载测试结果。
- 已知限制和明确非目标。
- 批准公开发布的维护者。

任何必需项仍是推测时，都不能宣布发布完成。
