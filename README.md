# Shawn Core

Shawn Core 是 `Shawn / 顺子` 的统一知识仓库。

它的目标很直接：让顺子在 `Codex` 和 `ChatGPT` 两端都保持同一套角色设定、设计判断逻辑和输出标准。

## 顺子是谁

顺子（Shawn）是一个 26 岁的海报设计搭子，核心标签是：

- 干净
- 聪明
- 松弛
- 有审美

固定识别点：黑色微卷短发、黑框眼镜、白衬衫、粉灰细条纹领带、蓝色牛仔裤、白鞋。

常用 slogan：

> 把画面排明白，把审美落到位。

## 角色形象展示

### 1) 科技感主视觉海报

![顺子科技海报](assets/showcase/shunzi-poster-tech.png)

### 2) 角色标准头像

![顺子标准头像](assets/showcase/shawn-portrait.png)

### 3) 工作室场景海报

![顺子工作室海报](assets/showcase/shawn-studio-poster.png)

## 仓库目录说明

- `codex-skill/Shawn/`：Codex 本地 Skill 文件（主规则 + references 模块）
- `gpt-package/`：网页端 GPT 上传包（Instructions + Knowledge）
- `design-library/`：设计原则、风格库、提示词模式、审美检查清单
- `assets/`：角色卡与视觉资产
- `CHANGELOG.md`：版本更新记录

## 推荐工作流（简版）

1. 先在这个仓库改规则或知识文件。
2. 提交并推送到 GitHub。
3. 在另一台设备拉取最新版本。
4. 需要更新网页 GPT 时，同步 `gpt-package/` 与知识文件。

## Codex 使用方式

把 `codex-skill/Shawn/` 同步到本机技能目录：

```text
/Users/kklm/.codex/skills/shun-designer
```

## ChatGPT 网页端使用方式

在 ChatGPT 创建自定义 GPT（建议命名 `Shawn`）：

1. 把 `gpt-package/gpt-instructions.md` 粘贴到 Instructions。
2. 上传 `gpt-package/knowledge-shawn-profile.md`、`design-library/` 核心文件、`assets/shunzi-character-card.png`。
3. 开启图片生成能力。

## 当前版本亮点

- 已升级 `v0.2` 设计工作流：先判断、再执行
- 新增任务路由与三层锁定（Locked / Guided / Open）
- 新增角色动态 A/B 分类与学习复盘闭环
