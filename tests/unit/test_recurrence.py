import unittest
from datetime import datetime, timedelta
from src.services import calculate_next_due

class TestRecurrence(unittest.TestCase):
    def test_daily_recurrence(self):
        start = "2026-01-01T10:00:00"
        next_due = calculate_next_due(start, "daily")
        self.assertEqual(next_due, "2026-01-02T10:00:00")

    def test_weekly_recurrence(self):
        start = "2026-01-01T10:00:00"
        next_due = calculate_next_due(start, "weekly")
        self.assertEqual(next_due, "2026-01-08T10:00:00")

    def test_monthly_recurrence(self):
        # Simplistic monthly (30 days) for now or real calendar?
        # Let's use 30 days for simplicity in MVP
        start = "2026-01-01T10:00:00"
        next_due = calculate_next_due(start, "monthly")
        # 2026-01-31
        self.assertTrue(next_due.startswith("2026-01-31") or next_due.startswith("2026-02-01"))

if __name__ == '__main__':
    unittest.main()
