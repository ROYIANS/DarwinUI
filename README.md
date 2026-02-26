# DarwinUI

DarwinUI 是一个面向 AI 时代网页设计协作的风格库。  
项目目标是：让人和 AI 都能快速理解、复用、落地一致的视觉风格。

## 项目结构

```text
DarwinUI/
├─ styles/
│  ├─ editorial-ink/
│  │  ├─ index.html
│  │  └─ guideline-readme.md
│  ├─ atelier/
│  │  ├─ index.html
│  │  └─ guideline-readme.md
│  ├─ brutalist/
│  │  ├─ index.html
│  │  └─ guideline-readme.md
│  ├─ journal/
│  │  ├─ index.html
│  │  └─ guideline-readme.md
│  └─ README.md
└─ skills/
   ├─ darwinui-style-system/
   │  ├─ SKILL.md
   │  └─ references/
   ├─ darwinui-style-editorial-ink/
   │  └─ SKILL.md
   ├─ darwinui-style-atelier/
   │  └─ SKILL.md
   ├─ darwinui-style-brutalist/
   │  └─ SKILL.md
   └─ darwinui-style-journal/
      └─ SKILL.md
```

## 四种风格

1. `editorial-ink`：报刊感、克制、信息密度高。
2. `atelier`：夜间工作室气质，深色、精致、展陈感强。
3. `brutalist`：高冲突、高对比、网格和文字图形化。
4. `journal`：手账拼贴、轻松、温暖、拟物纸感。

详细规则请看：
- `styles/editorial-ink/guideline-readme.md`
- `styles/atelier/guideline-readme.md`
- `styles/brutalist/guideline-readme.md`
- `styles/journal/guideline-readme.md`

## Skill 化使用（给 AI 调用）

你现在可以把 DarwinUI 作为 skill 安装到 Codex：

1. 安装总控技能（推荐）  
   `install-skill-from-github.py --repo <your-org>/<your-repo> --path skills/darwinui-style-system`
2. 按需安装单风格技能（可选）  
   `install-skill-from-github.py --repo <your-org>/<your-repo> --path skills/darwinui-style-journal`

如果你是在本地直接试用，也可以把对应技能目录复制到：
- Windows: `%USERPROFILE%\\.codex\\skills\\`
- macOS/Linux: `~/.codex/skills/`

安装后重启 Codex，示例调用：
- `使用 $darwinui-style-system，帮我做一个 SaaS 官网首页，偏品牌高级感。`
- `使用 $darwinui-style-brutalist，做一个活动落地页 hero。`
- `使用 $darwinui-style-journal，做一个社区周报页面。`

## 本地一键安装脚本

仓库内提供了自动发现技能并安装的脚本（新增 style skill 时无需改脚本）：

```bash
python scripts/install_darwinui_skills.py --list
python scripts/install_darwinui_skills.py
```

常用参数：
- `--only darwinui-style-system darwinui-style-journal` 只装指定技能
- `--dest <path>` 指定目标目录
- `--force` 覆盖已安装目录

## 统一 Token Registry

统一风格 token 文件：
- `styles/tokens/styles.tokens.json`

新增风格模板：
- `styles/tokens/style-template.json`

这个 registry 提供：
- 四种风格统一结构（颜色/字体/布局/组件词汇）
- 每种风格到 HTML、guideline、skill 的映射
- `extensions` 区域中的新增风格检查清单

## 使用建议

1. 先定风格，再写结构和内容。
2. 风格切换时，优先替换 token（颜色/字体/间距/组件语气），不要只换配色。
3. 生成新页面时，先让 AI 输出「风格决策摘要」，再输出代码，稳定性更高。
4. 新增 style 时，按 `styles.tokens.json` 的 `addStyleChecklist` 逐项补齐。
