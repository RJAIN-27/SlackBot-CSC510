class Command(object):
 
    def handlecommand(self, user, command):
        response = "<@" + user + ">: "
        response += "Welcome Boss" 
        return response

        
         
    