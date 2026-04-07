import requests
from constant import GITHUB_TOKEN

def create_review(owner, repo, pr_number, review_body, event):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "body": review_body,
        "event": event  # APPROVE, REQUEST_CHANGES, COMMENT
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("✅ Review submitted")
    else:
        print("❌ Failed:", response.status_code, response.text)