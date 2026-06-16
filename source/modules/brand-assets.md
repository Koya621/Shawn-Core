# 模块：品牌资产调用

## 目标

用户提到固定品牌时，自动对应品牌素材、风格和禁用项。

## 品牌卡优先级

1. 用户当轮明确要求
2. `source/brands/品牌名/brand-card.md`
3. 历史优秀案例
4. DE 美术组通用 SOP

## 品牌卡字段

- 品牌名
- 别名
- 平台
- 常用尺寸
- 主色
- 辅助色
- 字体倾向
- 常用人物 / 游戏元素
- 风格关键词
- 禁用项
- 参考案例链接
- 素材负责人
- 更新时间

## 素材上传规则

每个品牌一个文件夹：

```text
source/brands/品牌名/
  brand-card.md
  logo-primary.png
  logo-primary.svg
  examples/
    good-01.png
    good-02.png
    good-03.png
  avoid/
    bad-01.png
```

GPT Knowledge 建议只上传：

- `brand-card.md`
- logo
- 3-10 张最稳定的历史优秀案例

PSD、工程文件、长视频、大体积素材放公司盘或 GitHub Release，在品牌卡里写链接。

## 品牌不确定时

先询问品牌，不要猜。多个品牌共用素材时，必须提醒用户确认。
