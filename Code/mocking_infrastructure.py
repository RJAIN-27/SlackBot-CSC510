import json
import operator
import openpyxl as xl

with open("data.json") as json_file:
    data = json.load(json_file)
columnNames = data["columnNames"]
modelDict = data["listModels"]
wrngColEx = data["wrongTargetColumnException"]
parameters_count=int(data["parameters_to_be_counted"])
target=data["target"]
wrong_target=data["wrong_target"]
path=data["path_to_csv_file_case1_case2"]
libraries = data["libraries"]

# USECASE 1
def mockbestModel(path,target):
    # for mocking the main and alternate flow
    flag = targetCheck(target,columnNames)
    if flag !=1:
        return flag
    sorted_x = sorted(modelDict.items(), key=operator.itemgetter(1))
    return(sorted_x[len(sorted_x)-1][0])

def max_val_fun():
    ls = []
    for i in modelDict:
        ls.append(modelDict[i])
    return max(ls)

def targetCheck(target, columnNames):
    return 1 if target in columnNames else "The target column is not present in the file. Please upload the file again and give the correct target column name. Remember, target column is case sensitive."

# USECASE 2
def mock_analysis_interaction(path, target):
    flag = targetCheck(target,columnNames)
    if flag !=1:
        return flag
    filename=data["path_for_usecase2"]
    a=""
    count=0
    for line in open(filename, 'r'):
        a=a+line
    if "MEAN" in a:
        count=count+1
    if "MEDIAN" in a:
        count=count+1
    if "MODE" in a:
        count=count+1
    if "Correlation" in a:
        count=count+1
    if "Normality Tests" in a:
        count=count+1
    if count == parameters_count:
        return filename
    return 0

# USECASE 3
def mock_keyword_extraction(a):
    list = a.split(' ')
    ans_list = []
    length = len(list)
    i = 0
    wb = xl.load_workbook('libraryFile.xlsx')
    sheet = wb['Sheet1']
    libInfo = {}
    for row in range(2, sheet.max_row + 1):
        libInfo[sheet.cell(row, 1).value] = sheet.cell(row, 2).value
    while i < length:
        for r in (libInfo):
            if list[i].lower() in r:
                ans_list.append({r: libraries[r]})
        i = i + 1
    return ans_list


def read_from_json_and_test(a):
    list = a.split(' ')
    i = 0
    ans_list = []

    length = len(list)
    while i < length:
        for r in (libraries):
            if list[i].lower() in r:
                ans_list.append({r: libraries[r]})
        i = i + 1
    return ans_list
