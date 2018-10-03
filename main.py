#!/usr/local/bin/python3

from news_source.tools.data_handler import Data_Handler
from data.data_importer import Data_Importer
from data.data_importer import get_prices

import numpy as np

import subprocess

def main():
    di = Data_Importer(debug=True)
    result = di.load_data(name="RBS")
    dh = Data_Handler()
    results = dh.run(df=result,name="RBS")
    print(results)
    return

def loaded_main():
    dh = Data_Handler()
    dh.load_data(name="RBS")
    
    dh.get_returns()

    results = dh.get_df()

    #print(np.sum(results["raw_text_guardian"] == ""))
    print(np.sum(results["raw_text_guardian"].apply(lambda x: type(x) == str)))
    print(results.shape)

if __name__ == '__main__':
    #main()
    loaded_main()