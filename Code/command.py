import KeywordExtraction
import modelSelection
import analysis
import mocking_infrastructure
import json
import unittest
import test
from mock import Mock


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
        elif "Pssst" in command:
            return "error"    
        elif "no" in command:
            return "Sorry about that :("
        elif "yes" in command:
            return "Thankyou for the feedback"
        elif flag==2:
            model_Selection=modelSelection.modelSelInteraction(path, command)
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
