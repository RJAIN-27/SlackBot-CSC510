import kwx

class Command(object):
 
    def handlecommand(self, user, command):
        if "know" in command:
            list=kwx.keywordExtraction(command)
            #list = command.split(' ')
            return list
