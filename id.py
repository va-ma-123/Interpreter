from globals import tokenizer
import sys

class Id:
    eIds = {}

    def __init__(self):
        self.value = None
        self.initialized = False


    @staticmethod
    def is_initialized(idName):
        return Id.eIds[idName].initialized

    @staticmethod
    def is_declared(idName):
        return idName in Id.eIds

    @staticmethod
    def parse_id_decl(idName):
        try:
            if Id.is_declared(idName):
                raise ValueError("ID '{}' already declared".format(idName))
            newId = Id()
            Id.eIds[idName] = newId
            tokenizer.skipToken() # Skip the ID
        except ValueError as e:
            # Handle the error
            print("Error in parse_id_decl:", e)
            sys.exit(1)
        

    @staticmethod
    def parse_id_assign(idName):
        tokenizer.skipToken() # Skip the ID
        try:
            if not Id.is_declared(idName):
                raise ValueError("ID '{}' not declared".format(idName))
        except ValueError as e:
            # Handle the error
            print("Error in parse_id_assign:", e)
            sys.exit(1)
            
        

    def print_id(self):
        for id in Id.eIds:
            if Id.eIds[id] == self:
                print(id, end="")

    def exec_id(self):
        pass
    

    @staticmethod
    def getValue(idName):
        return Id.eIds[idName].value
    
    @staticmethod
    def setValue(idName, val):
        if not Id.is_declared(idName):
            raise ValueError("ID '{}' name is not declared".format(idName))
        Id.eIds[idName].value = val