from typing import Optional
from datetime import datetime
import subprocess
import platform
import os

try:
    from dateutil import parser
except ImportError:
    parser = None

def parse_date(date_str: str) -> Optional[str]:
    if not date_str: return None
    if not parser:
        try: return datetime.fromisoformat(date_str).isoformat()
        except: return None
    try:
        dt = parser.parse(date_str)
        return dt.isoformat()
    except: return None

def format_date(date_str: str) -> str:
    if not date_str: return ""
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%Y-%m-%d %H:%M")
    except: return date_str

def send_notification(title: str, message: str):
    plt = platform.system()
    try:
        if plt == "Windows":
            command = f'[reflection.assembly]::loadwithpartialname("System.Windows.Forms"); $notification = new-object system.windows.forms.notifyicon; $notification.icon = [system.drawing.systemicons]::Information; $notification.visible = $true; $notification.showballoontip(5000, "{title}", "{message}", [system.windows.forms.tooltipicon]::Info)'
            subprocess.run(["powershell", "-Command", command], capture_output=True)
        elif plt == "Darwin":
            subprocess.run(["osascript", "-e", f'display notification "{message}" with title "{title}"'], capture_output=True)
        elif plt == "Linux":
            subprocess.run(["notify-send", title, message], capture_output=True)
    except: pass