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
            return
        self.df = pd.read_csv(filename)

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

        results = results.values

        #print("Results:")
        #print(results)

        all_words = ""

        for x in list(results):
            all_words = all_words + " " + x
        
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

    def get_lemms(self,arr):
        lemmer = WordNetLemmatizer()

        arr = list(map(lemmer.lemmatize,arr))

        return arr

    def run(self,df=None):
        self.load_df(df=df)

        all_words = self.get_all_words()

        tokens = self.tokenize(all_words)

        lemms = self.get_lemms(tokens)

        fdist = self.get_freq_dist(lemms)

        print(len(fdist))

        fdist_list = list(fdist)

        temp = pd.DataFrame({"words":fdist_list})

        temp.to_csv("./words.csv")

        to_take = 2000

        self.vocabulary = list(fdist)[to_take:]

        for i in range(to_take):
            self.df["x_{}".format(i)] = self.df["raw_text_guardian"].apply(lambda x: 1 if self.vocabulary[i] in x else 0)

        self.df.to_csv("./processed.csv")

        for col in self.df.columns:
            if "x_" in col:
                print(df[col].unique())

        return self.df

        


        


