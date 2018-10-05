import datetime as dt
import requests

class News_Wrangler:
    """
        Gets raw news string from news source
    """
    def __init__(self):
        return

    def search(self,search=None,date=None,news_delay=3,just_results=False):
        """
            returns text from news source

            Params:
            @search : term(s) to search for
            @date : date of the price
        """

        if not date:
            date = dt.date.today()

        if type(date) == str:
            date = dt.datetime.strptime(date,"%Y-%M-%d")
        
        to_date = "{}-{}-{}".format(date.year,date.month,date.day)

        date = date - dt.timedelta(days=3)

        from_date = "{}-{}-{}".format(date.year,date.month,date.day)

        return self.api_search(search=search,from_date=from_date,to_date=to_date,news_delay=news_delay,just_results=just_results)


    def api_search(self,search=None,from_date=None,to_date=None,news_delay=None,just_results=False):
        return

        
        

        
        