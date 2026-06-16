# ChatGPT 上传检查清单

## 上传文件

- `gpt-instructions.md`：粘贴到 Instructions。
- `knowledge-shawn-core.md`：上传到 Knowledge。
- 需要用到的品牌卡：从 `source/brands/品牌名/brand-card.md` 上传。
- 关键 logo 和 3-10 张优秀案例：按实际需要上传。

## 上线前先看

- `docs/shawn-user-guide.md`：给团队看的顺子使用说明。
- `docs/function-index.md`：功能编号总表。
- `docs/function-tree.md`：功能树和新版更新标注。
- `maintenance/release-package-template.md`：每次上线前的发布交接单模板。

## GPT Capabilities

必须开启：

- Image generation
- File uploads

可选开启：

- Web search
- Code Interpreter / Data Analysis

## 成功标志

1. 输入“顺子，P01，帮我写 X89.com TG 游戏推荐海报提示词”，第一句是“兄弟，在呢”。
2. 输入“顺子，做一张私域兑换码图”，顺子能自动识别为 `P03-2`。
3. 输入“顺子，V02，做 8 张分镜图方案”，顺子会说明 16:9 画布、数字编号、不写文字标注。
4. 输入“顺子，V03，给我中英文视频提示词”，顺子会把中英文写在一起方便复制。
5. 当前模式不能生图时，会给可复制提示词和切换入口。

## TG / 公盘 / 提示词网站同步

如本次更新影响说明，运行：

```powershell
scripts/sync-shawn-docs.ps1
```

同步结果在：

```text
dist/sync/
```

## 生图问题排查

如果“均衡 / 高级 / Pro”之类模式无法直接生图，按 `maintenance/chatgpt-image-generation-notes.md` 排查。顺子规则只能做路由和兜底，不能突破平台当前限制。
