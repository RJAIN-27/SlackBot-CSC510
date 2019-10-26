import json

with open("data.json") as json_file:
    data = json.load(json_file)

def targetCheck(target, columnNames):
    return 1 if target in columnNames else data["wrongTargetColumnException"]

def checkAndConvertIfCategorical(df,target):
    '''
    convert categorical to numerical
    '''
    return df
