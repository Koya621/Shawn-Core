# 顺子更新说明模板

复制本文件后，另存为：

```text
maintenance/updates/shawn-update-YYYYMMDD-v01.md
```

## 基础信息

- 更新标题：
- 更新人：
- 日期：
- 分支名：
- 关联功能编号：P__ / V__
- 是否需要负责人更新线上 GPT：是 / 否
- 是否需要同步 TG / 公盘 / 提示词网站：是 / 否

## 这次解决什么问题

请用简单话说明，不要只写“优化一下”。

```text
例：P03-2 兑换码图之前按钮感不够强，用户一眼看不出 code 要复制。
```

## 增加了什么

- 新增文件：
- 新增规则：
- 新增模板：
- 新增品牌素材：

## 删除了什么

- 删除文件：
- 删除规则：
- 删除原因：

如果没有删除，写“无”。

## 修改了什么

- 修改文件：
- 修改前问题：
- 修改后效果：

## 影响范围

- 影响功能编号：
- 影响 GPT 上传文件：
- 影响 Codex Skill：
- 影响 TG 同步文件：
- 影响公盘说明：
- 是否影响品牌卡：

## 测试记录

至少填写 2 条测试。

```text
测试 1：
输入：
输出是否符合预期：

测试 2：
输入：
输出是否符合预期：
```

## 负责人上线 GPT 时要做什么

需要上传：

- [ ] `dist/chatgpt/gpt-instructions.md`
- [ ] `dist/chatgpt/knowledge-shawn-core.md`
- [ ] 品牌卡：
- [ ] 其他：

需要删除旧 Knowledge 文件：

- [ ] 无
- [ ] 有，文件名：

## TG / 公盘 / 提示词网站同步

需要运行：

- [ ] `scripts/sync-shawn-docs.ps1`

需要同步：

- [ ] `dist/sync/tg-help.txt`
- [ ] `dist/sync/prompt-site-guide.html`
- [ ] `dist/sync/public-drive-guide.md`
- [ ] 无

## 风险和注意事项

- 是否有未确认素材：
- 是否包含内部隐私：
- 是否涉及 TG bot 程序逻辑：
- 是否需要进一步测试：
