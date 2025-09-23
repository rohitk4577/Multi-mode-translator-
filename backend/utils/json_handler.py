# backend/utils/json_handler.py
import json
import os
import threading
from typing import Dict, List, Any

DATA_DIR = "data"
RESULT_FILE = os.path.join(DATA_DIR, "results.json")
_lock = threading.Lock() # To prevent race conditions when writing to the file

def _ensure_file():
    """Ensures the data directory and results file exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(RESULT_FILE):
        with open(RESULT_FILE, "w") as f:
            json.dump([], f)

def save_result(data: Dict[str, Any]):
    """Appends a new result to the JSON file in a thread-safe manner."""
    _ensure_file()
    with _lock:
        try:
            with open(RESULT_FILE, "r+") as f:
                results = json.load(f)
                results.append(data)
                f.seek(0)
                json.dump(results, f, indent=2)
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is empty or corrupt, start fresh
            with open(RESULT_FILE, "w") as f:
                json.dump([data], f, indent=2)

def read_results() -> List[Dict[str, Any]]:
    """Reads all results from the JSON file."""
    _ensure_file()
    try:
        with open(RESULT_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []