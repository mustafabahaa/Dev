import re
import argparse
import sys


def main(branch_name):
    try:
        is_branch_name_valid = False

        # Check branch name format
        if not re.match(r"^issue_[0-9]+_[a-zA-Z0-9_-]{1,100}$", branch_name):
            print(
                "Branch names must follow the format 'issue_<issue-number>_short_description' with a short description not exceeding 100 characters.",
                file=sys.stderr,
            )
            print("Example: issue_15_canif_fix", file=sys.stderr)
            sys.exit(1)

        # Set validation flag
        is_branch_name_valid = True

        # Print result
        print(f"is_branch_name_valid={is_branch_name_valid}")

        if not is_branch_name_valid:
            sys.exit(1)

    except Exception as e:
        print(f"Error occurred while checking branch name: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch_name", help="Branch Name", required=True)
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(args.branch_name)
