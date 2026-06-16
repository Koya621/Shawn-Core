# ChatGPT 生图能力说明

## 结论

顺子可以通过规则提升“该生图时就调用生图”的命中率，但不能突破 ChatGPT 当前模型、账号、工作区或 GPT 配置限制。

## 必须开启

在自定义 GPT 设置里开启：

- Image generation
- File uploads

## 顺子内置兜底

如果当前模式支持图像生成，顺子可以直接生成。

如果当前模式不支持图像生成，顺子必须输出可复制提示词，并提示用户切换到支持图像生成的模型或 Images 入口。

## 官方参考

- Creating and editing GPTs: https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
- GPT-5.5 in ChatGPT: https://help.openai.com/articles/11909943

## 团队排查步骤

1. 检查 GPT 是否开启 Image generation。
2. 检查当前模型或模式是否支持图像生成。
3. 检查是否达到图片生成额度。
4. 如果不能直接生图，复制顺子输出的 Prompt 到 Images 入口。

成功标志：团队即使遇到不能直接生图，也能拿到完整提示词继续生产，不会卡在当前对话里。
