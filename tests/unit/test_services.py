import unittest
from unittest.mock import patch, MagicMock
from src import services, models

class TestServices(unittest.TestCase):
    @patch('src.storage.load_tasks')
    @patch('src.storage.save_tasks')
    def test_add_task(self, mock_save, mock_load):
        mock_load.return_value = []
        task = services.add_task("Buy milk")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy milk")
        self.assertEqual(task.status, "pending")
        mock_save.assert_called_once()

    @patch('src.storage.load_tasks')
    @patch('src.storage.save_tasks')
    def test_add_task_increment_id(self, mock_save, mock_load):
        mock_load.return_value = [models.Task.create(1, "Existing")]
        task = services.add_task("New task")
        
        self.assertEqual(task.id, 2)

    @patch('src.storage.load_tasks')
    def test_list_tasks(self, mock_load):
        mock_load.return_value = [models.Task.create(1, "Task 1")]
        tasks = services.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "Task 1")

    @patch('src.storage.load_tasks')
    @patch('src.storage.save_tasks')
    def test_update_task(self, mock_save, mock_load):
        existing = models.Task.create(1, "Old")
        mock_load.return_value = [existing]
        
        updated = services.update_task(1, "New")
        self.assertIsNotNone(updated)
        self.assertEqual(updated.description, "New")
        mock_save.assert_called_once()

    @patch('src.storage.load_tasks')
    @patch('src.storage.save_tasks')
    def test_delete_task(self, mock_save, mock_load):
        existing = models.Task.create(1, "To Delete")
        mock_load.return_value = [existing]
        
        result = services.delete_task(1)
        self.assertTrue(result)
        mock_save.assert_called()
        
        # Verify save called with empty list
        args, _ = mock_save.call_args
        self.assertEqual(len(args[0]), 0)

if __name__ == '__main__':
    unittest.main()
