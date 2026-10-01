#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $(basename "$0") <JIRA-KEY> <image.png> [image2.png ...]" >&2
  exit 2
}

[[ $# -ge 2 ]] || usage

JIRA_KEY="$1"
shift

# Find the repository root so each user can keep their own credentials
# in <repo>/.env without putting secrets in the skill or in Git.
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$REPO_ROOT" ]]; then
  echo "Error: run this command from inside the Git repository." >&2
  exit 1
fi

ENV_FILE="$REPO_ROOT/.env"
if [[ ! -f "$ENV_FILE" ]]; then
  echo "Error: $ENV_FILE does not exist." >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

required=(JIRA_CLOUD_ID JIRA_EMAIL JIRA_API_TOKEN)
for name in "${required[@]}"; do
  if [[ -z "${!name:-}" ]]; then
    echo "Error: $name is missing from $ENV_FILE." >&2
    exit 1
  fi
done

UPLOAD_URL="https://api.atlassian.com/ex/jira/${JIRA_CLOUD_ID}/rest/api/3/issue/${JIRA_KEY}/attachments"

for IMAGE_PATH in "$@"; do
  if [[ ! -f "$IMAGE_PATH" ]]; then
    echo "Error: image not found: $IMAGE_PATH" >&2
    exit 1
  fi

  RESPONSE_FILE="$(mktemp)"
  trap 'rm -f "$RESPONSE_FILE"' EXIT

  HTTP_STATUS="$(
    curl --silent --show-error \
      --user "${JIRA_EMAIL}:${JIRA_API_TOKEN}" \
      --request POST \
      "$UPLOAD_URL" \
      --header "Accept: application/json" \
      --header "X-Atlassian-Token: no-check" \
      --form "file=@${IMAGE_PATH}" \
      --output "$RESPONSE_FILE" \
      --write-out "%{http_code}"
  )"

  if [[ "$HTTP_STATUS" != "200" ]]; then
    echo "Error: Jira attachment upload failed for $IMAGE_PATH (HTTP $HTTP_STATUS)." >&2
    cat "$RESPONSE_FILE" >&2
    exit 1
  fi

  # Keep the successful Jira response available to Claude. It contains the
  # attachment id/filename needed for the next Jira-comment step.
  cat "$RESPONSE_FILE"
  echo

  rm -f "$RESPONSE_FILE"
  trap - EXIT
done
