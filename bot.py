from dotenv import load_dotenv
import pandas as pd
import os
import twitter

load_dotenv()

api = twitter.Api(consumer_key=os.environ["consumer_key"],
                  consumer_secret=os.environ["consumer_secret"],
                  access_token_key=os.environ["access_token_key"],
                  access_token_secret=os.environ["access_token_secret"])

selected = pd.read_csv("database.csv").sample()

if selected["path"].isna():
    status = "キー\t：{}\n動作\t：{}\nシーン\t：{}\n\n{}".format(*selected)
    # api.PostUpdate(status)
else:
    status = "キー\t：{}\n動作\t：{}\nシーン\t：{}\n\n{}".format(*selected[:-1])
    media_path = "screenrecord/" + str(selected[-1]) + ".gif"
    # api.PostUpdate(status, media=media_path)

print(status)
