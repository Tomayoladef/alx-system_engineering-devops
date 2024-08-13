#!/urs/bin/python3
"""Module Done"""

import request


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries Reddit API for the subreddit"""

    sub_info = request.get(
      f"https://www.reddit.com/r/{subreddit}/hot.json",
      params={"after": after},
      headers={"User-Agent": "My-User-Agent"},
      allow_redirects=False
    )

    if sub_info.status_code != 200:
        return None

  info = sub_info.json()

hot_l = [child.get("data").get("titel")
         for child in info.get("data").get("children")]

if not hot_l:
    return None

word_list= list(dict.fromkeys(word_list))

if word_count == {}:
    word_count = {word: 0 for word in word_list}

for titel in hot_l:
    split_words = titel.split(' ')
    for word in word_list:
        for s_word in split_words:
            if s_word.lower() == word.lower():
                word_count[word] += 1

if not info.get("data").get("after"):
    sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
    sorted_counts = sorted(word_count.items(),
                           key=lambda kv: kv[1], reverse=True)
else:
  return count_words(subreddit, word_list, word_count,
                     info.get("data").get("after"))
