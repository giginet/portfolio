#!/usr/bin/env python3
"""Fetch GitHub star counts for listed repositories."""

import json
import urllib.request

REPOS = [
    "giginet/Scipio",
    "giginet/Crossroad",
    "giginet/xcprofiler",
    "giginet/swift-testing-revolutionary",
    "giginet/Toybox",
    "giginet/NESEmulator-watchOS",
    "giginet/xcodeproj-mcp-server",
    "giginet/Peafowl",
]

OUTPUT_PATH = "data/stars.json"


def main():
    stars = {}
    for repo in REPOS:
        url = f"https://api.github.com/repos/{repo}"
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            stars[repo] = data.get("stargazers_count", 0)
        print(f"  {repo}: {stars[repo]}")

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(stars, f, indent=2)

    print(f"Wrote star counts to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
