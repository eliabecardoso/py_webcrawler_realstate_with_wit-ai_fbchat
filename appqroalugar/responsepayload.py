class ResponsePayload:
    payloadRegiao = [
         {
            "content_type":"text",
            "title":"Todos",
            "payload":"BTN_ESCOLHA_REGIAO.TODOS",
            "image_url":"https://st3.depositphotos.com/8639728/13913/v/1600/depositphotos_139134884-stock-illustration-compass-with-north-south-east.jpg"
        },
        {
            "content_type":"text",
            "title":"Centro",
            "payload":"BTN_ESCOLHA_REGIAO.CENTRO",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Letter_c.svg/1200px-Letter_c.svg.png"
        },
        {
            "content_type":"text",
            "title":"Norte",
            "payload":"BTN_ESCOLHA_REGIAO.NORTE",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/LetterN.svg/1200px-LetterN.svg.png"
        },
        {
            "content_type":"text",
            "title":"Sul",
            "payload":"BTN_ESCOLHA_REGIAO.SUL",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Letter_s.svg/1200px-Letter_s.svg.png"
        },
        {
            "content_type":"text",
            "title":"Leste",
            "payload":"BTN_ESCOLHA_REGIAO.LESTE",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/LetterL.svg/1200px-LetterL.svg.png"
        },
        {
            "content_type":"text",
            "title":"Oeste",
            "payload":"BTN_ESCOLHA_REGIAO.OESTE",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Letter_o.svg/1200px-Letter_o.svg.png"
        },
    ]

    payloadTipoLocacao = {
        "template_type":"generic",
        "elements":[
            {
                "title":"Buscar Casas",
                "image_url":"https://www.plantapronta.com.br/projetos/140/01.jpg",
                "subtitle":"Está procurando uma casa para alugar?",
                # "default_action": {
                #     "type": "web_url",
                #     "url": "https://www.amazon.com/Champion-Mens-Classic-Jersey-T-Shirt/dp/B01N6DJO7M",
                #     "messenger_extensions": False,
                #     "webview_height_ratio": "tall",
                #     "fallback_url": "https://www.amazon.com/"
                # },
                "buttons":[
                    {
                        "type":"postback",
                        "title":"Casas",
                        "payload":"BTN_ESCOLHA_TIPOLOCACAO.CASA",
                    }              
                ]         
            },
            {
                "title":"Buscar Apartamentos",
                "image_url":"https://www.galeriadaarquitetura.com.br/Img/projeto/702x415/4120/apartamento-sumare1430.jpg",
                "subtitle":"Está procurando um apartamento para alugar?",
                # "default_action": {
                #     "type": "web_url",
                #     "url": "https://www.amazon.com/Champion-Mens-Classic-Jersey-T-Shirt/dp/B01N6DJO7M",
                #     "messenger_extensions": False,
                #     "webview_height_ratio": "tall",
                #     "fallback_url": "https://www.amazon.com/"
                # },
                "buttons":[
                    {
                        "type":"postback",
                        "title":"Apartamentos",
                        "payload":"BTN_ESCOLHA_TIPOLOCACAO.APARTAMENTO",
                    }              
                ]         
            } 
        ]
    }

    payloadQTDQUARTO = [
        {
            "content_type":"text",
            "title":"1",
            "payload":"BTN_ESCOLHA_QTDQUARTO.1",
        },
        {
            "content_type":"text",
            "title":"2",
            "payload":"BTN_ESCOLHA_QTDQUARTO.2",
        },
        {
            "content_type":"text",
            "title":"3",
            "payload":"BTN_ESCOLHA_QTDQUARTO.3",
        },
        {
            "content_type":"text",
            "title":"4",
            "payload":"BTN_ESCOLHA_QTDQUARTO.4",
        },
    ]

    payloadQTDBANHEIRO = [
         {
            "content_type":"text",
            "title":"1",
            "payload":"BTN_ESCOLHA_QTDBANHEIRO.1",
        },
        {
            "content_type":"text",
            "title":"2",
            "payload":"BTN_ESCOLHA_QTDBANHEIRO.2",
        },
        {
            "content_type":"text",
            "title":"3",
            "payload":"BTN_ESCOLHA_QTDBANHEIRO.3",
        },
        {
            "content_type":"text",
            "title":"4",
            "payload":"BTN_ESCOLHA_QTDBANHEIRO.4",
        },
    ]

    payloadQTDVAGA = [
         {
            "content_type":"text",
            "title":"1",
            "payload":"BTN_ESCOLHA_QTDVAGA.1",
        },
        {
            "content_type":"text",
            "title":"2",
            "payload":"BTN_ESCOLHA_QTDVAGA.2",
        },
        {
            "content_type":"text",
            "title":"3",
            "payload":"BTN_ESCOLHA_QTDVAGA.3",
        },
        {
            "content_type":"text",
            "title":"4",
            "payload":"BTN_ESCOLHA_QTDVAGA.4",
        },
    ]

    payloadRangePrecoAluguel = [
         {
            "content_type":"text",
            "title":"R$50 ~ R$550",
            "payload":"BTN_ESCOLHA_RANGEALUGUEL.50-550",
        },
        {
            "content_type":"text",
            "title":"R$551 ~ R$1.000",
            "payload":"BTN_ESCOLHA_RANGEALUGUEL.551-1000",
        },
        {
            "content_type":"text",
            "title":"R$1.001 ~ R$1.500",
            "payload":"BTN_ESCOLHA_RANGEALUGUEL.1001-1500",
        },
        {
            "content_type":"text",
            "title":"R$1.501 ~ R$2.000",
            "payload":"BTN_ESCOLHA_QTDVAGA.1501-2000",
        },
        {
            "content_type":"text",
            "title":"R$2.001 ~ R$2.500",
            "payload":"BTN_ESCOLHA_QTDVAGA.2001-2500",
        },
        {
            "content_type":"text",
            "title":"R$2.501 ~ R$3.000",
            "payload":"BTN_ESCOLHA_QTDVAGA.2501-3000",
        },
        {
            "content_type":"text",
            "title":"+R$3.001",
            "payload":"BTN_ESCOLHA_QTDVAGA.+3001",
        },
    ]