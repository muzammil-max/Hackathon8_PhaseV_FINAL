import unittest
import subprocess
import sys
import os

class TestCLIBanner(unittest.TestCase):
    def setUp(self):
        self.env = os.environ.copy()
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.env["PYTHONPATH"] = project_root

    def test_banner_display_startup(self):
        # Run todo.py with NO args -> should show banner then help
        result = subprocess.run(
            [sys.executable, "src/todo.py"], 
            capture_output=True, 
            text=True,
            env=self.env
        )
        # Check for ASCII art specific part
        self.assertIn("/_/", result.stdout) 
        self.assertIn("usage:", result.stdout)

    def test_no_banner_flag_startup(self):
        # Run todo.py with --no-banner only -> should suppress banner then show help (because no command)
        result = subprocess.run(
            [sys.executable, "src/todo.py", "--no-banner"], 
            capture_output=True, 
            text=True,
            env=self.env
        )
        # Should NOT contain ASCII art specific part
        self.assertNotIn("/_/", result.stdout)
        self.assertIn("usage:", result.stdout)

if __name__ == '__main__':
    unittest.main()
