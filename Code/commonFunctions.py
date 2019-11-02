import json
import pandas as pd

with open("data.json") as json_file:
    data = json.load(json_file)

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
        return flag,[]
    data,cat_flag = checkAndConvertIfCategorical(data, target)
    return data,column_names,cat_flag
