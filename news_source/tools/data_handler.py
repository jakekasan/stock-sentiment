from sources.guardian import Guardian

import datetime as dt
import pandas as pd


source_wranglers = {
    "guardian":Guardian
}

class Data_Handler:
    def __init__(self,df=None,sources=["guardian"],debug=False,datecol="Date"):
        self.df = df
        self.sources = [source_wranglers[x]() for x in sources]
        self.debug = debug
        self.datecol = datecol

    def run(self,df=None,name=None):
        if name is None:
            return

        if self.debug:
            print("Started processing data for {}".format(df["name"][0]))

        if self.debug:
            print("Df size:",df.shape)

        df["date"] = df["Date"].apply(lambda x: dt.datetime.strptime(x,"%Y-%M-%d"))
        
        df = df.apply(lambda x: self.process_row(x) ,axis=1)

        if self.debug:
            print("Finished processing data")

        return df

    def process_row(self,row):
        """
            Takes a row, applies search for each source, and returns row
        """
        for source in self.sources:
            col_name = "raw_text_{}".format(source.name)

            if col_name in row.index and row[col_name] != "":
                continue
        
            row[col_name] = source.search(row["name"],date=row["date"])

        if self.debug:
            print("Finished {}".format(row["date"]))

        return row

    def process_date(self,df):
        df["date"] = df[self.datecol].apply(lambda x: dt.datetime.strptime(x,"%Y-%M-%d"))
        pass

        

        
    


        

    