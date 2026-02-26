# Editorial Ink Guideline

## 1) 风格定位

`Editorial Ink` 是“报刊编辑部”语气：克制、理性、信息优先。  
适合内容平台、研究报告、深度博客、文档型官网。

## 2) 视觉 Token

- 主色：`#0f0e0c`（ink）
- 纸色：`#f5f0e8`（paper）
- 次纸色：`#ede8dc`（paper2）
- 强调色：`#c8391a`（accent）
- 次级文字：`#7a7468`（dim）
- 线条：`rgba(15,14,12,0.12)`（rule）

## 3) 字体系统

- 标题/正文：`Noto Serif SC`
- 标签/数据：`Space Mono`
- 辅助无衬线：`Noto Sans SC`

规则：
- 标题强调竖向节奏与粗细对比。
- 正文行距偏大（约 1.9）保证阅读呼吸。
- 标签和元信息统一等宽字，形成“编辑系统感”。

## 4) 布局与组件语法

- 顶部报头 + 主文档中轴。
- 章节有明确分割线和节奏间距。
- 高优先级组件：
  - Kicker / Lead / Pull Quote
  - Spec Block（深色规格块）
  - Stat Card / Data Bar
  - Table / Timeline / TOC
  - Do / Don't

## 5) 动效与交互

- 以“低干预”动效为主：淡入、轻微位移、滚动节奏。
- 避免夸张弹跳、过多旋转和强装饰性过场。

## 6) AI 生成提示词模板

```text
请按 DarwinUI 的 Editorial Ink 风格生成页面：
- 语气：编辑部、理性、克制
- 颜色：ink/paper + 少量 accent
- 字体：Noto Serif SC + Space Mono
- 组件：kicker、pull quote、spec block、table、timeline
- 要求：高可读性、清晰信息层级、少装饰
```

## 7) Do / Don't

- Do：优先信息层级和阅读节奏。
- Do：用强调色点到为止。
- Don't：把页面做成营销海报式大面积花哨视觉。
- Don't：过度使用圆角、阴影、渐变。
