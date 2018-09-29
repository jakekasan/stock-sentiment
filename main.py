#!/usr/local/bin/python3

from news_source.tools.data_handler import Data_Handler
from data.data_importer import Data_Importer

import subprocess

def main():
    di = Data_Importer()
    result = di.search("RBS")
    print(result)
    return

if __name__ == '__main__':
    main()