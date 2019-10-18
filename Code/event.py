import command
import requests

 
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
            self.handleevent(event['user'], event['text'], event['channel'])
        if event and 'files' in event and event['user']!="UP6FMPQ1X" and event['upload']==True:
            print(event['files'][0]['filetype'])   
            print(event['files'][0]['url_private'])
            response = requests.get(event['files'][0]['url_private'], headers={'Authorization': 'Bearer xoxb-795814705207-788531806065-9dWeyIRqj2t1LSbICYnDkB01'})
            print(response.content)
            with open("my.xlsx",'wb') as f: 
                f.write(response.content) 
            self.handleevent(event['user'], event['text'], event['channel'])    
     
    def handleevent(self, user, command, channel):
        if command and channel:
            print ("Received command: " + command + " in channel: " + channel + " from user: " + user)
            response = self.command.handlecommand(user, command)
            self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
