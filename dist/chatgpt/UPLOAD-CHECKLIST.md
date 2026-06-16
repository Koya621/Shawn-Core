# ChatGPT 上传检查清单

## 上传文件

- `gpt-instructions.md`：粘贴到 Instructions。
- `knowledge-shawn-core.md`：上传到 Knowledge。
- 需要用到的品牌卡：从 `source/brands/品牌名/brand-card.md` 上传。
- 关键 logo 和 3-10 张优秀案例：按实际需要上传。

## GPT Capabilities

必须开启：

- Image generation
- File uploads

可选开启：

- Web search
- Code Interpreter / Data Analysis

## 成功标志

1. 输入“顺子，帮我写 X89.com TG 活动海报提示词”，第一句是“兄弟，在呢”。
2. 输出包含设计判断、Prompt、Negative Prompt、后期排版建议、确认点。
3. 输入“白底图”时自动出现纯白背景和无飞散元素约束。
4. 当前模式不能生图时，会给可复制提示词和切换入口。

## 生图问题排查

如果“均衡 / 高级 / Pro”之类模式无法直接生图，按 `maintenance/chatgpt-image-generation-notes.md` 排查。顺子规则只能做路由和兜底，不能突破平台当前限制。
