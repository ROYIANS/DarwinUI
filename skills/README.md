# DarwinUI Skills

可安装技能：

1. `darwinui-style-system`（推荐，内置四种风格选择与应用）
2. `darwinui-style-editorial-ink`
3. `darwinui-style-atelier`
4. `darwinui-style-brutalist`
5. `darwinui-style-journal`

## GitHub 安装示例

```bash
install-skill-from-github.py --repo <your-org>/<your-repo> --path skills/darwinui-style-system
```

```bash
install-skill-from-github.py --repo <your-org>/<your-repo> --path skills/darwinui-style-journal
```

安装后重启 Codex 才会生效。

## 本地仓库快速安装

```bash
python scripts/install_darwinui_skills.py --list
python scripts/install_darwinui_skills.py
```

脚本会自动发现 `skills/` 下包含 `SKILL.md` 的目录，因此新增 style skill 后无需改脚本。
