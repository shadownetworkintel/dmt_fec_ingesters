#!/usr/bin/env python3
import argparse
import sys
import os
from dotenv import load_dotenv
from core.utils import get_committees_by_candidate_id

# Load environment first
load_dotenv()
env_mode = os.getenv("ENV_MODE", "dev") 
load_dotenv(dotenv_path=f".env.{env_mode}", override=True)

from core.utils import (
    list_committee_targets,
    add_committee_target, 
    remove_committee_target,
    enable_all_committees_mode
)
from core.logger import get_logger

logger = get_logger()

def main():
    parser = argparse.ArgumentParser(description="Manage committee targets")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List committees
    list_parser = subparsers.add_parser('list', help='List all committee targets')
    
    # Add committee
    add_parser = subparsers.add_parser('add', help='Add a committee target')
    add_parser.add_argument('committee_id', help='Committee ID (e.g., C00467571)')
    add_parser.add_argument('--name', help='Committee name')
    add_parser.add_argument('--description', help='Description')
    
    # Remove committee
    remove_parser = subparsers.add_parser('remove', help='Remove a committee target')
    remove_parser.add_argument('committee_id', help='Committee ID to remove')
    
    # Enable all committees mode
    all_parser = subparsers.add_parser('all', help='Enable all committees mode (deactivate all targets)')
    
    # Add by candidate
    add_by_cand_parser = subparsers.add_parser(
        'add-by-candidate',
        help='Add all committees associated with a candidate_id'
    )
    add_by_cand_parser.add_argument('candidate_id', help='Candidate ID (e.g., H0NY12345)')

    args = parser.parse_args()
    
    if args.command == 'list':
        targets = list_committee_targets()
        if targets:
            print("\nCommittee Targets:")
            print("-" * 80)
            for target in targets:
                status = "ACTIVE" if target['active'] else "INACTIVE"
                print(f"{target['committee_id']:<12} {status:<8} {target['committee_name'] or 'N/A'}")
        else:
            print("No committee targets found.")
            
    elif args.command == 'add':
        success = add_committee_target(args.committee_id, args.name, args.description)
        if success:
            print(f"Successfully added committee target: {args.committee_id}")
        else:
            print(f"Failed to add committee target: {args.committee_id}")
            sys.exit(1)
            
    elif args.command == 'remove':
        success = remove_committee_target(args.committee_id)
        if success:
            print(f"Successfully removed committee target: {args.committee_id}")
        else:
            print(f"Failed to remove committee target: {args.committee_id}")
            sys.exit(1)
            
    elif args.command == 'all':
        success = enable_all_committees_mode()
        if success:
            print("Successfully enabled all committees mode")
        else:
            print("Failed to enable all committees mode")
            sys.exit(1)
            
    elif args.command == 'add-by-candidate':
        candidate_id = args.candidate_id
        committees = get_committees_by_candidate_id(candidate_id)
        if not committees:
            print(f"No committees found for candidate_id: {candidate_id}")
            sys.exit(1)
        added = 0
        for committee in committees:
            success = add_committee_target(
                committee['committee_id'],
                committee.get('committee_name'),
                committee.get('candidate_ids')
            )
            if success:
                print(f"Added committee {committee['committee_id']}")
                added += 1
            else:
                print(f"Failed to add committee {committee['committee_id']}")
        print(f"Added {added} committees for candidate_id: {candidate_id}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()