import praw

def redditScrape(maxNum):
    maxNum += 2
    linkList= []
    reddit = praw.Reddit(client_id = 'PpPWRzTFc6nfKQ',
                         client_secret = 'QrSKPiZsDBWIyaLPvBvlgZLh_IY',
                         username = 'ethanseow',
                         password = 'loler123',
                         user_agent = 'abc123')


    subreddit = reddit.subreddit('dankmemes')
                         
    hot_dankmemes = subreddit.hot(limit = maxNum)

    for submission in hot_dankmemes:
        if not submission.stickied:
            link = '{}{}'.format('https://www.reddit.com', submission.permalink)
            linkList.append(link)

    return linkList

