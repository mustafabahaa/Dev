import argparse
import json
import re
import sys

def extract_issue_id(pull_request_json):
    try:
        # Convert JSON string to Python dictionary
        pull_request = json.loads(pull_request_json)

        # Search for the issue ID using regex
        match = re.search(r'\*\*Issue ID:\*\* #(\d+)', pull_request.get("body", ""))

        if match:
            issue_id = match.group(1)
            print(f"issue_id={issue_id}")
        else:
            print("Issue ID not found in the pull request body.")
            print("Make sure you are using the pull request template.")
            sys.exit(1)

    except Exception as e:
        print(f"Error occurred while extracting issue ID: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--pull_request", help="Pull Request Object", required=True)
    args = parser.parse_args()

    # Call the function to extract issue ID
    extract_issue_id(args.pull_request)
