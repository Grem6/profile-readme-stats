import os
from flask import Flask, jsonify, abort
import requests

app = Flask(__name__)

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
    response = requests.get(url, headers=headers)
    data = response.json()
    followers = data.get("followers", 0)
    return jsonify({"followers": followers})


# Endpoint to fetch repository count
@app.route("/api/repositories")
def repositories_count():
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url, headers=headers)
    data = response.json()
    repositories = len(data)
    return jsonify({"repositories": repositories})


if __name__ == "__main__":
    app.run(debug=True)
