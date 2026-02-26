import importlib.util
import shutil
import sys
import unittest
import uuid
from pathlib import Path

WORKSPACE_TMP = Path(__file__).resolve().parents[0] / ".tmp-tests"
WORKSPACE_TMP.mkdir(parents=True, exist_ok=True)


def _load_module():
    script_path = Path(__file__).resolve().parents[1] / "scripts" / "install_darwinui_skills.py"
    if not script_path.exists():
        raise FileNotFoundError(f"Missing script: {script_path}")
    spec = importlib.util.spec_from_file_location("install_darwinui_skills", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _mk_skill(base: Path, name: str, body: str = "# test") -> Path:
    p = base / name
    p.mkdir(parents=True, exist_ok=True)
    (p / "SKILL.md").write_text(body, encoding="utf-8")
    return p


def _case_dir() -> Path:
    p = WORKSPACE_TMP / f"case-{uuid.uuid4().hex}"
    p.mkdir(parents=True, exist_ok=False)
    return p


class DarwinUISkillInstallerTests(unittest.TestCase):
    def test_discover_skills_sorted_and_only_valid(self):
        root = _case_dir()
        try:
            skills_root = root / "skills"
            skills_root.mkdir()
            _mk_skill(skills_root, "darwinui-style-zeta")
            _mk_skill(skills_root, "darwinui-style-alpha")
            (skills_root / "not-a-skill").mkdir()

            m = _load_module()
            discovered = m.discover_skills(skills_root)
            self.assertEqual([s.name for s in discovered], ["darwinui-style-alpha", "darwinui-style-zeta"])
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_install_selected_skills_only(self):
        root = _case_dir()
        try:
            skills_root = root / "skills"
            dest = root / ".codex" / "skills"
            skills_root.mkdir(parents=True)
            _mk_skill(skills_root, "darwinui-style-a")
            _mk_skill(skills_root, "darwinui-style-b")

            m = _load_module()
            discovered = m.discover_skills(skills_root)
            result = m.install_skills(discovered, dest, selected={"darwinui-style-b"}, force=False)

            self.assertEqual(result["installed"], ["darwinui-style-b"])
            self.assertFalse((dest / "darwinui-style-a").exists())
            self.assertTrue((dest / "darwinui-style-b" / "SKILL.md").exists())
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_install_existing_without_force_raises(self):
        root = _case_dir()
        try:
            skills_root = root / "skills"
            dest = root / ".codex" / "skills"
            skills_root.mkdir(parents=True)
            _mk_skill(skills_root, "darwinui-style-a", body="new")
            _mk_skill(dest, "darwinui-style-a", body="old")

            m = _load_module()
            discovered = m.discover_skills(skills_root)
            with self.assertRaises(FileExistsError):
                m.install_skills(discovered, dest, selected=None, force=False)
        finally:
            shutil.rmtree(root, ignore_errors=True)

    def test_install_existing_with_force_overwrites(self):
        root = _case_dir()
        try:
            skills_root = root / "skills"
            dest = root / ".codex" / "skills"
            skills_root.mkdir(parents=True)
            _mk_skill(skills_root, "darwinui-style-a", body="new")
            _mk_skill(dest, "darwinui-style-a", body="old")

            m = _load_module()
            discovered = m.discover_skills(skills_root)
            result = m.install_skills(discovered, dest, selected=None, force=True)

            self.assertEqual(result["installed"], ["darwinui-style-a"])
            content = (dest / "darwinui-style-a" / "SKILL.md").read_text(encoding="utf-8")
            self.assertEqual(content, "new")
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
