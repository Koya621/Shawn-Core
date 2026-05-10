# Shawn Core

Shawn Core 是 Shawn / 顺子的统一知识仓库，用来同步和维护两个版本：

- Codex Skill 版：给本地 Codex 使用。
- ChatGPT GPT 版：给网页端自定义 GPT 使用。

## 目录说明

- `codex-skill/Shawn/`：Codex 本地 Skill 文件。
- `gpt-package/`：上传到 ChatGPT 自定义 GPT 的说明和知识文件。
- `design-library/`：长期积累的设计原则、风格库、提示词模式和审美自检清单。
- `assets/`：角色卡、三视图、参考资产。
- `CHANGELOG.md`：每次升级记录。

## 推荐工作流

1. 在公司或家里更新 Shawn 时，先更新这个仓库。
2. 每次更新后提交一次 Git 版本。
3. 另一台电脑拉取最新版。
4. 如果需要网页端 GPT，也同步更新 `gpt-package/` 里的文件并上传到 GPT Builder。

## Codex 使用方式

把 `codex-skill/Shawn/` 同步到本机 Codex skills 目录，或让 Codex 读取这个仓库并更新本机 Skill。

当前本机 Skill 路径：

```text
/Users/kklm/.codex/skills/shun-designer
```

## ChatGPT 网页端使用方式

在 ChatGPT 网页端创建自定义 GPT，名称设为 `Shawn`，然后：

1. 把 `gpt-package/gpt-instructions.md` 粘贴到 GPT Instructions。
2. 把 `gpt-package/knowledge-shawn-profile.md`、`design-library/` 里的核心文件和 `assets/shunzi-character-card.png` 上传到 Knowledge。
3. 开启图片生成能力。

