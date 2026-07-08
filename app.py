# app.py
# Sample Python application with hardcoded secrets
# Committed to a PUBLIC repo — GitGuardian will detect these immediately

import os
import boto3
import requests

# -------------------------------------------------------
# Hardcoded AWS credentials in public source code
# This is one of the most common and dangerous leak patterns
# -------------------------------------------------------
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# Hardcoded GitHub token
GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ012345"

# Hardcoded Stripe key
STRIPE_KEY = "sk_live_51ABCDEFGHIJKLMNOPQRSTUVWXabcdefghijklmnopqrstuvwxyz123456"

# OpenAI API key
OPENAI_API_KEY = "sk-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP12"


def get_s3_client():
    """Create an S3 client using hardcoded credentials."""
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name="us-east-1",
    )


def call_github_api(repo):
    """Call GitHub API using hardcoded token."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(
        f"https://api.github.com/repos/{repo}", headers=headers
    )
    return response.json()


if __name__ == "__main__":
    print("App running — secrets exposed in public repo!")
