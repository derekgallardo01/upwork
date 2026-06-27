#!/usr/bin/env bash
# Initialize each standalone package as its own git repo with a first commit,
# then print the commands to add a remote and push. It does NOT create GitHub
# repos and does NOT push — you stay in control of what goes public.
#
# Usage:  bash standalone/init-repos.sh [your-github-username]
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
USER_NAME="${1:-<you>}"

for dir in "$HERE"/*/; do
  name="$(basename "$dir")"
  # skip non-package files
  [ -f "$dir/README.md" ] || continue

  if [ -d "$dir/.git" ]; then
    echo "• $name — already a git repo, skipping init"
  else
    git -C "$dir" init -q
    git -C "$dir" add -A
    git -C "$dir" commit -q -m "Initial commit"
    git -C "$dir" branch -M main
    echo "• $name — initialized + committed"
  fi

  echo "    Next, create an empty repo named '$name' on GitHub, then run:"
  echo "      git -C '$dir' remote add origin https://github.com/$USER_NAME/$name.git"
  echo "      git -C '$dir' push -u origin main"
  echo
done

echo "Done. Review each repo, then run the remote-add + push lines above."
