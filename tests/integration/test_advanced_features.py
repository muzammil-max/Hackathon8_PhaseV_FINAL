import unittest
import subprocess
import sys
import os
import shutil

class TestAdvancedFeatures(unittest.TestCase):
    def setUp(self):
        self.env = os.environ.copy()
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.env["PYTHONPATH"] = project_root
        
        self.test_dir = "test_env_adv"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        self.cwd = self.test_dir

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def run_todo(self, args):
        cmd = [sys.executable, "../src/todo.py", "--no-banner"] + args
        return subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env=self.env,
            cwd=self.cwd
        )

    def test_add_advanced(self):
        res = self.run_todo(["add", "Urgent Task", "--priority", "high", "--tags", "work,urgent"])
        self.assertIn("Task added", res.stdout)
        
        # Verify listing shows it
        res = self.run_todo(["list"])
        self.assertIn("Urgent Task", res.stdout)
        # Note: We haven't implemented display of tags/priority in list yet, 
        # but command shouldn't fail.

    def test_filter_tasks(self):
        # Add mixed tasks
        self.run_todo(["add", "High Prio", "--priority", "high"])
        self.run_todo(["add", "Low Prio", "--priority", "low"])
        
        res = self.run_todo(["list", "--filter", "priority=high"])
        self.assertIn("High Prio", res.stdout)
        self.assertNotIn("Low Prio", res.stdout)

    def test_search(self):
        self.run_todo(["add", "Find Me"])
        self.run_todo(["add", "Hide Me"])
        
        res = self.run_todo(["search", "Find"])
        self.assertIn("Find Me", res.stdout)
        self.assertNotIn("Hide Me", res.stdout)

if __name__ == '__main__':
    unittest.main()
