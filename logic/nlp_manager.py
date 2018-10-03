import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
import pandas as pd


class NLP_Manager:
    def __init__(self,df=None):
        self.df = df
        self.all_words = None
        
    def load_df(self,df=None,filename=None):
        if filename is None:
            self.df = df

    def get_all_words(self):
        def get_row_words(row=None,cols=None):
            data = ""
            for col in cols:
                data = data.join(row[col])
            return data
        
        cols = [x for x in self.df.columns if "raw_text" in x]

        for col in cols:
            self.df[col] = self.df[col].fillna("")

        results = self.df.apply(lambda x: get_row_words(row=x,cols=cols),axis=1)

        all_words = ""
        for x in list(results):
            all_words = all_words.join(x)
            all_words = all_words.join(" ")
        
        self.all_words = all_words

        return all_words

    def tokenize(self,string):
        string = string.lower()

        string = re.sub(r'(?u)[^\w\s]'," ", string)

        string = string.split()

        return string

    def get_freq_dist(self,arr):
        fdist = nltk.FreqDist(arr)
        return fdist

    def get_hapaxes(self,arr):
        pass


