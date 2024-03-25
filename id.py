import sys

class Id:
    # dictionary to store the ids
    eIds = {}

    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.value = None
        self.initialized = False

    # check if Id is initialized
    @staticmethod
    def is_initialized(idName):
        return Id.eIds[idName].initialized

    # check if Id is declared
    @staticmethod
    def is_declared(idName):
        return idName in Id.eIds

    # parse the id declaration
    @staticmethod
    def parse_id_decl(idName,tokenizer):
        try:
            if Id.is_declared(idName): # Check if the ID is already declared
                raise ValueError("ID '{}' already declared".format(idName))
            newId = Id()
            Id.eIds[idName] = newId # Add the ID to the dictionary
            tokenizer.skipToken() # Skip the ID
        except ValueError as e:
            # Handle the error
            print("Error in parse_id_decl:", e)
            sys.exit(1)
        
    # parse the id assignment
    @staticmethod
    def parse_id_assign(idName,tokenizer): 
        tokenizer.skipToken() # Skip the ID
        try:
            if not Id.is_declared(idName): # Check if the ID is Not declared
                raise ValueError("ID '{}' not declared".format(idName))
        except ValueError as e:
            # Handle the error
            print("Error in parse_id_assign:", e)
            sys.exit(1)
            
        
    # pretty print the id
    def print_id(self):
        for id in Id.eIds:
            if Id.eIds[id] == self:
                print(id, end="")

    # No execute for id
    def exec_id(self):
        pass
    

    # get the value of the id
    @staticmethod
    def getValue(idName):
        return Id.eIds[idName].value
    
    # set the value of the id
    @staticmethod
    def setValue(idName, val):
        if not Id.is_declared(idName):
            raise ValueError("ID '{}' name is not declared".format(idName))
        Id.eIds[idName].value = val