#!/bin/bash
# Commit and push everything that is not ignored.
#   scripts/save.sh "what changed"
# Refuses to commit anything that looks like an API key, or any file over 20 MB.
set -e
cd "$(dirname "$0")/.."
git add -A
if git diff --cached --quiet; then echo "Nothing to commit."; exit 0; fi

# --- safety checks on what is staged ---
if git diff --cached -U0 | grep -E '^\+' | grep -qiE 'ELEVENLABS_API_KEY=[A-Za-z0-9_-]{8,}|sk_[a-f0-9]{16,}|xi-api-key[:= ]+[A-Za-z0-9_-]{8,}'; then
  echo "STOPPED: a staged change looks like an API key. Unstaging."; git reset -q; exit 1
fi
big=$(git diff --cached --name-only | while read -r f; do if [ -f "$f" ] && [ "$(wc -c < "$f")" -gt 20000000 ]; then echo "$f"; fi; done || true)
if [ -n "$big" ]; then
  echo "STOPPED: files over 20 MB are staged:"; echo "$big"; git reset -q; exit 1
fi

git commit -q -m "${1:-Update}" -m "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
git pull --rebase --quiet origin main || { echo "Pull failed. Fix the conflict, then run again."; exit 1; }
git push --quiet origin main
echo "Pushed: $(git log --oneline -1)"
