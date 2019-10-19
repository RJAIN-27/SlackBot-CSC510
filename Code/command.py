import kwx
import modelSelection
import analysis

path = "my.csv"
flag=0

class Command(object):
 
    def handlecommand(self, user, command):
        if "know" in command:
            list=kwx.keywordExtraction(command)
            #list = command.split(' ')
            return list

        elif flag==1:
            analyses_file=analysis.analysis(path, command)
            return analyses_file
        else:
            model_Selection=modelSelection.modelSelection(path, command)   
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
