# 公司电脑同步 Shawn-Core

这份说明给“另一台电脑”用，比如公司电脑。

目标只有一个：

让公司电脑和家里电脑都围绕同一个 `Shawn-Core` 仓库工作，不再靠重复聊天来补上下文。

## 仓库地址

```text
https://github.com/Koya621/Shawn-Core
```

## 最省事的方案

推荐使用 GitHub Desktop。

原因：

- 不用记命令。
- 能看见改了哪些文件。
- 点按钮就能拉取、提交、上传。
- 比手动压缩包来回传更稳定。

## 第一次在公司电脑上配置

1. 安装 GitHub Desktop  
   下载地址：

   ```text
   https://desktop.github.com
   ```

2. 登录和家里相同的 GitHub 账号。

3. 选择 `Clone a repository from the Internet`。

4. 搜索并选择：

   ```text
   Koya621/Shawn-Core
   ```

5. 选择一个本地保存位置，比如：

   ```text
   Documents/Shawn-Core
   ```

6. 点击 `Clone`。

完成后，公司电脑就拿到了和家里一致的 Shawn-Core。

## 每次开始工作前

先拉最新版本。

在 GitHub Desktop 里点击：

```text
Fetch origin
```

如果有新内容，再点：

```text
Pull origin
```

这样可以先拿到家里电脑最新升级过的 Shawn。

## 每次改完之后

1. 在 GitHub Desktop 左侧查看改动。
2. 确认改的是你想改的内容。
3. 在底部填写一次更新说明，例如：

   ```text
   update Shawn poster workflow
   ```

4. 点击：

   ```text
   Commit to main
   ```

5. 再点击：

   ```text
   Push origin
   ```

这样公司电脑的改动就会同步回 GitHub，家里电脑也能拉下来。

## 主要改哪些文件

如果是更新 Shawn 的能力，优先改这些位置：

- `codex-skill/Shawn/SKILL.md`
- `codex-skill/Shawn/references/shunzi-memory.md`
- `design-library/design-principles.md`
- `design-library/style-library.md`
- `design-library/prompt-patterns.md`
- `design-library/critique-checklist.md`
- `gpt-package/gpt-instructions.md`
- `gpt-package/knowledge-shawn-profile.md`
- `CHANGELOG.md`

## 建议工作方式

如果当天你只是：

- 调整顺子角色设定
- 增加一种设计风格
- 优化提示词写法
- 新增审美判断规则
- 记录一次成功案例

那就直接改 Shawn-Core，再提交。

不要等积累很多再一起改，不然以后会忘记为什么这么改。

## ChatGPT 网页端同步

GitHub 仓库更新后，不代表 ChatGPT 网页端的自定义 GPT 会自动更新。

网页端 GPT 仍然需要你手动把新版本内容上传进去。

需要同步时，优先更新：

- `gpt-package/gpt-instructions.md`
- `gpt-package/knowledge-shawn-profile.md`
- `design-library/` 里的相关知识文件
- `assets/shunzi-character-card.png`

## 推荐节奏

建议按这个节奏用：

1. 在公司或家里工作时，持续更新 Shawn-Core。
2. 每次完成一个小升级，就提交到 GitHub。
3. 另一台电脑开工前先拉最新版。
4. 当积累到一个阶段，再同步更新网页端 GPT。

## 如果你不想碰 Git 命令

完全没问题。

你以后只需要记住一件事：

始终在 GitHub Desktop 里做这三步：

1. 开始前 `Pull`
2. 改完后 `Commit`
3. 最后 `Push`

这就够了。
