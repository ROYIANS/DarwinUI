#!/usr/bin/env python3
"""Install DarwinUI skills from this repository into Codex skills directory."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SkillEntry:
    name: str
    path: Path


def discover_skills(skills_root: Path) -> list[SkillEntry]:
    if not skills_root.exists():
        return []
    entries: list[SkillEntry] = []
    for child in skills_root.iterdir():
        if child.is_dir() and (child / "SKILL.md").is_file():
            entries.append(SkillEntry(name=child.name, path=child))
    return sorted(entries, key=lambda item: item.name)


def _default_destination() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    if os.name == "nt":
        user_profile = os.environ.get("USERPROFILE")
        if user_profile:
            return Path(user_profile) / ".codex" / "skills"
    return Path.home() / ".codex" / "skills"


def install_skills(
    discovered: list[SkillEntry],
    destination: Path,
    selected: set[str] | None,
    force: bool,
) -> dict[str, list[str] | str]:
    by_name = {item.name: item for item in discovered}
    if selected is None:
        target_names = sorted(by_name.keys())
    else:
        unknown = sorted(selected - set(by_name.keys()))
        if unknown:
            raise ValueError(f"Unknown skills: {', '.join(unknown)}")
        target_names = sorted(selected)

    destination.mkdir(parents=True, exist_ok=True)
    installed: list[str] = []
    for name in target_names:
        source = by_name[name].path
        target = destination / name
        if target.exists():
            if not force:
                raise FileExistsError(f"Destination already exists: {target}")
            shutil.rmtree(target)
        shutil.copytree(source, target)
        installed.append(name)
    return {"installed": installed, "destination": str(destination)}


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install DarwinUI skills to local Codex directory.")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Repository root path. Default is the parent of this script.",
    )
    parser.add_argument(
        "--dest",
        default=None,
        help="Destination skills directory. Defaults to CODEX_HOME/skills or ~/.codex/skills.",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        default=None,
        help="Install only specified skill names (space-separated).",
    )
    parser.add_argument("--list", action="store_true", help="List discoverable skills only.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing installed skill folders.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    repo_root = Path(args.repo_root).expanduser().resolve()
    skills_root = repo_root / "skills"
    discovered = discover_skills(skills_root)
    if not discovered:
        print(f"No skills found under: {skills_root}")
        return 1

    if args.list:
        for skill in discovered:
            print(skill.name)
        return 0

    destination = Path(args.dest).expanduser().resolve() if args.dest else _default_destination()
    selected = set(args.only) if args.only else None
    result = install_skills(discovered, destination, selected=selected, force=args.force)

    print(f"Installed {len(result['installed'])} skill(s) to {result['destination']}:")
    for name in result["installed"]:
        print(f"- {name}")
    print("Restart Codex to pick up newly installed skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
