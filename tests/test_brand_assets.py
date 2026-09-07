import json
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def png_size(path):
    with path.open("rb") as image:
        header = image.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"{path} is not a PNG")
    return struct.unpack(">II", header[16:24])


class BrandAssetTests(unittest.TestCase):
    def test_selected_master_matches_approved_concept(self):
        concepts = ROOT / "assets" / "brand" / "concepts"
        selection = json.loads((concepts / "selection.json").read_text(encoding="utf-8"))
        selected = concepts / selection["selectedConcepts"][0]
        master = ROOT / "assets" / "brand" / "faceslim-selected-master.png"
        supporting = concepts / selection["selectedSupportingConcepts"][0]
        self.assertEqual(selected.read_bytes(), master.read_bytes())
        self.assertTrue(supporting.is_file())
        self.assertEqual(4, len(list(concepts.glob("direction-*.png"))))

    def test_marketing_images_have_expected_dimensions(self):
        expected = {
            "assets/social-preview.png": (1280, 640),
            "assets/screenshots/workspace.png": (1440, 860),
            "assets/screenshots/presets.png": (1440, 860),
            "assets/screenshots/export.png": (1440, 860),
            "assets/screenshots/result-before-after.png": (1280, 640),
        }
        for relative, size in expected.items():
            self.assertEqual(size, png_size(ROOT / relative), relative)

    def test_public_version_strings_match(self):
        expected = "1.29.1"
        self.assertIn(f'VERSION = "{expected}"', (ROOT / "faceslim/runtime.py").read_text(encoding="utf-8"))
        self.assertIn(f"FaceSlim v{expected}", (ROOT / "FaceSlim.py").read_text(encoding="utf-8"))
        self.assertIn(f"FaceSlim v{expected}", (ROOT / "FaceSlim_v1.py").read_text(encoding="utf-8"))
        self.assertIn(f"version-{expected}-", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn(f"FaceSlim v{expected}", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
