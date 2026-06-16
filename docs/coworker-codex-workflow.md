# 同事用 Codex 更新顺子的流程

这份说明给需要维护顺子的同事使用。目标是：同事可以更新规则，你负责审核和上线 GPT，不会每次文件名都乱、更新内容说不清。

## 分工

- 同事：用 Codex 修改规则、补文档、准备更新说明、发 PR。
- 负责人：审核 PR，合并后更新线上 GPT。
- 线上 GPT 上传者：仍然是负责人，不建议多人直接操作同一个 GPT。

## 第一次准备

1. 安装 GitHub Desktop。
2. 登录自己的 GitHub 账号。
3. 克隆仓库：

```text
https://github.com/Koya621/Shawn-Core.git
```

4. 用 Codex 打开本地仓库。
5. 先看这三个文件：

```text
README.md
docs/shawn-user-guide.md
docs/function-index.md
```

成功标志：GitHub Desktop 左上角显示当前仓库是 `Shawn-Core`。

## 每次更新怎么做

### 1. 新建分支

不要直接改 `main`。

分支命名：

```text
update/F编号-简短主题-YYYYMMDD
```

示例：

```text
update/F03-poster-prompt-20260616
update/F12-video-script-20260616
update/F10-visual-review-20260616
```

### 2. 告诉 Codex 要改什么

推荐说法：

```text
请只优化 F03 海报提示词，不要改其他功能。
需要同步更新 source 和 dist/chatgpt。
最后帮我填写 maintenance/update-request-template.md 里的更新说明。
```

### 3. 修改范围

优先改：

```text
source/
docs/
maintenance/
dist/chatgpt/
dist/codex-skill/
```

不要上传：

```text
账号密码
内部群聊截图
客户隐私
没确认的大文件
PSD / AE / PR 工程
```

### 4. 填写更新说明

每次更新都要复制 `maintenance/update-request-template.md`，另存为：

```text
maintenance/updates/shawn-update-YYYYMMDD-v01.md
```

里面必须写清：

- 改了哪些功能编号
- 增加了哪些文件
- 删除了哪些文件
- 修复了什么问题
- 怎么测试
- 负责人上线 GPT 时要上传哪些文件

### 5. 提交 commit

commit 命名：

```text
Update F03 poster prompt format
Update F12 video script workflow
Fix F14 image fallback wording
```

### 6. 发 PR

在 GitHub Desktop 点 Push，再到 GitHub 创建 Pull Request。

PR 标题示例：

```text
Update F03 poster prompt format
```

PR 里必须按模板填写，不要只写“更新了一下”。

## 负责人怎么审核

审核时重点看：

- 功能编号是否写清楚。
- 有没有误改不相关功能。
- `source/` 和 `dist/chatgpt/` 是否同步。
- 是否写清增加/删除文件。
- 是否有测试结果。
- 是否影响线上 GPT 上传文件。

成功标志：负责人不用问第二遍，就能知道这次改了什么、为什么改、要上传什么。

## 常见错误

- 直接改 `main`。
- 文件名每次都叫 `新版.md`。
- 只改 `dist/`，忘了改 `source/`。
- 只写“优化提示词”，没写优化哪个功能编号。
- 删除文件不说明原因。
- 没有测试截图或测试文字。
