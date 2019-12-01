import unittest
import json
import modelSelection
import commonFunctions as cf
import pandas as pd
import analysis
import KeywordExtraction as ke
from command import Command


with open("data.json") as json_file:
    data = json.load(json_file)

libraries = data["libraries"]
columnNames = data["columnNames"]
modelDict = data["listModels"]
wrngColEx = data["wrongTargetColumnException"]
parameters_to_be_counted = int(data["parameters_to_be_counted"])
target = data["target"]
wrong_target = data["wrong_target"]


    
class TestStringMethods(unittest.TestCase):
    #when the user gives file with text
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
        
    
