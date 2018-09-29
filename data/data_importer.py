from config.data_sources import world_trading_data

import datetime as dt
import pandas as pd
import requests


class Data_Importer:
    def __init__(self,name=None):
        self.name = name

    def set_name(self,name=None):
        self.name = name

    def get_data(self,name=None,from_date=None,to_date=None):
        data = pd.DataFrame(self.search(name=name,from_date=from_date,to_date=to_date))
        pass

    def search(self,name=name,from_date=None,to_date=None):

        if 
        if (date is not None) and (not isinstance(date,dt.datetime)):
            return print(self.error())
        try:
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

            return r.json()    
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