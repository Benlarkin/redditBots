#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("climbing")
for submission in subreddit.hot(limit=5):
    print("title: ", submission.title)
    print("text: ", submission.selftext)
    print("score: ", submission.score)
    print("---------------\n")