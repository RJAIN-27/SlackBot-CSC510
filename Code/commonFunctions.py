import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

with open("data.json") as json_file:
    data = json.load(json_file)

def ngram(data, target):
    cols = list(data.columns)
    newcols = []
    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2),
                            stop_words='english')
    for col in cols:
        if not(data[col].dtypes=='float64' or data[col].dtypes=='int64'):
            newCol = col+"ConvertedFeatures" if col!=target else col
            newcols.append(newCol)
            data[newCol] = tfidf.fit_transform(data['col']).toarray()
    data = data.reindex(columns=newcols)
    return data



def targetCheck(target, columnNames):
    return 1 if target in columnNames else data["wrongTargetColumnException"]

def checkAndConvertIfCategorical(df,target):
    cols = list(df.columns)
    newcols = []
    flag = 0
    for col in cols:
        if not(df[col].dtypes=='float64' or df[col].dtypes=='int64'):
            flag = 1
            newCol = col+"id" if col!=target else col
            df[newCol]=df[col].factorize()[0]
            newcols.append(newCol)
        else:
            newcols.append(col)
    df = df.reindex(columns = newcols)
    return df,flag

def preprocessS1(path,target):
    data = pd.read_csv(path, sep=',', header=0)
    data = data[[col for col in data if data[col].nunique() > 1]]
    column_names = list(data.columns)
    flag = targetCheck(target, column_names)
    if flag != 1:
        return flag,[],0
    data,cat_flag = checkAndConvertIfCategorical(data, target)
    return data,column_names,cat_flag
