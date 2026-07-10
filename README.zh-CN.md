# Agent Project Kit

[English README](README.md)

Agent Project Kit 是一套可以放进软件项目仓库的协作与交付规范，让人类、Codex 和 Claude Code 在开始工作前理解同一套项目边界、风险门禁和验证标准。

当前版本：**0.1.0**

## 设计目标

- 新项目可以从模板快速建立协作规范。
- 已有项目可以按模块接入，而不覆盖现有规则。
- 人类通过 README 理解如何使用和维护。
- Codex 通过 `AGENTS.md` 和 `.agents/skills/` 自动发现规则。
- Claude Code 通过 `CLAUDE.md` 和 `.claude/skills/` 加载同一套规则。
- 架构、API、数据模型、跨组件和破坏性变更必须先比较方案、确认决策和完成标准。
- 数据库、部署和生产回滚必须先确认环境、备份、验证与回滚。
- 交付必须区分已验证、未验证、兼容性妥协和故意未做事项。

## 明确非目标

- 本仓库不保存任何真实项目的密钥、生产地址、数据库备份或个人数据。
- 本仓库不替代密码管理器、基础设施配置系统或发布平台。
- 本仓库不假设某一种编程语言、框架、分支模型或云厂商。
- 0.1.x 暂不提供自动升级器，也不自动合并已有项目的规则文件。

## 新项目使用方式

1. 在 GitHub 上将本仓库设置为 Template repository。
2. 使用 “Use this template” 创建新仓库。
3. 在 Codex 中调用 `$project-bootstrap`，或在 Claude Code 中调用 `/project-bootstrap`，根据仓库证据填写 `.agents/project/` 下的项目资料、仓库清单、命令、环境、API 约定和责任人。
4. 删除不适用的工作流，但不要保留空洞或错误的占位内容。
5. 根据项目真实情况调整根 `AGENTS.md`，保持其简短。
6. 将项目自己的产品说明写入 README，并保留本规范的入口链接。
7. 先执行 `./scripts/validate-project-profile.sh`，确认项目资料没有遗留占位符，再执行 `./scripts/validate.sh`。
8. 让 Codex 列出已加载的规则并调用 `$api-contract`；在 Claude Code 中用 `/memory` 检查规则并调用 `/api-contract`，确认双端入口有效。

完整步骤见 [新项目入门](docs/getting-started.md)。

## 已有项目接入方式

不要直接覆盖已有的 `AGENTS.md`、`CLAUDE.md`、`.agents/` 或 `.claude/`。

先在 Codex 中调用 `$project-bootstrap`，或在 Claude Code 中调用 `/project-bootstrap`，让 Agent 盘点现有规则和仓库证据。

推荐顺序：

1. 备份并盘点当前规则。
2. 复制通用工作流、运行手册和模板。
3. 人工合并根路由文件。
4. 将真实项目事实填入 `.agents/project/`。
5. 解决重复或冲突规则，明确哪一份是权威来源。
6. 验证两个 agent 的加载结果。

详见 [已有项目接入](docs/existing-project.md)。

## 三层信息模型

| 层级 | 内容 | 是否共享 |
| --- | --- | --- |
| 通用核心 | 工作流、运行手册、模板、安全门禁 | 是 |
| 项目资料 | 组件、命令、环境、API 约定、责任人 | 随项目共享 |
| 本机私有 | 临时机器说明和非共享配置引用 | 否 |

真实密钥不应存放在任何一层的 Markdown 文档中。`.agents/local/` 被忽略，但仍不应当作长期密钥仓库。

## 双 Agent、单一权威来源

```text
Human          -> README.md
Codex          -> AGENTS.md -> .agents/index.md -> .agents/*
Claude Code    -> CLAUDE.md imports AGENTS.md
Claude skills  -> .claude/skills/* -> .agents/references/*
Codex skills   -> .agents/skills/* -> .agents/references/*
```

详细规则只维护在 `.agents/`，工具专属入口只负责加载和少量工具差异，避免同一规则在多处漂移。

## 内置 Skills

| Skill | Codex | Claude Code | 用途 |
| --- | --- | --- | --- |
| 项目初始化 | `$project-bootstrap` | `/project-bootstrap` | 配置新项目、合并已有规则并验证项目资料 |
| API 契约 | `$api-contract` | `/api-contract` | 检查生产者、消费者、兼容迁移和验证范围 |

## 本地验证

```sh
./scripts/validate.sh
./scripts/test.sh
```

本地验证依赖 Bash、Python 3 和 ripgrep（`rg`）。

公共模板自身故意保留项目资料占位符；从模板生成的实际项目必须让 `./scripts/validate-project-profile.sh` 通过，才能把 `.agents/project/` 当作权威事实。

它会检查：

- 必需文件和双端入口
- skill 元数据、共享引用路径和 Codex/Claude 入口一致性
- Markdown 相对链接
- 个人绝对路径、手机号形态、IP、私钥和常见 token 前缀
- 调用者通过 `EXTRA_DENY_PATTERN` 提供的额外禁用标识
- `.agents/local/` 是否意外出现其他文件

这些检查不能替代专业秘密扫描和人工 PII 审查。公开仓库后还应启用托管平台的 secret scanning 与 push protection。

正式改为公开仓库前，必须完成 [公开发布检查清单](docs/publishing.md)。其中真实代码责任人、私密漏洞报告渠道和行为准则联络方式必须由维护者填写，本模板不会编造这些信息。

完成维护者配置、初始提交和 private `origin` 后，再执行：

```sh
python3 scripts/validate-publish-readiness.py
```

这个本地门禁不能代替 GitHub 设置和远程 CI 的人工复核。

## 开源维护

- 变更记录见 [CHANGELOG.md](CHANGELOG.md)。
- 升级方式见 [docs/upgrading.md](docs/upgrading.md)。
- 分发方式见 [docs/distribution.md](docs/distribution.md)。
- 中文公开发布门禁见 [docs/publishing.zh-CN.md](docs/publishing.zh-CN.md)。
- 贡献规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。
- 安全报告见 [SECURITY.md](SECURITY.md)。
- 许可证见 [LICENSE](LICENSE)。
