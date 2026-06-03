# Shawn Core 更新记录

## 2026-06-03

- 将“私域社群风格”“社区贴纸海报”“轻博彩奖品感”的固定记忆写入 `codex-skill/Shawn/`。
- 同步更新 `gpt-package/knowledge-shawn-profile.md`，让 ChatGPT 网页端也能读取同一套风格记忆。
- 同步更新 `Shawn-Core-upload/` 与 `release/chatgpt-online-full-v0.3/` 中的对应文件，保持 GitHub 仓库与线上上传包一致。

## 2026-05-12

- 修复网页 GPT 稳定性规则冲突：统一“先提示词后生图，用户明确直生图可例外”。
- 调整抗中断策略：从“280字硬限制”改为“400-900字短而完整 + 分轮输出”，减少卡住与截断风险。
- 新增 `release/chatgpt-online-full-v0.3/` 全量上传包和 `UPLOAD-CHECKLIST.md`，支持一键替换。
- 同步更新 `Shawn-Core-upload/gpt-package/`，确保上传副本与主规则一致。

## 2026-05-10

- 建立 Shawn Core 仓库结构。
- 收录 Shawn / 顺子角色卡资产。
- 收录 Codex Skill 版。
- 新增 ChatGPT 网页端 GPT 迁移包。
- 明确 Shawn 没有固定海报风格偏好，每次按用户当次需求判断。


## 2026-05-11

- 升级 Shawn / 顺子 Skill 到 v0.2。
- 新增任务路由、三层资产锁定、视觉语义翻译、角色动态 A/B 分类、学习闭环。
- 将规则模块化拆分到 references 独立文件，便于维护。
- 同步升级 GPT 网页端 `gpt-package/gpt-instructions.md`。
