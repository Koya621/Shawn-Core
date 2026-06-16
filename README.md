# Shawn Core / 顺子设计助手

> DE 美术组专用设计助手知识仓库。<br>
> 维护线上 GPT 顺子、Codex 顺子 Skill、品牌素材规则、TG / 公盘 / 提示词网站同步说明。

![顺子主视觉](assets/showcase/shunzi-poster-tech.png)

## 最近更新

`UPDATED` 功能编号已升级为图片 / 视频大类：

- `P` = 图片功能
- `V` = 视频功能
- 子功能用短编号，例如 `P01-1`，不用写 `P01.01`
- 不写编号也可以，顺子会根据文案自动判断
- 新增 TG / 公盘 / 提示词网站同步包：`dist/sync/`

## 快速开始

```text
顺子，P01，帮我给 X89 做一张 TG 游戏推荐海报，1:1。
```

```text
顺子，做一张私域兑换码图。
```

```text
顺子，V01，写一个 15 秒 KOL 视频脚本。
```

```text
顺子，V03，给我中英文视频提示词，写在一起方便复制。
```

## 功能入口

| 入口 | 给谁看 | 用途 |
| --- | --- | --- |
| [文档首页](docs/index.md) | 所有人 | 快速找到该看的说明 |
| [顺子使用说明](docs/shawn-user-guide.md) | 新人 / 老同事 | 快速上手怎么问 |
| [功能编号总表](docs/function-index.md) | 老同事 / 维护者 | 查 `P01`、`P03-2`、`V02` |
| [功能树](docs/function-tree.md) | 维护者 / 审核者 | 看功能层级和新版更新标注 |
| [同事更新流程](docs/coworker-codex-workflow.md) | 维护同事 | 用 Codex + GitHub Desktop 更新 |

## 功能总览

| 编号 | 大类 | 功能 |
| --- | --- | --- |
| `P01` | 图片 | 社媒图：游戏推荐、开奖、公告、收集引导、节日活动 |
| `P02` | 图片 | 白底图：人物、Banner、人物 + 文案、道具物料 |
| `P03` | 图片 | 私域图：公告、兑换码、贴纸风海报 |
| `P04` | 图片 | 人物 / KOL 图：新 KOL、已有 KOL 延展 |
| `P05` | 图片 | 产品 / 物料图 |
| `P06` | 图片 | 文案与标题 |
| `P07` | 图片 | 视觉诊断与质检 |
| `V01` | 视频 | 视频脚本 |
| `V02` | 视频 | 分镜图方案 |
| `V03` | 视频 | 中英文视频生成提示词 |
| `V04` | 视频 | 视频整包 |

## 仓库结构

```text
source/        正式规则源，日常维护先改这里
dist/          给线上 GPT、Codex、TG、公盘、提示词网站使用的发布文件
docs/          给团队看的说明
sync/          同步源文件
scripts/       同步脚本
maintenance/   发布、审查、更新交接模板
assets/        顺子形象和展示素材
```

## 上线 GPT 用这些

- Instructions：`dist/chatgpt/gpt-instructions.md`
- Knowledge：`dist/chatgpt/knowledge-shawn-core.md`
- 品牌卡：`dist/chatgpt/brands/品牌名/brand-card.md`
- 发布检查：`maintenance/release-package-template.md`

## TG / 公盘 / 提示词网站同步

先运行：

```powershell
scripts/sync-shawn-docs.ps1
```

生成结果在：

```text
dist/sync/
```

当前只生成帮助说明和同步文件，不自动移动公盘文件，不改 TG bot 的收集、下载、归档、重复检测逻辑。

## 顺子形象

![顺子头像](assets/showcase/shawn-portrait.png)

固定识别：黑色微卷短发、黑框眼镜、白衬衫、粉灰细条纹领带、蓝色牛仔裤、白鞋。

```text
把画面排明白，把审美落到位。
```

## 重要提醒

- 线上 GPT 仍由负责人最终上传。
- TG bot 真实 `config.json`、token、内部群信息不要提交到 GitHub。
- 大文件、PSD、视频工程放公司盘或 GitHub Release，只在品牌卡里写链接。
- 新增功能只追加编号，不重排旧编号。
