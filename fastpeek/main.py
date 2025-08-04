import os
import subprocess
import sys

FILENAMES = {"diff": "diff.diff", "log": "log.txt", "status": "status.txt"}


def output_repo(repo_path: str):
    """Generate git output files using shell redirection"""

    for filename in FILENAMES.values():
        if os.path.exists(filename):
            os.remove(filename)

    subprocess.run(f"git status > {FILENAMES['status']}", shell=True, cwd=repo_path)
    subprocess.run(f"git log -1 > {FILENAMES['log']}", shell=True, cwd=repo_path)

    # TODO add diff


def run():
    """Run the fastpeek analysis"""
    current_dir = os.getcwd()

    if not os.path.exists(os.path.join(current_dir, ".git")):
        print("Error: Not in a git repository")
        sys.exit(1)

    output_repo(current_dir)
    print("Git output files created successfully")


if __name__ == "__main__":
    run()
