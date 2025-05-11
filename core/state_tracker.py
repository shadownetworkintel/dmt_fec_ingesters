import json
import os
from datetime import datetime

STATE_FILE = "ingest_state.json"

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def get_last_run(name):
    state = load_state()
    return state.get(name)

def update_last_run(name):
    state = load_state()
    state[name] = datetime.now().isoformat()
    save_state(state)
