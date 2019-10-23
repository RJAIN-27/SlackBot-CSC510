import time
import event
import command
from slackclient import SlackClient
import os

global BOT_ID

class Bot(object):
    def __init__(self):
        #self.slack_client = SlackClient("xoxb-795814705207-788531806065-9dWeyIRqj2t1LSbICYnDkB01")
        self.slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        self.botname = "libbot"
        self.botid = self.getbotid()
        if self.botid is None:
            exit("Error, could not find " + self.botname)
        self.event = event.Event(self)
        self.command=command.Command()

        self.listen()
     
    def getbotid(self):
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == self.botname:
                    BOT_ID=(user.get('id'))
                    return  user.get('id') 
            return None
             
    def listen(self):
        if self.slack_client.rtm_connect(with_team_state=False):
            print ("Successfully connected, listening for commands")
            while True:
                self.event.waitforevent()
                 
                time.sleep(1)
        else:
            exit("Error, Connection Failed")
