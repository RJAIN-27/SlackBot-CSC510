# Python code to demonstrate working of unittest using mock
import operator
import unittest
import json
import modelSelection

with open("data.json") as json_file:
    data = json.load(json_file)
libraries = data["libraries"]
columnNames = data["columnNames"]
modelDict = data["listModels"]
wrngColEx = data["wrongTargetColumnException"]
parameters_to_be_counted = int(data["parameters_to_be_counted"])
target = data["target"]
wrong_target = data["wrong_target"]
path_to_csv_file_case1_case2 = data["path_to_csv_file_case1_case2"]
filename = data["path_for_usecase2"]

# USECASE 1
def mockbestModel(path, target):
    # for mocking the main and alternate flow
    flag = targetCheck(target, columnNames)
    if flag != 1:
        return flag
    sorted_x = sorted(modelDict.items(), key=operator.itemgetter(1))
    return (sorted_x[len(sorted_x) - 1][0])

def max_val_fun():
    ls = []
    for i in modelDict:
        ls.append(modelDict[i])
    return max(ls)

def best_models():
    ls = []
    accr = 0
    for models in modelDict:
        if accr<modelDict[models]:
            accr = modelDict[models]
    for model in modelDict:
        if accr == modelDict[model]:
            ls.append(model)
    return ls

# USECASE 1
def targetCheck(target, columnNames):
    return 1 if target in columnNames else wrngColEx

class TestStringMethods(unittest.TestCase):
    # usecase 1 - happy flow
    def test_modelsel(self):
        ls = best_models()
        for model in ls:
            self.assertEqual(modelDict[model],max_val_fun())

    # usecase 1 - alternate flow
    def test_modelsel2(self):
        self.assertEqual(modelSelection.modelSelInteraction(path_to_csv_file_case1_case2, wrong_target), wrngColEx)

if __name__ == '__main__':
    unittest.main()
