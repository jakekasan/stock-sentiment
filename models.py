import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from nlptools.main import most_common_words

def get_test_train(x,y):
    return train_test_split(x,y,test_ratio=0.3)

def get_returns(df=None,p_col=None):
    r = df[p_col].pct_change(periods=1)
    r.fillna(0,inplace=True)
    return r

def run_knn(data):
    """
        runns a knn model on given data
    """

    x = most_common_words(target=data["text"])

    y = get_returns
    
    pass