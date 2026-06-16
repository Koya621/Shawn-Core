# Changelog

## v1.2.0 - P/V Function Tree And Sync Pack

- 将顺子功能编号升级为图片 `P`、视频 `V` 两大类。
- 新增短子编号格式，例如 `P01-1`，避免长编号难输入。
- 新增 `docs/function-tree.md`，用 Mermaid 展示功能树，并标注 `NEW`、`UPDATED`、`PLANNED`。
- 新增 `docs/index.md`、`docs/gpt-public-description.md`、`docs/gpt-answer-rules.md`。
- 同步更新 GPT Knowledge、GPT Instructions、Codex Skill 和维护模板。
- 新增 `sync/` 源文件、`scripts/sync-shawn-docs.ps1` 和 `dist/sync/` 同步输出，用于 TG 帮助、公盘说明和提示词网站说明。
- 增加 TG bot 安全约束：不提交真实 `config.json`、token 或控制密码；本版不改 TG bot 归档核心逻辑。

## v1.1.0 - Function Guide And Collaboration Workflow

- 新增顺子功能编号体系：F01-F14。
- 新增团队使用说明：`docs/shawn-user-guide.md`。
- 新增功能编号总表：`docs/function-index.md`。
- 新增同事 Codex + GitHub Desktop 协作流程：`docs/coworker-codex-workflow.md`。
- 新增 PR 模板、更新说明模板、GPT 发布交接单模板。
- 更新 README，加入顺子形象、快速开始、功能总览和维护入口。
- 同步 GPT Knowledge 和 Codex Skill，让顺子能识别功能编号。

## v1.0.0 - DE Art Team Skills Upgrade

- 清理旧重复结构：移除 `Shawn-Core-upload/`、`release/`、`_release/`、`gpt-package/`、`design-library/`、旧 `codex-skill/` 和 `.DS_Store`。
- 新增单一源文件结构：`source/shawn-core.md`、`source/modules/`、`source/templates/`、`source/brands/`。
- 新增 ChatGPT 网页端上传包：`dist/chatgpt/`。
- 新增 Codex Skill 分发包：`dist/codex-skill/Shawn/`。
- 新增 DE 美术组 6 个能力模块：需求拆解、品牌资产、海报社媒、AI 生图修图、视频脚本提示词、质检复盘。
- 新增品牌素材上传格式和 9 个品牌占位卡。
- 新增维护说明、贡献规则和测试清单，方便多人共同维护。
- 加入 ChatGPT 生图兜底规则：当前模式不能调用图像生成时，输出可复制提示词并提示切换到支持生图的入口。

## v0.3

- 旧版 Shawn 个人提示词助手。
- 已有海报提示词、白底图、私域社群风格、角色动态 A/B 分类等能力。
