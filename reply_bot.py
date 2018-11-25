import praw
import pdb
import re
import os

#creating an instance of reddit
reddit = praw.Reddit('bot1')

#create empty list if first instance of running code
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
#otherwise read and split the post id's
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

#test subreddit for inital bot
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    if submission.id not in posts_replied_to:
        #search titles regardless of case
        if re.search("a2 pulley", submission.title, re.IGNORECASE):
            #comment that is posted
            submission.reply("Check out the following article for self-care: https://theclimbingdoctor.com/pulley-injuries-explained-part-2/")
            #simple output check that it replied in console
            print("Bot replying to :", submission.title)

            #store id into list
            posts_replied_to.append(submission.id)
#now save that the post has been replied to.
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
