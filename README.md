# Shawn Core for DE Art Team

Shawn Core 是 DE 美术组的设计助手知识仓库，用来维护「顺子 Shawn」在 ChatGPT 网页端和 Codex 端的同一套工作规则。

现在的目标不是做一个只会按个人习惯写提示词的助手，而是做一个能服务团队生产的设计 Skills：

- 拆需求：把品牌、平台、尺寸、类型、交付物和缺失信息先整理清楚。
- 调素材：根据品牌名匹配品牌卡、素材规则、风格关键词和禁用项。
- 写提示词：按统一格式输出可复制的海报、修图、生图、视频提示词。
- 做脚本：输出短视频脚本、KOL 视频分镜、字幕节奏和视频生成提示词。
- 做质检：按 DE 美术组 SOP 检查主体、层级、文案、尺寸、品牌一致性。
- 做沉淀：把好案例、坏案例、品牌变化和提示词优化沉淀回仓库。

## 目录结构

```text
source/
  shawn-core.md              # 唯一主规则源
  modules/                   # 六个能力模块
  brands/                    # 品牌素材卡与上传格式
  templates/                 # 输出模板
dist/
  chatgpt/                   # 上传到网页 GPT 的文件
  codex-skill/Shawn/         # 安装到 Codex 的 Skill
maintenance/                 # 维护流程、测试清单、发布说明
assets/                      # 角色与展示素材
```

## 维护原则

1. 日常只改 `source/`。
2. 更新网页 GPT 时使用 `dist/chatgpt/`。
3. 更新 Codex Skill 时使用 `dist/codex-skill/Shawn/`。
4. 新增品牌先填 `source/brands/_template/brand-card.md`。
5. 新增提示词必须进入 `source/templates/`，不要散落在聊天记录里。

## ChatGPT 网页端部署

1. 创建或编辑自定义 GPT。
2. Instructions 粘贴 `dist/chatgpt/gpt-instructions.md`。
3. Knowledge 上传 `dist/chatgpt/knowledge-shawn-core.md` 和需要的品牌卡。
4. Capabilities 里开启 Image generation。
5. 用 `maintenance/test-checklist.md` 做一次验收。

成功标志：输入「顺子，帮我给 X89 做一张 TG 活动海报提示词」，输出会按统一模板给出设计判断、Prompt、Negative、后期排版建议和确认点。

## Codex 端部署

把 `dist/codex-skill/Shawn/` 放到 Codex skills 目录。

成功标志：在 Codex 里输入「顺子」开头的需求，第一句固定回复 `兄弟，在呢`，并按 DE 美术组规则工作。

## 重要限制

网页端生图能力受 ChatGPT 当前模型和 GPT 配置影响。规则里已经加入兜底：如果当前模式不能生图，顺子必须输出可复制提示词，并提示切换到支持图像生成的入口。

详细排查见 `maintenance/chatgpt-image-generation-notes.md`。
