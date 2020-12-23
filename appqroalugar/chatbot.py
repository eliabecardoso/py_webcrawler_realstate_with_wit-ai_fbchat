from flask import Flask, request
import os 
import requests
import traceback
import json
from handleMessage import handleMessage

token = os.environ.get("FB_ACCESS_TOKEN")
app = Flask("appqroalugar") #__name__
urlbase = 'https://graph.facebook.com/v2.6/me/messages?access_token='
endpoint = '{}{}'.format(urlbase, token)
handleMsg = handleMsgessage()

def response(sender, data):
    if "attachment" in str(data):
        payload = { 'recipient': { 'id': sender }, 'message': data }
    elif "quick_replies" in str(data):
        payload = { 'recipient': { 'id': sender }, 'message': data }
    elif "sender_action" in str(data):
        payload = { 'recipient': { 'id': sender }, 'message': \
        {'text': 'Aguarde só alguns segundos que já estou buscando para você! 🔎🏡🏢' }  }
        requests.post(endpoint, json=payload)
        payload = { 'recipient': { 'id': sender }, 'sender_action': 'typing_on' }
    else:
        payload = { 'recipient': { 'id': sender }, 'message': {'text': data } }

    r = requests.post(endpoint, json=payload)


@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode())
            sender = data['entry'][0]['messaging'][0]['sender']['id']
            obj = data['entry'][0]['messaging'][0]

            if "RANGEALUGUEL" in str(obj):
                response(sender, "sender_action")   
            
            print(data)
            #tratamento e retorno
            if obj and not "delivery" in str(obj):
                msg = handleMsg.handle(obj)
                response(sender, msg)
                
        except Exception as e:
            print(traceback.format_exc())
            print("Data error: " + str(request.data.decode()))

    elif request.method == 'GET': #Para Validação Inicial
        if request.args.get('hub.verify_token') == os.environ.get('FB_VERIFY_TOKEN'):
            return str(request.args.get('hub.challenge'))
        return 'Wrong Verify Token'
    return 'Nothing'

if __name__ == '__main__':
    app.run(debug=True)