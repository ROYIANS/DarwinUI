---
name: darwinui-style-system
description: Use when designing or generating web pages and you want DarwinUI style selection and consistent application across four visual styles.
---

# DarwinUI Style System

Use this skill to choose and apply one DarwinUI style in a consistent way.

## Workflow

1. If user already named a style, use it directly.
2. If not, read `references/style-selection.md` and pick the closest style by task intent.
3. Load only the chosen style reference:
   - `references/editorial-ink.md`
   - `references/atelier.md`
   - `references/brutalist.md`
   - `references/journal.md`
4. Output in two blocks:
   - `Style Decision`: chosen style + why
   - `Implementation`: design tokens + component vocabulary + concrete UI output

## Output Contract

- Keep one dominant style. Do not mix multiple style grammars in the same page.
- Preserve readability before decoration.
- Reuse the style's color, type, spacing, and component syntax as a system.
- If user asks for code, include a CSS variable block first, then component structure.
