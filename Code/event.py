
import command
import requests
import io

 
class Event:
    def __init__(self, bot):
        self.bot = bot
        self.command = command.Command()
     
    def waitforevent(self):
        events = self.bot.slack_client.rtm_read()
        if events and len(events) > 0:
            for event in events:
                self.parseevent(event)
                 
    def parseevent(self, event):
        if event and 'text' in event and 'files' not in event and event['user']!="UP6FMPQ1X":   
            print("******")
            print(event)
            print("*****")
            self.handleevent(event['user'], event['text'], event['channel'])
        if event and 'files' in event and 'text' in event and event['user']!="UP6FMPQ1X" and event['upload']==True:
            print(event['files'][0]['filetype'])   
            print(event['files'][0]['url_private'])
            response = requests.get(event['files'][0]['url_private'], headers={'Authorization': 'Bearer xoxb-795814705207-788531806065-9dWeyIRqj2t1LSbICYnDkB01'})
            with open("my.csv",'wb') as f: 
                f.write(response.content) 
            f.close()    
            #f1=open("analysis_19_10_2019_14_07_54.txt", "r")
            #content=f1.read()
            #print(content)
            #print(type(content))
            #self.bot.slack_client.api_call("files.upload", channels=event['channel'], file=content)
           
            self.handleevent1(event['user'], event['text'], event['channel'])    
     
    def handleevent(self, user, command, channel):
        
        if command and channel:
            print ("Received command: " + command + " in channel: " + channel + " from user: " + user)
            response = self.command.handlecommand(user, command)
            print(response)
  
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="The information you asked is:\n", as_user=True)

            if type(response) is str:
                
                if(".txt" in response):
                    f1=open(response, "r")
                    content=f1.read()
                    print(content)
                    print(type(content))
                    self.bot.slack_client.api_call("files.upload", channels=channel, file=content)
                else:    
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

            if type(response) is list:
                for i in response:
                    for j in i:
                        self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=i[j], as_user=True)


        #    f1=open(response, "r")
        #    content=f1.read()
        #    print(content)
        #    print(type(content))
        #    self.bot.slack_client.api_call("files.upload", channels=channel, file=content)
            
        #   You have to use this    
        #    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
       
        # You have to use this
        #    for i in response:
        #        for j in i:
        #            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=i[j], as_user=True)

    def handleevent1(self, user, command, channel):
         if command and channel:
            print ("Received command: " + command + " in channel: " + channel + " from user: " + user)
            response = self.command.handlecommands(user, command)   
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
            


