# Styles Index

DarwinUI 的四种风格模板已按文件夹拆分，每种风格都包含：
- `index.html`：可直接预览的完整样式页面
- `guideline-readme.md`：供 AI 和开发者快速复用的风格准则

## 风格目录

1. `styles/editorial-ink/`
2. `styles/atelier/`
3. `styles/brutalist/`
4. `styles/journal/`

## 建议流程

1. 先读该风格的 `guideline-readme.md`。
2. 再参考 `index.html` 的实际组件表现。
3. 最后在新页面中复用对应 token 和组件语法。

## 可扩展 Token 入口

- 统一 token registry: `styles/tokens/styles.tokens.json`
- 新风格模板: `styles/tokens/style-template.json`

后续新增风格时，先复制模板，再把条目追加到 `styles/tokens/styles.tokens.json` 的 `styles` 数组。
