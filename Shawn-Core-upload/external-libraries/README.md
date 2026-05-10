# Shawn 外部词库接入说明

这个目录用于登记和吸收外部 Prompt Library、设计资料库、风格参考仓库。

目标不是把大型外部仓库全文塞进 Shawn，而是把它们变成：

- 可检索的参考来源
- 可提炼的设计素材
- 可沉淀的规则输入

## 使用原则

Shawn 不直接记忆整个外部仓库。

Shawn 对外部仓库的正确处理方式是：

1. 先识别这个库适合解决什么问题
2. 再按任务类型筛选相关内容
3. 抽取出可复用的 prompt 模式、风格语言、控制规则和负面约束
4. 最后只把提炼后的结果写回 Shawn-Core

## 适合放在这里的内容

- GitHub prompt libraries
- 设计资源站
- 成熟项目的风格词汇表
- 角色动态、镜头、排版参考资源

## 不适合做的事

- 不要整库复制进 Skill
- 不要把海量原文当长期记忆
- 不要把重复、相似、未经筛选的 prompt 全塞进 GPT Knowledge

## 推荐工作流

1. 用户给外部仓库链接
2. Shawn 先判断任务目标
3. Shawn 只筛相关部分
4. Shawn 提炼成内部规则
5. 再更新：

- `design-library/`
- `case-library/`
- `gpt-package/`
- `CHANGELOG.md`
