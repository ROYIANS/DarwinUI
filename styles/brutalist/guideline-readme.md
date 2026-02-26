# Brutalist Guideline

## 1) 风格定位

`Brutalist` 是“文字即图形”的冲突型表达：强网格、强边框、强对比。  
适合活动页、宣言页、实验品牌、需要视觉记忆点的专题。

## 2) 视觉 Token

- 底色：`#f2f0eb`（white）/ `#e8e5de`（off）
- 字色：`#0d0d0b`（ink）
- 强调红：`#e3210a`（red）
- 线条：`rgba(13,13,11,0.12)`（rule）

## 3) 字体系统

- 超大标题：`Bebas Neue`
- 结构与正文：`IBM Plex Sans` / `IBM Plex Mono`
- 中文支持：`Noto Sans SC`

规则：
- 大字、窄行高、硬边界是核心视觉语言。
- 等宽字用于元信息、编号、标签和数据。
- 中英混排时先保证节奏，再微调字重。

## 4) 布局与组件语法

- 明显网格切割（横条、竖列、分栏对撞）。
- 边框既是结构也是视觉元素。
- 高优先级组件：
  - Kicker / Badge / Pull Quote
  - Number Grid / Stat Card / Data Bar
  - Table / Timeline / TOC
  - Figure / Rule / Chapter Opener / Annotation

## 5) 动效与交互

- 可以使用 ticker、硬切换、位移动效。
- 动效应服务“冲突感”，但不能破坏可读性。

## 6) AI 生成提示词模板

```text
请按 DarwinUI 的 Brutalist 风格生成页面：
- 语气：强烈、直接、实验感
- 颜色：黑白为主，红色作为唯一高强度强调
- 字体：Bebas Neue + IBM Plex Mono/Sans
- 组件：grid、ticker、number blocks、硬边框表格
- 要求：视觉冲突明确，但信息仍可快速扫描
```

## 7) Do / Don't

- Do：把网格、边框和字号对比用到位。
- Do：控制强调色数量（通常只用红）。
- Don't：叠加太多阴影、圆角、玻璃拟态。
- Don't：在同一屏中混入多个审美体系。
