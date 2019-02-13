from flask import Flask, request
from pymessenger.bot import Bot
from dotenv import load_dotenv
import os
import random
import json
from Tracker import LaPosteTracker

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')

app = Flask(__name__)
bot = Bot(ACCESS_TOKEN)
tracker = LaPosteTracker(os.getenv('API_KEY'))


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        m = x['message']['text']
                        message = json.loads(tracker.track(m))
                        status = "COLIS #"+message['code'] + " " + \
                            message['status'] + "\nDate: "+message['date']
                        bot.send_text_message(recipient_id, status)
                        bot.send_button_message(recipient_id, message['message'], [{
                            "type": "web_url",
                            "url": message['link'],
                            "title": "Suvie Colis"
                        }])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run()
