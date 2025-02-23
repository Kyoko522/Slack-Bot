import os
from slack_sdk import WebClient
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

#config flask
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)


#The client is the connection to the slack API and the channels under it 
client = WebClient(token=os.environ['SLACK_TOKEN'])
client.chat_postMessage(channel='#test', text='Hello World!')

if __name__ == '__main__':
    app.run(debug=True)