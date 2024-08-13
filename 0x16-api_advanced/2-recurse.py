#!/urs/bin/python3
"""
    Uses Reddit API to get all hot posts
"""
import request


def recures(subreddit, hot_List=[], after""):
    """Get all hot posts"""
    if after is None:
        return []

  url= f"https://www.reddit.com/r/{subreddit}/hot.json"
  url +=f"?limit=100&after={after}"
  headers = {'user-agent': 'request'}
  response = request.get(url, headers=headers, allow_redirects=False)

  if response.status_code != 200:
      return None

  r_json = response. json()
  hot_posts_json = r_json.get("data").get("children")

  for post in hot_posts_json: 
      hot_list.append(post.get("data").get("titel"))
  return hot_list + recurse(subreddit, [], r_json.get("data").get("after"))
