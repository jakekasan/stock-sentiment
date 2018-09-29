from config.data_sources import world_trading_data

import datetime as dt
import pandas as pd
import requests


class Data_Importer:
    def __init__(self,name=None):
        self.name = name

    def set_name(self,name=None):
        self.name = name

    def get_data(self,name=None,date_from=None,date_to=None):
        results = self.search(name=name,date_from=date_from,date_to=date_to)

        if results is None:
            return None

        price = [item["close"] for key,item in results.items()]
        date = [key for key,item in results.items()]

        df = pd.DataFrame({"date":date,"price":price})

        print(df.head())

        return None

    def search(self,name=None,date_from=None,date_to=None):
        try:
            if name is None:
                return None

            date_to = date_to or dt.datetime.now()
            date_from = date_from or date_to - dt.timedelta(days=365)
            

            params = {
                "api_token":world_trading_data["api_key"],
                "sort":"newest",
                "symbol":name,
                "date_from":date_from,
                "date_to":date_to
            }

            r = requests.get(world_trading_data["address"]["price"],params=params)

            return r.json()["history"]    
        except:
            return None


    def error(self):
        def no_name():
            return print("No name given to search for")
        def wrong_date_format():
            return print("Date must either be None or a datetime object")

        return {
            no_name,
            wrong_date_format
        }