# Python code to demonstrate working of unittest using mock
import unittest
import json
import modelSelection
import commonFunctions as cf
import pandas as pd

with open("data.json") as json_file:
    data = json.load(json_file)
    
libraries = data["libraries"]
columnNames = data["columnNames"]
modelDict = data["listModels"]
wrngColEx = data["wrongTargetColumnException"]
parameters_to_be_counted = int(data["parameters_to_be_counted"])
target = data["target"]
wrong_target = data["wrong_target"]

# USECASE 1
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

class TestStringMethods(unittest.TestCase):
    # usecase 1 - happy flow
    def test_modelsel(self):
        ls = best_models()
        bestMod = modelSelection.modelSelInteraction("Datasets/Wine.csv", target)
        flag = 0
        for model in ls:
            if model not in bestMod:
                flag = 1
                break
        self.assertEquals(flag,0) and self.assertEquals(len(ls),len(bestMod))

    # usecase 1 - alternate flow
    def test_modelsel2(self):
       self.assertEqual(modelSelection.modelSelInteraction("Datasets/Wine.csv", wrong_target), wrngColEx)

    def test_modelsel3(self):
        self.assertIsNotNone(modelSelection.modelSelInteraction("Datasets/Crime1.csv","Category"))

    def test_categorical(self):
        data = pd.read_csv("Datasets/Crime1.csv", sep=',', header=0)
        df,newcols,flag = cf.checkAndConvertIfCategorical(data,"Category")
        cflag=0
        for col in newcols:
            if not (df[col].dtypes == 'float64' or df[col].dtypes == 'int64'):
                cflag = 1
                break
        self.assertEquals(flag,1) and self.assertEquals(cflag,0)

    def test_fileCreation(self):
        self.assertIsNotNone(open("modelSelectionProcess.txt","r"))

if __name__ == '__main__':
    unittest.main()
