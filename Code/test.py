import unittest
import json
import modelSelection
import commonFunctions as cf
import pandas as pd
import analysis
import KeywordExtraction as ke
from command import Command


with open("/home/CSC510-23/Code/data.json") as json_file:
    data = json.load(json_file)

libraries = data["libraries"]
columnNames = data["columnNames"]
modelDict = data["listModels"]
wrngColEx = data["wrongTargetColumnException"]
parameters_to_be_counted = int(data["parameters_to_be_counted"])
target = data["target"]
wrong_target = data["wrong_target"]

parameter_count_categorical = 5
parameter_count_numerical = 4

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

def contentCheck_categorical():
    filename = "Analysis.txt"
    a = ""
    count = 0
    for line in open(filename, 'r'):
        a = a + line
    if "VALUE COUNTS" in a:
        count = count + 1
    if "DATA INFORMATION" in a:
        count = count + 1
    if "MEAN, MEDIAN AND MODE:" in a:
        count = count + 1
    if "Correlation" in a:
        count = count + 1
    if "Normality Tests" in a:
        count = count + 1
    return count 

def contentCheck_numerical():
    filename = "Analysis.txt"
    a = ""
    count = 0
    for line in open(filename, 'r'):
        a = a + line
    if "DATA INFORMATION" in a:
        count = count + 1
    if "MEAN, MEDIAN AND MODE:" in a:
        count = count + 1
    if "Correlation" in a:
        count = count + 1
    if "Normality Tests" in a:
        count = count + 1
    return count 
    
class TestStringMethods(unittest.TestCase):
    # usecase 1 - happy flow
    def test_modelsel(self):
        ls = best_models()
        bestMod = modelSelection.modelSelInteraction("/home/CSC510-23/Code/Datasets/Wine.csv", target)
        flag = 0
        for model in ls:
            if model not in bestMod:
                flag = 1
                break
        self.assertEquals(flag,0) and self.assertEquals(len(ls),len(bestMod))

    # usecase 1 - alternate flow
    def test_modelsel2(self):
       self.assertEqual(modelSelection.modelSelInteraction("/home/CSC510-23/Code/Datasets/Wine.csv", wrong_target), wrngColEx)

    def test_modelsel3(self):
        self.assertIsNotNone(modelSelection.modelSelInteraction("/home/CSC510-23/Code/Datasets/Crime1.csv","Category"))

    def test_categorical(self):
        data = pd.read_csv("/home/CSC510-23/Code/Datasets/Crime1.csv", sep=',', header=0)
        df,newcols,flag = cf.checkAndConvertIfCategorical(data,"Category")
        cflag=0
        for col in newcols:
            if not (df[col].dtypes == 'float64' or df[col].dtypes == 'int64'):
                cflag = 1
                break
        self.assertEquals(flag,1) and self.assertEquals(cflag,0)

    def test_fileCreation(self):
        self.assertIsNotNone(open("modelSelectionProcess.txt","r"))


    # Use case 2 happy flow 
    def test_analysis_categorical(self):
            analysis.analysisInteraction("/home/CSC510-23/Code/Datasets/Crime1.csv","Category")
            count_cat = contentCheck_categorical()
            self.assertEquals(count_cat,parameter_count_categorical)
            
    def test_analysis_numerical(self):
            analysis.analysisInteraction("/home/CSC510-23/Code/Datasets/Wine.csv","Class")
            count_cat = contentCheck_numerical()
            self.assertEquals(count_cat,parameter_count_numerical)
            
    # usecase 2 - alternate flow
    def test_analysis_target_cat(self):
           self.assertEqual(analysis.analysisInteraction("/home/CSC510-23/Code/Datasets/Crime1.csv", "Hululu"), wrngColEx)
    
    def test_analysis_target_num(self):
           self.assertEqual(analysis.analysisInteraction("/home/CSC510-23/Code/Datasets/Wine.csv", "Hululu"), wrngColEx) 
            
    def test_analysis_result_cat(self):
        self.assertIsNotNone(analysis.analysisInteraction("/home/CSC510-23/Code/Datasets/Crime1.csv","Category"))
        
    def test_analysis_result_num(self):
        self.assertIsNotNone(analysis.analysisInteraction("/home/CSC510-23/Code/Datasets/Wine.csv","Class"))
        
    def test_fileCreation(self):
        self.assertIsNotNone(open("Analysis.txt","r"))

    # usecase 3 - happy flow
    def test_KELib1(self):
        self.assertIsNotNone(ke.keywordExtraction("I wanna know about numpy, scipy, keras and someLib","Sheet1"))

    def test_KEFun1(self):
        self.assertIsNotNone(ke.keywordExtraction("I wanna know about sin, cos, and tan","Sheet3"))
        
    def test_usecase11(self):
        c=Command()
        ans = c.handlecommands("UP5FE7HSM", "suggest best model")
        actualanswer = "Please provide the target column"
        self.assertEquals(ans,actualanswer)

    #when the user does not give the file
    def test_usecase12(self):
        c=Command()
        ans = c.handlecommand("UP5FE7HSM", "suggest best model")
        actualanswer = "Please upload the dataset along with your query"
        self.assertEquals(ans,actualanswer)

    def test_usecase31(self):
        c=Command()
        ans = c.handlecommand("UP5FE7HSM", "i want to know numpy")
        actualanswer = [{u'numpy': u'NumPy is a very popular python library for large multi-dimensional array and matrix processing, with the help of a large collection of high-level mathematical functions. It is very useful for fundamental scientific computations in Machine Learning. It is particularly useful for linear algebra, Fourier transform, and random number capabilities. High-end libraries like TensorFlow uses NumPy internally for manipulation of Tensors. https://numpy.org/ https://docs.scipy.org/doc/numpy/reference/ http://cs231n.github.io/python-numpy-tutorial/'}, 'onlylibrary']
        self.assertEquals(ans,actualanswer) 

    def test_usecase32(self):
        c=Command()
        ans = c.handlecommand("UP5FE7HSM", "i want to know sin and cos from numpy")
        actualanswer = [{u'cos': u'The cos function is provided by numpy library in Python:\nnumpy.cos(x[, out]) = ufunc \u2018cos\u2019) : This mathematical function helps user to calculate trignmetric cosine for all x(being the array elements).'}, {u'sin': u'The sin function is provided by numpy library in Python:\nnumpy.sin(x[, out]) = ufunc \u2018sin\u2019) : This mathematical function helps user to calculate trignmetric sine for all x(being the array elements).'}, "onlyfunction"]
        self.assertEquals(ans,actualanswer) 

    def test_usecase33(self):
        c=Command()
        ans = c.handlecommand("UP5FE7HSM", "i want to know sin and cos")
        actualanswer = ['onlylibrary']
        self.assertEquals(ans,actualanswer)

    def test_usecase34(self):
        c=Command()
        ans = c.handlecommand("UP5FE7HSM", "i want to know further")
        actualanswer = ['onlylibrary']
        self.assertEquals(ans,actualanswer)

if __name__ == '__main__':
    unittest.main()
        
    
