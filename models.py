import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def get_test_train(x,y):
    return train_test_split(x,y,test_ratio=0.3)

def get_returns(df=None,p_col=None):
    df["returns"] = df[p_col].pct_change(periods=1)
    df["returns"].fillna(0,inplace=True)
    return df

def run_knn():
    pass