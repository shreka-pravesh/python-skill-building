# Program to filter unwanted keywords from social media comments

blocked_keywords = {"spam", "follow", "subscribe", "giveaway"}
user_comments = [
    "Check out my page!",
    "Follow me for updates!",
    "This is so cool",
    "Subscribe to my channel",
    "Lovely post!"
]
clean_comments = []
for comment in user_comments:
    words = set(comment.lower().split())
    if words.isdisjoint(blocked_keywords):
        clean_comments.append(comment)
print(" Clean Comments (No spam):")
for c in clean_comments:
    print("-", c)
