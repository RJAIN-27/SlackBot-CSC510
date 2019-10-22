import KeywordExtraction
import modelSelection
import analysis
import mocking_infrastructure

path = "my.csv"
flag=0

class Command(object):
 
    def handlecommand(self, user, command):
        if "know" in command:
            #list=KeywordExtraction.keywordExtraction(command)
            list=mocking_infrastructure.mock_keyword_extraction(command)
            print (list) 
            return list
        elif "Pssst" in command:
            return "error"    
        elif "no" in command:
            return "Sorry about that :("
        elif "yes" in command:
            return "Thankyou for the feedback"
        elif flag==1:
            #analysis_file=analysis.analysisInteraction(path, command)
            analysis_file=mocking_infrastructure.mock_analysis_interaction(path,command)
            return analysis_file
        elif flag==0:
            #model_Selection=modelSelection.modelSelInteraction(path, command)
            model_Selection=mocking_infrastructure.mockbestModel(path,command)
            return model_Selection

    def handlecommands(self, user, command):
        global flag
        if "suggestion" in command or "selection" in command:
            flag=0
            response="Please provide the target column"
            return response

        if "analyze" in command or "analyze" in command:
            response="Please provide the target"
            flag=1
            return response
