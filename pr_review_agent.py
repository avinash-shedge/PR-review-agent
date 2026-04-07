
from pr_diff import get_pr_diff
from llm import review_pr
from review_comment import create_review


def parse_pr_url(url):
    parts = url.strip().split("/")
    owner = parts[3]
    repo = parts[4]
    pr_number = parts[6]
    return owner, repo, pr_number

def review_from_url(pr_url):
    owner, repo, pr_number = parse_pr_url(pr_url)

    print(f"Reviewing PR #{pr_number} from {owner}/{repo}")

    diff = get_pr_diff(owner, repo, pr_number)
    review = review_pr(diff)

    if "high" in review.lower():
        create_review(owner, repo, pr_number, review, "REQUEST_CHANGES")
    else:
        create_review(owner, repo, pr_number, review, "COMMENT")

    print("\n===== REVIEW =====\n")
    print(review)

# ---- Run ----
review_from_url("https://github.com/avinash-shedge/shopping-cart/pull/1")