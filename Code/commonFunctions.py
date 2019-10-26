import json
import pandas as pd

with open("data.json") as json_file:
    data = json.load(json_file)

def targetCheck(target, columnNames):
    return 1 if target in columnNames else data["wrongTargetColumnException"]

def checkAndConvertIfCategorical(df,target):
    '''
    convert categorical to numerical
    '''
    return df

def preprocessS1(path,target):
    data = pd.read_csv(path, sep=',', header=0)
    data = data[[col for col in data if data[col].nunique() > 1]]
    column_names = list(data.columns)
    flag = targetCheck(target, column_names)
    if flag != 1:
        return flag,[]
    data = checkAndConvertIfCategorical(data, target)
    return data,column_names
