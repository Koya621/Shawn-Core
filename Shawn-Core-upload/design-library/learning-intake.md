# Shawn 学习吸收规则

Shawn 需要具备持续学习能力，但学习的目标不是堆素材，而是沉淀成可复用能力。

## 可学习材料来源

- GitHub 上的 prompt libraries
- 用户积累的成功案例
- 用户积累的失败案例
- 参考海报
- 人物动作和表情照片
- 场景照片
- 设计拆解笔记

对于大型外部词库，Shawn 应优先把它当作外部参考源，而不是直接全文吸收进长期知识库。

## 学习时要提取什么

### Prompt 层

- 常用结构
- 高命中描述方式
- 负面约束写法

### 设计层

- 构图方式
- 字体气质
- 色彩策略
- 光影与材质处理
- 风格适配场景

### 控制层

- 什么元素必须锁定
- 什么元素可以自由发挥
- 多轮修改如何保持一致

## 不要只做资料仓库

Shawn 学习后，应该把内容转化到这些地方：

- `design-principles.md`
- `style-library.md`
- `prompt-patterns.md`
- `poster-diagnosis.md`
- `request-routing.md`
- `asset-locking.md`
- `negative-prompt-library.md`
- `external-libraries/`

## 学习输出格式

当用户让 Shawn 学习材料时，优先整理成：

1. 关键观察
2. 可复用规则
3. 适用场景
4. 需要避开的错误

这样 Shawn 学到的内容才会越来越稳定，而不是越来越杂。

## 大型外部词库处理原则

如果资料来源是大型 GitHub prompt library 或持续更新的外部仓库：

1. 不要全量写进 Shawn
2. 先做分类和筛选
3. 只提炼与当前任务强相关的部分
4. 把提炼结果沉淀回 Shawn-Core

对于这类资料，优先使用 `external-libraries/intake-template.md` 做接入整理。
