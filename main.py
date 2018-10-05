#!/usr/local/bin/python3

from news_source.tools.data_handler import Data_Handler
from data.data_importer import Data_Importer
from data.data_importer import get_prices
from logic.nlp_manager import NLP_Manager

from config.news_sources import guardian
from news_source.sources.guardian import Guardian

import json
import numpy as np
import requests

import subprocess

def main():
    di = Data_Importer(debug=True)
    result = di.load_data(name="RBS")
    dh = Data_Handler()
    results = dh.run(df=result,name="RBS")
    print(results)
    return

def loaded_main():

    #custom_search("rbs")
    #test_print("business/business,uk/business")
    #return
    #print("\nNow the actual class\n")
    #custom_lookup("RBS OR (royal AND bank AND of AND scotland")
    #custom_lookup("rbs OR (royal AND bank AND of AND scotland) OR (brexit) OR (mark AND carney) OR economy")
    #custom_lookup("RBS")

    #return
    #get_sections()

    #return

    dh = Data_Handler()
    dh.load_data(name="RBS")
    
    dh.get_returns()

    dh.make_label()

    results = dh.get_df()

    nlp = NLP_Manager(df=results)

    df = nlp.run(df=results)

    print(df.head())
    return

    print(results.head())

    #print(np.sum(results["raw_text_guardian"] == ""))
    print(np.sum(results["raw_text_guardian"].apply(lambda x: type(x) == str)))
    print(results.shape)

def get_sections():
    params = {
        "q":"business",
        "api-key":guardian["API_KEY"]
    }

    url = "https://content.guardianapis.com/tags?q=business&api-key=test"

    base_url = "https://content.guardianapis.com/tags"
    r = requests.get(base_url,params=params)

    results = r.json()["response"]["results"]

    for thing in results:
        print(thing)

def custom_search(query):
    params = {
        "q":query,
        "api-key":guardian["API_KEY"],
        "tags":"business/business"
    }
    base_url = "https://content.guardianapis.com/search"
    #"https://content.guardianapis.com/search"
    #params = json.dumps(params)
    r = requests.get(base_url,params=params)
    print(r.url)
    for thing in r.json()["response"]["results"]:
        print(thing)

def custom_lookup(query):
    g = Guardian(debug=True)
    results = g.search(search=query,just_results=True,news_delay=3)
    
    for item in results:
        print(item["webTitle"])

def test_print(string):
    j = {
        "string":string
    }
    print(json.dumps(string))
    #print(json.loads(j))

if __name__ == '__main__':
    #main()
    loaded_main()