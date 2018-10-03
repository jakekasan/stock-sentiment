from config.data_sources import world_trading_data

import datetime as dt
import pandas as pd
import requests


class Data_Importer:
    def __init__(self,debug=False):
        self.data = {}
        self.debug = debug

    def load_data(self,name=None,date_from=None,date_to=None):
        """
            returns a DataFrame with the stock closing prices
        """

        if self.debug:
            print("Starting data import...")
            print("Name: {}".format(name))
            print("Date From: {}".format(date_from))
            print("Date To: {}".format(date_to))

        results = self.search(name=name,date_from=date_from,date_to=date_to)

        if results is None:
            return None

        price = [item["close"] for key,item in results.items()]
        date = [key for key,item in results.items()]

        df = pd.DataFrame({"date":date,"price":price})

        self.data[name] = df

        if self.debug:
            print("Data preview...")
            print(df.head())

        return df

    def search(self,name=None,date_from=None,date_to=None):
        try:
            if self.debug:
                print("Starting search for stock {}...".format(name))
            if name is None:
                return None

            date_to = date_to or dt.datetime.now()
            date_from = date_from or date_to - dt.timedelta(days=365)

            # format dates
            

            date_to = date_to.strftime("%Y-%m-%d")
            date_from = date_from.strftime("%Y-%m-%d")
            
            if self.debug:
                print("Date from set at {}\nDate to set at {}\n".format(date_from,date_to))

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
            if self.debug:
                print("Encountered problem searching for stock {}".format(name))

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

    # Non OO way ( classes are pointless here... )


def get_prices(name=None,date_from=None,date_to=None):
        results = search(name=name,date_from=date_from,date_to=date_to)

        if results is None:
            return None

        price = [item["close"] for key,item in results.items()]
        date = [key for key,item in results.items()]

        df = pd.DataFrame({"date":date,"price":price})

        print(df.head())

        return df

def search(name=None,date_from=None,date_to=None):
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