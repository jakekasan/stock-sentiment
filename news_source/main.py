from news_source.tools.data_handler import Data_Handler
from news_source.sources.news_wrangler import News_Wrangler
from news_source.sources.guardian import Guardian
from config import news_sources as config
from news_source.tools.ticker_lookup import ticker_lookup

import datetime as dt
import numpy as np
import os
import pandas as pd
import re

class News_Source():
    def __init__(self,df=None,date_col=None):
        pass

    def get_text_data(self,df=None,date_col=None):
        pass





# def main():

#     pwd = os.getcwd()

#     if "data" not in [x for x in os.listdir(pwd) if os.path.isdir(x)]:
#         print("No data directory")
#         return

#     data_dir = os.path.join(pwd,"data")

#     csv_regex = re.compile(r"(.*)\.csv")

#     companies = {}

#     for f in os.listdir(data_dir):
#         match = csv_regex.match(f)
#         companies[match.group(1)] = str(match.group())

#     for company,filename in companies.items():
#         df = pd.read_csv(os.path.join("./data",filename))
#         print("Read data for {}".format(company))
#         print(df.head())

#     #ticker_lookup("RBS")
#     return

#     df["date"] = df["Date"].apply(lambda x: dt.datetime.strptime(x,"%Y-%M-%d"))

#     print(df.head())

#     df["name"] = df.apply(lambda x: "RBS",axis=1)

#     df = df.head(20)

#     dh = Data_Handler()

#     results = dh.run(df)

#     print(results.tail(1)["raw_text_guardian"].values)

if __name__ == '__main__':
    main()