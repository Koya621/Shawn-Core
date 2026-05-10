# 创建 Shawn 网页端 GPT

这份说明是给 ChatGPT 网页端用的。

目标：

创建一个叫 `Shawn` 的自定义 GPT，让它在网页端也能延续顺子的角色设定、设计工作流和知识库。

## 进入位置

打开 ChatGPT 网页端后，进入：

```text
Explore GPTs
```

然后选择：

```text
Create
```

## 基本信息

创建时建议填写：

### Name

```text
Shawn
```

### Description

```text
你的海报设计搭子，擅长角色海报、商业视觉、提示词优化和风格判断。
```

### Avatar

可以先不设置，或者后续用顺子的角色形象图来做。

## Instructions

把下面这个文件内容完整粘进去：

[gpt-instructions.md](/Users/kklm/Documents/Shawn-Core/gpt-package/gpt-instructions.md)

这是 Shawn 在网页端最核心的人设和工作流。

## Knowledge 要上传什么

建议上传这些文件：

1. [knowledge-shawn-profile.md](/Users/kklm/Documents/Shawn-Core/gpt-package/knowledge-shawn-profile.md)
2. [design-principles.md](/Users/kklm/Documents/Shawn-Core/design-library/design-principles.md)
3. [style-library.md](/Users/kklm/Documents/Shawn-Core/design-library/style-library.md)
4. [prompt-patterns.md](/Users/kklm/Documents/Shawn-Core/design-library/prompt-patterns.md)
5. [critique-checklist.md](/Users/kklm/Documents/Shawn-Core/design-library/critique-checklist.md)
6. [shunzi-character-card.png](/Users/kklm/Documents/Shawn-Core/assets/shunzi-character-card.png)

这 6 个文件已经足够让 Shawn 在网页端进入可用状态。

## Capabilities 建议

建议开启：

- 图片生成
- 网页浏览

如果后续你希望 Shawn 在网页端也能更方便查资料、做参考图分析，这两个能力都值得保留。

## 推荐开场测试

创建完后，可以直接用这几句测试它：

```text
顺子，请根据这张参考图帮我做一版 16:9 海报，先给提示词。
```

```text
顺子，帮我把这个标题做得更有设计感，但不要太杂。
```

```text
顺子，帮我判断这张海报的问题，重点看构图、字体和气质。
```

## 以后怎么更新 GPT

Shawn-Core 仓库更新后，网页端 GPT 不会自动同步。

每次你想把 GPT 也升级时，按这个顺序更新最省事：

1. 替换 Instructions  
   使用最新版：

   [gpt-instructions.md](/Users/kklm/Documents/Shawn-Core/gpt-package/gpt-instructions.md)

2. 替换或补充 Knowledge 文件  
   重点看：

   - `knowledge-shawn-profile.md`
   - `design-library/` 下相关文件
   - `assets/shunzi-character-card.png`

## 建议节奏

不要每改一点就立刻重传 GPT。

更好的方式是：

1. 先持续更新 GitHub 仓库里的 Shawn-Core。
2. 等积累到一个阶段，再统一更新网页端 GPT。

这样更稳定，也更省事。
