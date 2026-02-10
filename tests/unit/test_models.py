import unittest
from src.models import Task, to_dict, from_dict

class TestTaskModelAdvanced(unittest.TestCase):
    def test_create_task_defaults(self):
        task = Task.create(1, "Basic")
        self.assertEqual(task.priority, "medium")
        self.assertEqual(task.tags, [])
        self.assertIsNone(task.due_date)

    def test_create_task_advanced(self):
        task = Task.create(
            1, "Adv", priority="high", tags=["work"], due_date="2026-01-01"
        )
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["work"])
        self.assertEqual(task.due_date, "2026-01-01")

    def test_from_dict_legacy(self):
        # Simulate loading v1.0 data (missing new fields)
        data = {
            'id': 1,
            'description': 'Legacy',
            'status': 'pending',
            'created_at': 'now',
            'updated_at': 'now'
        }
        task = from_dict(data)
        self.assertEqual(task.priority, "medium") # Default applied
        self.assertEqual(task.tags, [])

if __name__ == '__main__':
    unittest.main()