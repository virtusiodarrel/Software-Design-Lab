#! python3
import praw
import pandas as import pd
import datetime as dt

reddit = praw.Reddit(client_id='nu_xchEsqSZqyA',
                     client_secret='EpD5-bQ_TxNC2-JeaEJkx6tgvdA',
                     user_agent='CPE106L Experiment 5',
                     username='G2-8',
                     password='')

subreddit = reddit.subreddit('leagueoflegends')

top_subreddit = subreddit.top(limit=50)

topics_dict = {"title": [],
               "score": [],
               "id": [], "url": [],
               "comms_num": [],
               "created": [],
               "body": []}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)


def get_date(created):
    return dt.datetime.fromtimestamp(created)


_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp=_timestamp)

topics_data.to_csv('LeagueofLegends.csv', index=False)
