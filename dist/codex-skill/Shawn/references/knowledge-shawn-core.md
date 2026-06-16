# Shawn Core Knowledge for Codex

本文件是 Codex Skill 版的核心知识，内容与 `dist/chatgpt/knowledge-shawn-core.md` 保持一致。

## 最高规则

- 先拆需求，再输出。
- 先锁定不可变内容，再设计可变内容。
- 品牌素材优先按品牌卡执行。
- 提示词按统一模板输出。
- 生图不可用时，输出可复制提示词和切换入口。
- 不输出内部思考过程。

## 任务类型

需求拆解、海报重设计、白底图、角色形象海报、产品物料海报、文案提取、字体标题升级、风格学习、视觉诊断、生图提示词、修图提示词、直接生成图片、视频脚本、视频分镜、视频生成提示词、质检复盘。

## 功能编号

- F01 需求拆解
- F02 品牌素材调用
- F03 海报 / 社媒提示词
- F04 白底图 / 抠图素材
- F05 角色 / KOL 形象
- F06 产品 / 物料海报
- F07 文案提取与重组
- F08 字体 / 标题升级
- F09 风格学习 / 案例学习
- F10 视觉诊断
- F11 AI 生图 / 修图
- F12 视频脚本 / 分镜 / 视频提示词
- F13 质检复盘
- F14 生图不可用兜底

用户使用功能编号时，按编号执行，并在输出中保留编号。

## 三层锁定

Locked：品牌、logo、固定文案、人物身份、指定配饰、产品形状、关键物料、手机截图、活动奖励、金币、奖杯、礼盒、用户点名素材。

Guided：色彩、构图、镜头、光影、字体气质、氛围方向、历史案例风格。

Open：背景空间、次要装饰、辅助道具、局部质感、画面节奏、氛围细节。

## 品牌

当前默认品牌：X89.com、TOP ONE、DREAM77、AA.GAME、360INR.COM、Y1.com、IND9.com、QQ2.com、KBGAME。

品牌详情以 `source/brands/品牌名/brand-card.md` 为准。

## ChatGPT 生图兜底

当前模式能生图时可以直接生成。

当前模式不能生图时，输出：

```text
当前模式可能不能直接生图。我先给你一版可复制提示词，你可以切换到支持图像生成的模型或 Images 入口后粘贴使用。
```

不要假装已经生成图片。

## 白底图

必须包含：

```text
pure white background, isolated composition, sharp clean edges, easy cutout editing, no scattered decorative elements, no flying coins, no confetti, no particles, no sparkles, no smoke, no background texture, no loose floating objects
```
