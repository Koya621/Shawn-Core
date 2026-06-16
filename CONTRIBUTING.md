# 贡献与维护说明

这份文档给维护顺子 Shawn 的同事使用。

## 角色分工

- 维护人：可以修改核心规则、合并品牌规则、发布 GPT / Codex 版本。
- 贡献人：可以提交品牌素材、优秀案例、失败案例、提示词建议和 SOP 修正建议。

## 修改原则

1. 先改 `source/`，再同步 `dist/`。
2. 不要直接在 `dist/` 里发明新规则，避免源文件和发布文件不一致。
3. 新增提示词必须使用统一模板。
4. 新增品牌必须先填品牌卡。
5. 每次重要修改都要更新 `CHANGELOG.md`。
6. 每次功能更新都要写清 `P / V` 编号，例如 `P01-2` 或 `V03`。
7. 同事更新时走分支和 PR，不直接推送 `main`。

## 分支命名

```text
update/P编号-简短主题-YYYYMMDD
```

示例：

```text
update/P01-social-poster-20260616
update/V03-video-prompt-20260616
```

## 更新说明

每次更新复制 `maintenance/update-request-template.md`，另存为：

```text
maintenance/updates/shawn-update-YYYYMMDD-v01.md
```

负责人审核时，会看这里判断是否可以合并和上线 GPT。

## 新增品牌

1. 复制 `source/brands/_template/brand-card.md`。
2. 新建 `source/brands/品牌名/brand-card.md`。
3. 填写品牌名、别名、平台、尺寸、色彩、字体、素材、禁用项、案例链接。
4. 上传关键 logo 和 3-10 张优秀案例。
5. 大文件只放链接，不直接塞进 GPT Knowledge。

成功标志：用户输入品牌名时，顺子能说清这个品牌的风格、素材使用规则和禁用项。

## 新增提示词模板

1. 先判断它属于海报、修图、生图、视频、质检还是复盘。
2. 放入 `source/templates/` 对应模板。
3. 必须包含适用场景、固定格式、负面要求和确认点。
4. 同步更新 `dist/chatgpt/knowledge-shawn-core.md`。

成功标志：不同同事用同一个需求测试时，输出结构一致，不会每次换一套格式。

## 发布检查

发布前至少跑一遍 `maintenance/test-checklist.md`。

不要把未确认的品牌素材、敏感账号信息、内部群链接、客户隐私信息直接上传到公开仓库或 GPT Knowledge。
