import unittest
from datetime import datetime
from src.utils import parse_date, format_date

class TestUtils(unittest.TestCase):
    def test_parse_date_iso(self):
        iso = "2026-01-01T10:00:00"
        self.assertEqual(parse_date(iso), iso)

    def test_parse_date_natural(self):
        # This requires dateutil. If not present, might fail or return None
        # We assume dev env has it.
        try:
            import dateutil
            res = parse_date("2026-01-01")
            self.assertTrue(res.startswith("2026-01-01"))
        except ImportError:
            pass

    def test_parse_invalid(self):
        self.assertIsNone(parse_date("not a date"))

    def test_format_date(self):
        iso = "2026-01-01T10:30:00"
        self.assertEqual(format_date(iso), "2026-01-01 10:30")

if __name__ == '__main__':
    unittest.main()
