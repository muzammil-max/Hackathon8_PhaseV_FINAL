import os
import sys
# Explicitly add the path where huggingface_hub is installed
sys.path.append(r"C:\Users\Muzammil\Desktop\Hackathon08 -Phase2\backend\venv\Lib\site-packages")
from huggingface_hub import HfApi

# Configuration
TOKEN = "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"
REPO_ID = "MuzammilMax/todo_app" # Extracted from your URL

api = HfApi()

def deploy():
    print(f"🚀 Starting deployment to Hugging Face Space: {REPO_ID}...")
    
    try:
        # Upload the entire backend folder content to the root of the Space
        api.upload_folder(
            folder_path=".", # Current dir (backend)
            repo_id=REPO_ID,
            repo_type="space",
            token=TOKEN,
            ignore_patterns=[
                "venv/*",
                "__pycache__/*",
                ".env",
                ".gitignore",
                "*.pyc",
                "test_*.py",
                "inspect_*.py",
                "debug_*.py",
                "reinspect_*.py",
                "test_agent.py",
                "deploy_hf.py" # Don't upload the deploy script itself
            ]
        )
        print("✅ SUCCESS! Files uploaded to Hugging Face.")
        print(f"🔗 View your space here: https://huggingface.co/spaces/{REPO_ID}")
    except Exception as e:
        print(f"❌ FAILED: {e}")

if __name__ == "__main__":
    # Ensure we are in the backend directory context
    deploy()
