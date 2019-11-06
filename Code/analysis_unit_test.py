import operator
import unittest
import json
import analysis
import commonFunctions as cf
import pandas as pd

with open("data.json") as json_file:
    data = json.load(json_file)
libraries = data["libraries"]
columnNames = data["columnNames"]
wrngColEx = data["wrongTargetColumnException"]

parameter_count_categorical = 5
parameter_count_numerical = 4

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
    # Use case 2 happy flow 
    def test_analysis_categorical(self):
            analysis.analysisInteraction("Datasets/Crime1.csv","Category")
            count_cat = contentCheck_categorical()
            self.assertEquals(count_cat,parameter_count_categorical)
            
    def test_analysis_numerical(self):
            analysis.analysisInteraction("Datasets/Wine.csv","Class")
            count_cat = contentCheck_numerical()
            self.assertEquals(count_cat,parameter_count_numerical)
            
    # usecase 2 - alternate flow
    def test_analysis_target_cat(self):
           self.assertEqual(analysis.analysisInteraction("Datasets/Crime1.csv", "Hululu"), wrngColEx)
    
    def test_analysis_target_num(self):
           self.assertEqual(analysis.analysisInteraction("Datasets/Wine.csv", "Hululu"), wrngColEx) 
            
    def test_analysis_result_cat(self):
        self.assertIsNotNone(analysis.analysisInteraction("Datasets/Crime1.csv","Category"))
        
    def test_analysis_result_num(self):
        self.assertIsNotNone(analysis.analysisInteraction("Datasets/Wine.csv","Class"))
        
    def test_fileCreation(self):
        self.assertIsNotNone(open("Analysis.txt","r"))
        
if __name__ == '__main__':
    unittest.main()
        
