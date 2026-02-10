import unittest
import subprocess
import sys
import os
import shutil

class TestCLICRUD(unittest.TestCase):
    def setUp(self):
        self.env = os.environ.copy()
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.env["PYTHONPATH"] = project_root
        
        self.test_dir = "test_env"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        self.cwd = self.test_dir

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def run_todo(self, args):
        cmd = [sys.executable, "../src/todo.py", "--no-banner"] + args
        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            env=self.env,
            cwd=self.cwd
        )
        if res.returncode != 0:
            print(f"\nCommand failed: {args}")
            print(f"STDOUT: {res.stdout}")
            print(f"STDERR: {res.stderr}")
        return res

    def test_crud_cycle(self):
        # 1. Add
        res = self.run_todo(["add", "Buy milk"])
        self.assertIn("Task added", res.stdout)
        
        # 2. List
        res = self.run_todo(["list"])
        self.assertIn("Buy milk", res.stdout)
        
        # 3. Update
        res = self.run_todo(["update", "1", "--description", "Buy oat milk"])
        self.assertIn("updated", res.stdout)
        
        # 4. Done
        res = self.run_todo(["done", "1"])
        if "completed" not in res.stdout:
            print(f"\nDONE FAILED. STDOUT: {res.stdout} STDERR: {res.stderr}")
        self.assertIn("completed", res.stdout)
        
        # 5. Delete
        res = self.run_todo(["delete", "1"])
        self.assertIn("deleted", res.stdout)

if __name__ == '__main__':
    unittest.main()
