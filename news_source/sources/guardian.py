from config.sources import guardian as api
import requests
from sources.news_wrangler import News_Wrangler

address = "https://content.guardianapis.com/search"

class Guardian(News_Wrangler):
    def __init__(self):
        super()
        self.name = "guardian"
        self.address = api["address"]
        self.API_KEY = api["API_KEY"]

    def api_search(self,search,from_date=None,to_date=None,news_delay=None):
        """
            API-specific search function

            returns raw text for this source
        """

        if news_delay is None:
            # reset to default
            news_delay = 3

        params = {
            "api-key":self.API_KEY,
            "q":search,
            "from-date":from_date,
            "to-date":to_date,
            "show-fields":"bodyText",
            "tags":"business"
        }

        try:
            r = requests.get(self.address,params=params)
            results = r.json()

            articles = results["response"]["results"]

            return self.process_result(articles)

        except:
            return ""

    def process_result(self,results):
        """
            Takes the results from the API and processes them to a single string
        """
        try:
            if len(results) < 1:
                return ""

            all_text = ""

            for article in results:
                all_text = "".join([article["fields"]["bodyText"],all_text])

            return all_text

        except:
            return ""