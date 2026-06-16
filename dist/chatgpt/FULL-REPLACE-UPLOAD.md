# 线上 GPT 全量替换上传说明

这份说明给负责人更新线上 GPT 使用。

## 结论

旧文件不用找了。线上 GPT 直接全量替换成这 3 个核心文件：

1. `dist/chatgpt/gpt-instructions.md`
2. `dist/chatgpt/knowledge-shawn-core.md`
3. `dist/chatgpt/brand-master-knowledge.md`

如果某个品牌正在重点上线，可以额外上传该品牌 logo 和 3-5 张精选案例图。

## 为什么不把全部品牌素材都上传 GPT

不建议全部上传。

原因：

- GPT Knowledge 文件数有限，官方说明自定义 GPT 最多可附加 20 个文件。
- 图片素材太多会让检索混乱。
- 大量历史图、PSD、视频工程不适合放 GPT。
- 品牌素材后续会经常变，全部上传会很难维护。
- 如果 GitHub 仓库是公开的，不能放敏感品牌素材、内部素材和客户隐私。

推荐做法：

```text
GPT：放轻量品牌知识和少量精选参考
GitHub：放品牌卡、规则、公开可放的轻量素材索引
公盘/TG bot/提示词网站：放完整素材、历史图、PSD、视频和可复用资源
```

## GPT 上传步骤

1. 打开 GPT 编辑页面。
2. 删除旧 Knowledge 文件。
3. Instructions 粘贴：

```text
dist/chatgpt/gpt-instructions.md
```

4. Knowledge 上传：

```text
dist/chatgpt/knowledge-shawn-core.md
dist/chatgpt/brand-master-knowledge.md
```

5. 如需要，额外上传当前重点品牌的 logo 和 3-5 张精选案例图。
6. 开启能力：

```text
Image generation
File uploads
```

7. 用这些话测试：

```text
顺子，P01，帮我写 X89 TG 游戏推荐海报提示词。
顺子，做一张私域兑换码图。
顺子，V01，写 15 秒 KOL 视频脚本。
顺子，V03，给我中英文视频提示词。
```

## 品牌素材后续怎么更新

### 小更新

适合：

- 改品牌色
- 改禁用项
- 补案例链接
- 补素材负责人
- 补 KOL 描述

流程：

1. 修改 `source/brands/品牌名/brand-card.md`。
2. 同步到 `dist/chatgpt/brand-master-knowledge.md`。
3. 线上 GPT 删除旧 `brand-master-knowledge.md`。
4. 上传新的 `brand-master-knowledge.md`。

### 大更新

适合：

- 新 logo
- 新 KOL
- 品牌视觉大改版
- 历史案例换一批

流程：

1. 修改品牌卡。
2. 公盘 / TG bot / 提示词网站替换完整素材。
3. GPT 只上传新的品牌卡文字和少量精选图。
4. 在 `maintenance/releases/` 写一份发布交接单。

## 成功标志

- 顺子能识别 P/V 编号。
- 不写编号也能自动判断。
- 提到品牌时，会先使用品牌知识。
- 品牌信息缺失时，顺子不会乱猜，会提醒“品牌素材待补充”。
