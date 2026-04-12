# PR Review Agent

An automated tool that uses AI to review GitHub Pull Requests, providing intelligent feedback on code quality, bugs, security, and best practices..

## Features

- **Automated PR Review**: Analyzes pull request diffs using AI
- **Comprehensive Analysis**: Checks for bugs, security issues, performance concerns, and code quality
- **GitHub Integration**: Fetches PR diffs and posts review comments directly on GitHub
- **Configurable Reviews**: Can approve, request changes, or just comment based on findings
- **JSON Output**: Structured review feedback with severity levels and suggestions

## Prerequisites

- Python 3.7+
- [Ollama](https://ollama.ai/) installed and running
- Llama 3 model: `ollama pull llama3`
- GitHub Personal Access Token with `repo` permissions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/avinash-shedge/PR-review-agent.git
cd PR-review-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your GitHub token:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Usage

Run the PR review agent with a GitHub PR URL:

```bash
python pr_review_agent.py
```

The script is currently hardcoded to review a specific PR. To review a different PR, modify the URL in `pr_review_agent.py` or extend the script to accept command-line arguments.

## Configuration

- **GITHUB_TOKEN**: Set this environment variable to your GitHub Personal Access Token
- **Model**: Currently uses `llama3`. Change in `llm.py` if needed
- **Prompt**: Customize the review criteria in `prompt.txt`

## How It Works

1. **Fetch PR Diff**: Retrieves the diff from GitHub API
2. **AI Analysis**: Sends the diff to Ollama/Llama3 for analysis using a structured prompt
3. **Review Posting**: Posts the AI-generated review as a comment on the PR
4. **Decision Making**: Based on the review content, decides whether to approve or request changes

## Project Structure

- `pr_review_agent.py`: Main script that orchestrates the review process
- `pr_diff.py`: Fetches pull request diffs from GitHub
- `llm.py`: Handles AI-powered code review using Ollama
- `review_comment.py`: Posts review comments to GitHub
- `constant.py`: Configuration constants
- `prompt.txt`: System prompt for the AI reviewer
- `requirements.txt`: Python dependencies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Security Note

Never commit GitHub tokens or other secrets to version control. This project uses environment variables for secure token management.