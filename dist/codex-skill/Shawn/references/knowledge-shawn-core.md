# Shawn Core Knowledge for Codex

本文件是 Codex Skill 版核心知识，与 ChatGPT Knowledge 保持同一套功能编号。

## 最高规则

- 先拆需求，再输出。
- 先锁定不可变内容，再设计可变内容。
- 品牌素材优先按品牌卡执行。
- 提示词按统一模板输出。
- 生图不可用时，输出可复制提示词和切换入口。
- 用户不写编号时自动判断，并在输出里反标编号。

## 功能编号

图片：

- P01 社媒图：P01-1 游戏推荐、P01-2 活动开奖、P01-3 品牌公告、P01-4 收集引导、P01-5 特定活动 / 节日
- P02 白底图：P02-1 人物、P02-2 Banner、P02-3 人物 + 文案、P02-4 道具 / 物料
- P03 私域图：P03-1 公告、P03-2 兑换码、P03-3 贴纸风海报
- P04 人物 / KOL 图：P04-1 新 KOL、P04-2 已有 KOL
- P05 产品 / 物料图
- P06 文案与标题
- P07 视觉诊断与质检

视频：

- V01 视频脚本
- V02 分镜图方案
- V03 视频生成提示词
- V04 视频整包

## 自动识别

- 写 `P01-1`：精确执行。
- 写 `P01`：判断子类。
- 不写编号：根据文案识别。
- 写功能名但不写编号：也要识别。

## V02 分镜图规则

- 分镜图画布固定 16:9。
- 分镜图里放目标视频比例的单张画面。
- 一张分镜图至少 6 张。
- 剧情丰富用 8 张。
- 超过 8 张拆成多张分镜图。
- 图里不写文字标注，只保留数字编号。

## V03 视频提示词规则

中英文写在一起，方便整段复制。包含画面、动作、镜头、节奏、风格、负面要求。

## 白底图

必须包含：

```text
pure white background, isolated composition, sharp clean edges, easy cutout editing, no scattered decorative elements, no flying coins, no confetti, no particles, no sparkles, no smoke, no background texture, no loose floating objects
```
