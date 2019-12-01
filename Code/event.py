
import command
import requests
import io
import os
#import mocking_infrastructure
#from mock import Mock
import bot
import json


with open("/home/CSC510-23/Code/data.json") as json_file:
    data = json.load(json_file)

TOKEN = data["SLACK_BOT_TOKEN"]
#BOT_ID= os.environ.get('BOT_ID')
BOT_ID= data["BOT_ID"]

l_of_lib=[]

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
        #print event
        if event and 'text' in event and 'files' not in event and event['user']!=(BOT_ID) and event['user']!="USLACKBOT":   
            self.handleevent(event['user'], event['text'], event['channel'])
        elif event and 'files' in event and 'text' in event and event['user']!=(BOT_ID) and event['upload']==True:
            if event['text'] == '':
                self.bot.slack_client.api_call("chat.postMessage", channel=event['channel'], text="I am sorry can you please give me a csv file with the details of what is to be done\n", as_user=True)
            elif(event['files'][0]['filetype'] == "csv"):
                auth = 'Bearer '+str(TOKEN)
                response = requests.get(event['files'][0]['url_private'], headers={'Authorization': auth})
                #response = requests.get(event['files'][0]['url_private'], headers={'Authorization': 'Bearer xoxb-795814705207-788531806065-9dWeyIRqj2t1LSbICYnDkB01'})
                #response = requests.get(event['files'][0]['url_private'], headers={'Authorization': 'Bearer TOKEN'})
                #print response.content
                with open("my.csv",'wb') as f: 
                    f.write(response.content) 
                f.close()    
                self.handleevent1(event['user'], event['text'], event['channel']) 
            else:
                self.bot.slack_client.api_call("chat.postMessage", channel=event['channel'], text="I am sorry can you please give me a csv file\n", as_user=True)

    def rep(self, response, user, command, channel, flag):
        #print response
        if type(response) is str:   
                if(".txt" in response):
                    f1=open(response, "r")
                    content=f1.read()
                    f1.close()
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="The analysis of your dataset is:\n", as_user=True)
                    self.bot.slack_client.api_call("files.upload", channels=channel, file=content, filename="analysis.txt")
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="Were you satisfied with the analysis?", as_user=True)
                elif(response == "The target column is not present in the file. Please upload the file again and give the correct target column name. Remember, target column is case sensitive."):
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
                elif(response == "Sorry about that :("):
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
                elif(response == "Thankyou for the feedback"):
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
                elif (response == "error"):
                    print ("fine")   
                elif(response == "Sorry I did not get you"):
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
                elif(response == "Please continue with either of the functionalities like knowing more about libraries, data analysis or suggestion"):
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="Were you satisfied with the above provided information", as_user=True)
                elif(response == "Please upload the dataset along with your query"):
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
                else:  
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="The best model suggestion for your dataset is:\n", as_user=True)  
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="Were you satisfied with the recommendation?", as_user=True)

        elif type(response) is list and len(response)!=0:  
            if (type(response[0]) is str and response[0]=="onlylibrary" or response[0]=="onlyfunction" ):
                response.pop()
                #print response
                
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="I am sorry, coudn't fetch the information. My team is working on making me better everyday by adding new functions and libraries in my database!", as_user=True)
            elif (type(response[0]) is dict):
                if (response[-1]=="onlylibrary"):
                    response.pop()
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="The details of the libraries or functions you asked are:\n", as_user=True)
                if flag==0:
                    for i in response:
                        for j in i:
                            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=i[j], as_user=True)
                            l_of_lib.append(j)
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=" If you would like to have information about particular function in the above library, please enter the function name", as_user=True)   
               
                if flag==1:
                    for i in response:
                        for j in i:
                            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=i[j], as_user=True)
                            # l_of_lib.append(j)
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="Were you satisfied with the above provided information", as_user=True) 
                #self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="Were you satisfied with the details?", as_user=True)
            elif (type(response[0]) is str):
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="The best models that you can use are:\n", as_user=True)
                for i in response:
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=i, as_user=True)
                f1=open("modelSelectionProcess.txt", "r")
                content=f1.read()
                print(content)
                f1.close()
                self.bot.slack_client.api_call("files.upload", channels=channel, file=content, filename="modelSelectionProcess.txt")
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="Were you satisfied with the information?", as_user=True)

        elif type(response) is list and len(response)==0:
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="I am sorry, coudn't fetch the information. My team is working on making me better everyday by adding new functions and libraries in my database!", as_user=True)


    def handleevent(self, user, command, channel):
        global l_of_lib
        flag=0

        if command and channel:
            print ("Received command: " + command + " in channel: " + channel + " from user: " + user)

            if (len(l_of_lib)==0):
                response = self.command.handlecommand(user, command)
                if type(response) is list and response[-1]=="onlyfunction":
                    response.pop()
                    flag=1

                self.rep(response, user, command, channel, flag)
                
                
            elif (len(l_of_lib)!=0):
                flag=1
                response=self.command.handlecommande(user, command, l_of_lib)
                l_of_lib = []
                self.rep(response, user, command, channel, flag)

            
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
            


