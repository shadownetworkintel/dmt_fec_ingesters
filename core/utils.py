import yaml
import os

CONFIG_FILE = "configs/committee_ingest_targets.yaml"

def load_committee_list():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = yaml.safe_load(f)
        committee_ids = config.get("committee_ids", [])
        if isinstance(committee_ids, str) and committee_ids.lower() == "all":
            return []  # returning empty triggers all-committee run
        return committee_ids
    else:
        print(f"Configuration file {CONFIG_FILE} not found.")
        return []