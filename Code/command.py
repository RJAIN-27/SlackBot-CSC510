import KeywordExtraction
import modelSelection
import analysis
import mocking_infrastructure
import json
import unittest
import test
from mock import Mock
import collections
import openpyxl as xl
import keywordex


with open("data.json") as json_file:
    jsonData = json.load(json_file)

path = "my.csv"
flag=0

# KeywordExtraction.keywordExtraction = Mock(side_effect=mocking_infrastructure.mock_keyword_extraction)
# modelSelection.modelSelInteraction = Mock(side_effect=mocking_infrastructure.mockbestModel)
# analysis.analysisInteraction = Mock(side_effect = mocking_infrastructure.mock_analysis_interaction)


class Command(object):
   
    def handlecommand(self, user, command):
        if "know" in command:
            list=KeywordExtraction.keywordExtraction(command)
            #list=mocking_infrastructure.mock_keyword_extraction(command)
            print (list) 
            return list
        elif any(word in command for word in jsonData["model_sel_words"]):
            return "Please give the csv file that you want to analyze or want a suggestion about"
        elif "Pssst" in command:
            return "error"    
        elif "no" in command:
            return "Sorry about that :("
        elif "yes" in command:
            return "Thankyou for the feedback"
        elif flag==2:
            model_Selection=modelSelection.modelSelInteraction(path, command)
            print "jkkjkjkjkjkjkjk"
            print type(model_Selection)
            #model_Selection=mocking_infrastructure.mockbestModel(path,command)
            return model_Selection
        elif flag==1:
            analysis_file=analysis.analysisInteraction(path, command)
            #analysis_file=mocking_infrastructure.mock_analysis_interaction(path,command)
            return analysis_file
        elif flag==0:
             return "Sorry I did not get you"
        
    def handlecommands(self, user, command):
        global flag
        if any(word in command for word in jsonData["model_sel_words"]):
            flag=2
            response="Please provide the target column"
            return response

        if any(word in command for word in jsonData["analysis_words"]):
            flag=1
            response="Please provide the target column"
            return response
        
        else:
            return "Please give the file again with instructions on what to perform like suggesting model or analyzing the Data"

    def handlecommande(self, user, command, listx):
        ans=[]
        if "know" in command:
            listi=keywordex.keywordExtraction(command)
            d=collections.defaultdict(list)
            wb = xl.load_workbook(jsonData["xlsx_file"])
            sheet1= wb['Sheet2']
            for row in range(2, sheet1.max_row + 1):
                d[sheet1.cell(row, 1).value].append((sheet1.cell(row, 2).value))

            for i in listi:
                for j in listx:
                    m=d[j]
                    for k in i:
                        if k in m:
                            ans.append(i)
            return ans
        elif "no" in command:
            return "Please continue with either of the functionalities like knowing more about libraries, data analysis or suggestion"
             
        
