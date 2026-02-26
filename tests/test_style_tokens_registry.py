import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKENS_FILE = ROOT / "styles" / "tokens" / "styles.tokens.json"


class StyleTokensRegistryTests(unittest.TestCase):
    def test_tokens_file_exists(self):
        self.assertTrue(TOKENS_FILE.exists(), f"Missing token registry: {TOKENS_FILE}")

    def test_tokens_registry_shape_and_paths(self):
        data = json.loads(TOKENS_FILE.read_text(encoding="utf-8"))
        self.assertIn("version", data)
        self.assertIn("styles", data)
        self.assertIn("extensions", data)
        self.assertIsInstance(data["styles"], list)
        self.assertGreaterEqual(len(data["styles"]), 4)

        style_ids = []
        for item in data["styles"]:
            for key in [
                "id",
                "displayName",
                "tone",
                "source",
                "tokens",
                "componentVocabulary",
            ]:
                self.assertIn(key, item, f"Missing {key} in style entry")
            self.assertIn("html", item["source"])
            self.assertIn("guideline", item["source"])
            self.assertTrue((ROOT / item["source"]["html"]).exists(), f"Missing html for {item['id']}")
            self.assertTrue((ROOT / item["source"]["guideline"]).exists(), f"Missing guideline for {item['id']}")
            self.assertIn("colors", item["tokens"])
            self.assertIn("typography", item["tokens"])
            self.assertIn("layout", item["tokens"])
            style_ids.append(item["id"])

        self.assertEqual(len(style_ids), len(set(style_ids)), "Style ids must be unique")

    def test_extensions_section_for_future_styles(self):
        data = json.loads(TOKENS_FILE.read_text(encoding="utf-8"))
        ext = data["extensions"]
        self.assertIn("requiredStyleFields", ext)
        self.assertIn("requiredTokenSections", ext)
        self.assertIn("addStyleChecklist", ext)
        self.assertIsInstance(ext["addStyleChecklist"], list)
        self.assertGreaterEqual(len(ext["addStyleChecklist"]), 3)


if __name__ == "__main__":
    unittest.main()
