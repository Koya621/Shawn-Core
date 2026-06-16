# 发布说明

## 发布到 ChatGPT

1. 打开自定义 GPT 编辑页。
2. 将 `dist/chatgpt/gpt-instructions.md` 内容复制到 Instructions。
3. 上传 `dist/chatgpt/knowledge-shawn-core.md`。
4. 按需要上传品牌卡和品牌关键素材。
5. 开启 Image generation。
6. 用 `maintenance/test-checklist.md` 测试。

成功标志：顺子能按统一模板输出，并能在生图不可用时给兜底提示词。

## 发布前交接单

每次正式更新线上 GPT 前，复制：

```text
maintenance/release-package-template.md
```

另存为：

```text
maintenance/releases/shawn-gpt-update-YYYYMMDD-v01.md
```

交接单必须写清：

- 影响哪些功能编号
- 上传哪些文件
- 删除哪些旧文件
- 测试结果是什么

## 发布到 Codex

1. 复制 `dist/codex-skill/Shawn/` 到 Codex skills 目录。
2. 重启或刷新 Codex。
3. 用“顺子”开头测试。

成功标志：第一句固定为“兄弟，在呢”，并按 DE 美术组规则执行。

## 发布前风险

- 不要上传客户隐私、账号密码、内部群聊记录。
- 不要把未经确认的品牌素材当作正式素材。
- 不要只更新 `dist/` 忘记更新 `source/`。
