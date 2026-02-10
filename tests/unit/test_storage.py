import unittest
import os
import json
from src.storage import save_tasks, load_tasks
from src.models import Task

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load(self):
        tasks = [Task.create(1, "Task 1"), Task.create(2, "Task 2")]
        save_tasks(tasks, self.test_file)
        
        loaded = load_tasks(self.test_file)
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].description, "Task 1")
        self.assertEqual(loaded[1].id, 2)

    def test_load_non_existent(self):
        loaded = load_tasks("non_existent.json")
        self.assertEqual(loaded, [])

    def test_load_empty_file(self):
        with open(self.test_file, 'w') as f:
            f.write('')
        loaded = load_tasks(self.test_file)
        self.assertEqual(loaded, [])

    def test_load_malformed_json(self):
        with open(self.test_file, 'w') as f:
            f.write('{ "tasks": [') # Incomplete
        loaded = load_tasks(self.test_file)
        self.assertEqual(loaded, [])

if __name__ == '__main__':
    unittest.main()
