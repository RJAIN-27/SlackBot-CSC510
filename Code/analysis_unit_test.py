import unittest
import json
import analysis

with open("/home/ubuntu/CSC510-23/Code/data.json") as json_file:
    data = json.load(json_file)
libraries = data["libraries"]
columnNames = data["columnNames"]
wrngColEx = data["wrongTargetColumnException"]

parameter_count_categorical = 5
parameter_count_numerical = 4

# Checks the lines in the file if the dataset given by user is categorical
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

# Checks the lines in the file if the dataset given by user is numerical
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
    
    

class TestyAnalysisMethods(unittest.TestCase):
    # Use case 2 happy flow - to check the contents of the file produced after performing the EDA
    def test_analysis_categorical(self):
            analysis.analysisInteraction("Datasets/Crime1.csv","Category")
            count_cat = contentCheck_categorical()
            self.assertEquals(count_cat,parameter_count_categorical)
            
    def test_analysis_numerical(self):
            analysis.analysisInteraction("Datasets/Wine.csv","Class")
            count_cat = contentCheck_numerical()
            self.assertEquals(count_cat,parameter_count_numerical)
            
    # usecase 2 - alternate flow - if the wrong target column is provided 
    def test_analysis_target_cat(self):
           self.assertEqual(analysis.analysisInteraction("Datasets/Crime1.csv", "Hululu"), wrngColEx)
    
    def test_analysis_target_num(self):
           self.assertEqual(analysis.analysisInteraction("Datasets/Wine.csv", "Hululu"), wrngColEx) 
    
    # Checks if the result of execution of the call to Use case 2 is not empty 
    def test_analysis_result_cat(self):
        self.assertIsNotNone(analysis.analysisInteraction("Datasets/Crime1.csv","Category"))
        
    def test_analysis_result_num(self):
        self.assertIsNotNone(analysis.analysisInteraction("Datasets/Wine.csv","Class"))
    
    # Checks if the file has been created after executing use case 2 
    def test_fileCreation(self):
        self.assertIsNotNone(open("Analysis.txt","r"))
        
if __name__ == '__main__':
    unittest.main()
        
