import KeywordExtraction
import modelSelection
import analysis

path = "my.csv"
flag=0

class Command(object):
 
    def handlecommand(self, user, command):
        if "know" in command:
            list=KeywordExtraction.keywordExtraction(command)
            print (list)
            #list = command.split(' ') 
            return list
        elif "Pssst" in command:
            return "error"    
        elif "no" in command:
            return "Sorry about that :("
        elif "yes" in command:
            return "Thankyou for the feedback"
        elif flag==1:
            #analyses_file=analysis.analysis(path, command) #analysis.analysisInteraction()
            analyses_file=analysis.analysisInteraction(path, command)
            return analyses_file
        elif flag==0:
            #model_Selection=modelSelection.modelSelection(path, command) #modelSelInteraction()
            model_Selection=modelSelection.modelSelInteraction(path, command)
            return model_Selection

    def handlecommands(self, user, command):
        global flag
        if "suggestion" in command or "selection" in command:
            flag=0
            response="Please provide the target column"
            #list=modelSelection.modelSelection(file, target)
            return response

        if "analyze" in command or "analyze" in command:
            response="Please provide the target"
            flag=1
            return response
