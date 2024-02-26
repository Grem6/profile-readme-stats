import os
from flask import Flask, jsonify, abort
import requests

# app = Flask(__name__)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# GitHub API Token
TOKEN = os.getenv("GITHUB_API_TOKEN")

if not TOKEN:
    # If the token is not set, abort the application
    abort(500, "GitHub API token not set")

headers = {"Authorization": f"token {TOKEN}"}

# GitHub username
USERNAME = "Grem6"


# Endpoint to fetch follower count
@app.route("/api/followers")
def followers_count():
    url = f"https://api.github.com/users/{USERNAME}"
    response = requests.get(url)
    data = response.json()
    followers = data.get("followers", 0)
    return str(followers)


# Endpoint to fetch repository count
@app.route("/api/repositories")
def repositories_count():
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url)
    data = response.json()
    repositories = len(data)
    return str(repositories)


# Endpoint to fetch number of commits
@app.route("/api/commits")
def commits_count():
    url = f"https://api.github.com/users/{USERNAME}/events"
    response = requests.get(url)
    commits_count = len(
        [event for event in response.json() if event["type"] == "PushEvent"]
    )
    return str(commits_count)


# Endpoint for the root path
@app.route("/")
def index():
    return "Welcome to the GitHub API Wrapper"


if __name__ == "__main__":
    app.run(debug=True)
