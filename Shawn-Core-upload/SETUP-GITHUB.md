# Shawn-Core 上传 GitHub 指南

目标：创建一个私有 GitHub 仓库，用来同步 Shawn / 顺子的 Codex Skill 和 GPT Knowledge。

## 方式 A：最适合新手，使用 GitHub 网页上传

1. 打开 GitHub：

   ```text
   https://github.com
   ```

2. 登录账号。

3. 点击右上角 `+`，选择 `New repository`。

4. 填写：

   ```text
   Repository name: Shawn-Core
   Description: Shawn / 顺子的设计 Skill 与 GPT 知识库
   Visibility: Private
   ```

5. 不要勾选 `Add a README file`，因为本地已经有 README。

6. 点击 `Create repository`。

7. 进入新仓库页面后，点击 `uploading an existing file`。

8. 把本地这个文件夹里的内容拖进去：

   ```text
   /Users/kklm/Documents/Shawn-Core
   ```

   不要上传 `git-data` 文件夹。

9. 页面底部填写提交信息：

   ```text
   Initial Shawn Core knowledge base
   ```

10. 点击 `Commit changes`。

完成后，GitHub 上就有 Shawn-Core 了。

## 方式 B：之后更省事，使用 GitHub Desktop

GitHub Desktop 是 GitHub 官方桌面软件，适合不想记命令的人。

1. 下载：

   ```text
   https://desktop.github.com
   ```

2. 安装并登录 GitHub。
3. 选择 `File` -> `Add Local Repository...`。
4. 选择：

   ```text
   /Users/kklm/Documents/Shawn-Core
   ```

5. 如果提示不是 Git 仓库，选择创建仓库。
6. 点击 `Publish repository`。
7. 勾选 `Keep this code private`。
8. 点击发布。

## 公司电脑同步

公司电脑登录同一个 GitHub 账号后：

1. 打开 GitHub Desktop。
2. 找到 `Shawn-Core`。
3. 点击 `Clone`。
4. 以后每次更新：

   - 先点 `Fetch origin` / `Pull origin` 拉最新版。
   - 改完后写一句更新说明。
   - 点 `Commit`。
   - 点 `Push origin`。

## 网页端 GPT 更新

当 `gpt-package/` 或 `design-library/` 更新后：

1. 打开 ChatGPT 网页端。
2. 进入 Shawn GPT 的编辑页面。
3. 更新 Instructions。
4. 替换 Knowledge 里的对应文件。
5. 保存 GPT。

