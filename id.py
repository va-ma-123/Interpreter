class Id:
    eIds = [None] * 20
    idCount = 0

    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.value = None
        self.name = None
        self.declared = False
        self.initialized = False

    def parse_id(self):
        idStr = self.tokenizer.getToken()
        for id in Id.eIds:
            if id and id.name == idStr:
                return id
            
        newId = Id(self.tokenizer)
        newId.name = idStr
        Id.eIds[Id.idCount] = newId
        Id.idCount += 1
        return newId

    def print_id(self):
        print(self.name, end='')

    def exec_id(self):
        # id doesn't have exec
        pass
    
    def getName(self):
        if not self.name:
            raise ValueError("ID name is not set")
        return self.name

    def getValue(self):
        if not self.initialized:
            raise ValueError("Variable '{}' is not initialized".format(self.name))
        return self.value
    
    def setValue(self, val):
        if not self.name:
            raise ValueError("ID name is not set")
        for id in Id.eIds:
            if id and id.name == self.name:
                id.value = val
                id.initialized = True
                return
        raise ValueError("ID '{}' does not exist".format(self.name))
