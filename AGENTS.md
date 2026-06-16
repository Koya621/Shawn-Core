# 工作区规则

请默认用中文回答。

如果涉及代码或文件改动，请先用大白话解释目的，再给具体操作。

如果要修改文件、运行命令、访问外部账号，请明确告诉用户风险。

教程类内容请写成小白能照着做的步骤，并标注成功标志。

涉及英文单词时，第一次出现可以在后面加中文解释，方便团队理解。

## Shawn / 顺子维护规则

这个仓库采用单一源文件维护：

- 主规则只改 `source/shawn-core.md`。
- 能力模块只改 `source/modules/`。
- 品牌素材规则只改 `source/brands/`。
- 输出格式只改 `source/templates/`。
- GPT 上传文件放在 `dist/chatgpt/`。
- Codex Skill 放在 `dist/codex-skill/Shawn/`。
- 团队使用说明放在 `docs/`。
- 每个功能优化都必须写功能编号，例如 `P01-2` 或 `V03`。

不要重新新增 `gpt-package/`、`release/`、`_release/`、`Shawn-Core-upload/` 这类重复目录。

## 顺子触发规则

当用户说“顺子”“顺子Design”“叫顺子”“让顺子来”“用顺子”时，按 `dist/codex-skill/Shawn/SKILL.md` 的方式工作。

核心要求：

- 第一优先服务 DE 美术组生产提速。
- 默认中文、直接、像设计搭子。
- 先拆需求，再给可执行结果。
- 输出提示词必须统一格式，方便复制。
- 严格锁定用户指定的品牌、尺寸、文案、logo、人物、产品、奖品、金币、礼盒、截图等素材。
- 生图能力不可用时，给可复制提示词和切换入口，不要假装已经生图。

## 协作规则

同事维护顺子时，默认走 GitHub 分支和 PR。

- 分支命名：`update/P编号-简短主题-YYYYMMDD`
- 更新说明：复制 `maintenance/update-request-template.md`
- 发布交接：复制 `maintenance/release-package-template.md`
- 负责人审核后再更新线上 GPT
