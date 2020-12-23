import requests
import os
import random
from entity import Entity
from flask import jsonify
import responsepayload

class HandleMessage:
    tokenClientSide = os.environ.get("CLIENT_TOKEN_FB_WIT_AI")
    url = "https://api.wit.ai/message?v=20181107&q="
    headers = { "Authorization": 'Bearer ' + str(tokenClientSide) }
    entities = {}
    respayloads = responsepayload.ResponsePayload()


    def __init__(self):
        pass

    def firstEntity(self, nlp, intent):
        return nlp and nlp.entities and nlp.entities['intent'] and nlp.entities['intent'][0]
    
    def handle(self, data):
        message = str(data)
        
        if "message" in message:
           
            if "quick_reply" in message:
                payload = data['message']['quick_reply']['payload']
                
                if "REGIAO" in str(payload):
                    self.gravar_form(payload, "REGIAO")
                    return self.msg_tipolocacao()

                if "QTDQUARTO" in str(payload):
                    self.gravar_form(payload, "QTDQUARTO")
                    return self.msg_banheiros()

                if "QTDBANHEIRO" in str(payload):
                    self.gravar_form(payload, "QTDBANHEIRO")
                    return self.msg_vagas_garagem()

                if "QTDVAGA" in str(payload):
                    self.gravar_form(payload, "QTDVAGA")
                    return self.msg_range_preco_aluguel()
                
                if "RANGEALUGUEL" in str(payload):
                    self.gravar_form(payload, "RANGEALUGUEL")
                    return 

            elif ("👍🏾" or "👉🏾") in message:
                return data['message']['text']

            else:
                message = data['message']['text']
                resp = requests.get(self.url + message, headers=self.headers)

                witAi = Entity(resp.json())
                
                entityOne = self.firstEntity(witAi, "saudacao")
                print("Entidade 1:" + str(entityOne))

                if entityOne and entityOne['value'] == "saudacao" and entityOne['confidence'] > 0.4:
                    return self.msg_saudacao()    

                if (entityOne and entityOne['value'] == "alugar" and entityOne['confidence'] > 0.4):
                    self.delete_form()
                    return self.msg_quero_alugar() 

        elif "postback" in message:
            payload = data['postback']['payload']

            if "TIPOLOCACAO" in str(payload):
                    self.gravar_form(payload, "TIPOLOCACAO")
                    return self.msg_quartos()
    
        return self.msg_erro()
    
    def gravar_form(self, payload, prop): #dadosgeral
        payload = payload.split(".")[1]
        file = open("./dados/dadoscrawler.json", "a")
        file.write("'{}': '{}'\n".format(prop, payload))
        file.close()

    def delete_form(self):
        if os.path.isfile("./dados/dadoscrawler.json"):
            os.remove("./dados/dadoscrawler.json")
            print('File REMOVED!')

    def read_file(self, nameFile):
        file = open('./txtconversa/{}.txt'.format(nameFile), "r")
        frases = file.readlines()
        file.close()
        nr = random.randrange(len(frases))
        return frases[nr]
    
    def msg_erro(self):
        return self.read_file("erro")

    def msg_saudacao(self):
        msg = self.read_file("saudacao")
        return msg

    def msg_quero_alugar(self):
        msg = self.read_file("alugar")
        return self.model_quick_replies(msg, self.respayloads.payloadRegiao)
    
    def msg_tipolocacao(self):
        msg = self.read_file("tipolocacao")
        return self.model_carousel(msg, self.respayloads.payloadTipoLocacao)

    def msg_quartos(self):
        msg = self.read_file("quarto")
        return self.model_quick_replies(msg, self.respayloads.payloadQTDQUARTO)

    def msg_banheiros(self):
        msg = self.read_file("banheiro")
        return self.model_quick_replies(msg, self.respayloads.payloadQTDBANHEIRO)

    def msg_vagas_garagem(self):
        msg = self.read_file("vaga")
        return self.model_quick_replies(msg, self.respayloads.payloadQTDVAGA)

    def msg_range_preco_aluguel(self):
        msg = self.read_file("range_preco_aluguel")
        return self.model_quick_replies(msg, self.respayloads.payloadRangePrecoAluguel)

    def model_quick_replies(self, msg, payload):
        mount = {
            "text": msg,
            "quick_replies": payload
        }
        return mount

    def model_carousel(self, msg, payload):
        mount = {
            "attachment":{
                "type":"template",
                "payload": payload
            }
        }
        return mount

    def model_postback_buttons(self, msg, buttons):
        mount = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Mova para direita para ver mais opções",
                            "buttons": buttons[0]
                        },
                        {
                            "title": "Mova para esquerda para ver mais opções",
                            "buttons": buttons[1]
                        }
                    ]
                }
            }
        }
        return mount
 