#!/usr/bin/env bash
# Build the static site so it serves from the *root* of GitHub Pages
# (https://bitscol-soft.github.io/stibuilders/) instead of /docs/.
#
# Run this only after Settings -> Pages -> "Folder" has been set to /docs.
# With that setting Pages publishes docs/ as the site root, so the branch
# root (settings.py, the SQL dump, the rest of the Django source) is no
# longer downloadable.
set -euo pipefail
cd "$(dirname "$0")/.."

REPO_SLUG="${REPO_SLUG:-bitscol-soft/stibuilders}"
BASE_PATH="/${REPO_SLUG#*/}/"

python3 manage.py test website
python3 manage.py collectstatic --noinput
rm -rf docs
python3 manage.py export_static --out docs --base-path "$BASE_PATH"
touch docs/.nojekyll
# The entry point at the repo root is only needed while Pages serves the
# branch root; once docs/ is the site root, docs/index.html is the entry.
if [ -f index.html ]; then
  echo "note: repo-root index.html is still present"
fi
echo "built docs/ with base path $BASE_PATH"
