from news_source.sources.guardian import Guardian

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

        if df is None and self.df is None:
            return

        if name is None:
            return

        if self.debug:
            print("Started processing data for {}".format(df["name"][0]))

        if self.debug:
            print("Df size:",df.shape)

        if "Date" in df.columns and "date" not in df.columns:
            df["date"] = df["Date"].apply(lambda x: dt.datetime.strptime(x,"%Y-%M-%d"),axis=1)

        #df.apply(lambda x: print(x),axis=0)
        df = df.apply(lambda x: self.process_row(row=x,name=name),axis=1)

        if self.debug:
            print("Finished processing data")

        self.df = df

        self.save_data(name=name)

        return df


    def process_row(self,row=None,name=None):
        """
            Takes a row, applies search for each source, and returns row
        """
        if self.debug:
            print("Processing row")

        for source in self.sources:
            col_name = "raw_text_{}".format(source.name)

            if col_name in row.index and row[col_name] != "":
                continue
        
            row[col_name] = source.search(name,date=row["date"])

        if self.debug:
            print("Finished {}".format(row["date"]))

        
        return row

    def process_date(self,df):
        """

        """
        df["date"] = df[self.datecol].apply(lambda x: dt.datetime.strptime(x,"%Y-%M-%d"))
        pass

    def save_data(self,name=None):
        pathname = ""
        if name is None:
            pathname = "./current.csv"
        else:
            pathname = "./{}.csv".format(name)
        self.df.to_csv(pathname)
        return self.df
        
    def load_data(self,name=None):
        if name is None:
            return None
        try:
            self.df = pd.read_csv("./{}.csv".format(name))
            return self.df
        except:
            return None

    def get_df(self):
        if self.df is not None:
            return self.df
        return None

    def get_returns(self,df=None):
        if df is None:
            df = self.df

        df["returns"] = df["price"].pct_change()

        df["returns"] = df["returns"].fillna(0)

        print(df.head())

        self.df = df

        return self.df

    def make_label(self,df=None):
        if df is None:
            df = self.df

        def label_func(x):
            if x < -0.001:
                return -1
            if x > 0.001:
                return 1
            return 0

        df["label"] = df["returns"].apply(label_func)

        return        

    def nlp_get_hapaxes(self,df=None,number=1000):
        if df is None:
            df = self.df

    def nlp(self,df=None):
        if df is None:
            df = self.df

        
        
    


        

def process_row(row):
        """
            Takes a row, applies search for each source, and returns row
        """
        print("Processing row")
        return row

        for source in [source_wranglers[x]() for x in ["guardian"]]:
            col_name = "raw_text_{}".format(source.name)

            if col_name in row.index and row[col_name] != "":
                continue
        
            row[col_name] = source.search(row["name"],date=row["date"])

        
        print("Finished {}".format(row["date"]))

        return row