class Entity:
    _text = ""
    entities = {}

    def __init__(self, fromJson):
        self._text = fromJson["_text"]
        self.entities = fromJson["entities"]

