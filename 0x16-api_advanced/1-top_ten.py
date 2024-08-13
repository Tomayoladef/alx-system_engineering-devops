#!/urs/bin/pyton3
"""
    Uses reddit API to get 10hot posts
"""
import requests


def top_ten(subreddit):
    """Get 10 hot posts"""
    url = f"https://www.reddit.com/r/{subrddit}/hot.json?Limit=10"
    headers = {'user-agent': 'request'}
    response = request.get(url,  headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data =respose.json().get("data").get("children")
    top_10-posts = "\n".join(post.get("data").get("title") for post in data)
    print(top_10_posts)
