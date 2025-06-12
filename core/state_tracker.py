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

def update_last_run(name, dt=None):
    state = load_state()
    state[name] = (dt or datetime.now()).isoformat()
    save_state(state)

def get_checkpoint(name):
    state = load_state()
    checkpoints = state.get("checkpoints", {})
    return checkpoints.get(name)

def update_checkpoint(name, checkpoint_data):
    state = load_state()
    if "checkpoints" not in state:
        state["checkpoints"] = {}
    state["checkpoints"][name] = checkpoint_data
    save_state(state)

def clear_checkpoint(name):
    state = load_state()
    if "checkpoints" in state and name in state["checkpoints"]:
        del state["checkpoints"][name]
        save_state(state)