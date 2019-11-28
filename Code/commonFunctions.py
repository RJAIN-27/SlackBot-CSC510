import json

with open("/home/ubuntu/CSC510-23/Code/data.json") as json_file:
    data = json.load(json_file)

def bestModel(modelDict,f):
    if len(modelDict)==0:
        f.writelines("\n      No model to satisfy this dataset")
        return ["No model to satisfy this dataset"]
    accr = 70
    models = []
    for model in modelDict:
        if accr<=modelDict[model]:
            accr = modelDict[model]
    for model in modelDict:
        if accr == modelDict[model]:
            models.append(model)

    return models if len(models)>0 else ["No decent model to satisfy this dataset"]

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
    return df,newcols,flag

def preprocessS1(data,target):
    data = data[[col for col in data if data[col].nunique() > 1]]
    column_names = list(data.columns)
    flag = targetCheck(target, column_names)
    if flag != 1:
        return flag,[],0
    data,column_names,cat_flag = checkAndConvertIfCategorical(data, target)
    return data,column_names,cat_flag
