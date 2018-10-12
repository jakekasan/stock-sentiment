from news_source.main import single_lookup, range_lookup
from nlptools.main import get_tokens, get_lemms, remove_stopwords

import pandas as pd

"""
    lets import some data
    (we'll just read from disc for now)
"""

# df = pd.read_csv("./../news-source/data/RBS.csv")
# df = df.head(300)

# query="RBS OR (Bank AND of AND England) OR brexit OR unemployment OR fraud"

# df["text"] = range_lookup(query=query,df=df,article_list=True,date_range=3,date_col="Date")

# df.to_csv("./test.csv")

# print("Done!")

# import processed data

df = pd.read_csv("./test.csv")

# get tokens
