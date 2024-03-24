from globals import tokenizer

class Id:
    eIds = {}
    idCount = 0

    def __init__(self):
        self.value = None
        self.name = None

    def is_declared(self):
        return self.name in Id.eIds

    def parse_id_decl(self):
        idStr = tokenizer.idVal()
        tokenizer.skipToken()
        self.name = idStr
        if self.is_declared():
            raise ValueError("ID '{}' already declared".format(idStr))
        else:
            Id.eIds[idStr] = None
            Id.idCount += 1

    def parse_id_assign(self):
        idStr = tokenizer.idVal()
        tokenizer.skipToken() # Skip the ID
        self.name = idStr
        if not self.is_declared():
            raise ValueError("ID '{}' not declared".format(idStr))
        # Initialize the value and mark as initialized
        self.value = 0
        Id.eIds[idStr] = self

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
        if self.value is None:
            raise ValueError("Variable '{}' is not initialized".format(self.name))
        return self.value
    
    def setValue(self, val):
        if not self.name:
            raise ValueError("ID name is not declared")
        if self.name not in Id.eIds:
            raise ValueError("ID '{}' does not exist".format(self.name))
        Id.eIds[self.name].value = val



# from globals import tokenizer

# class Id:
#     eIds = [None] * 20
#     idCount = 0

#     def __init__(self):
#         self.value = None
#         self.name = None


#     # def parse_id_decl(self):
#     #     idStr = tokenizer.idVal()
#     #     tokenizer.skipToken()
#     #     self.name = idStr
#     #     for id in Id.eIds:
#     #         if id is not None and id.name == idStr:
#     #             raise ValueError("ID '{}' already declared".format(idStr))
#     #     else:
#     #         Id.eIds[Id.idCount] = self.name
#     #         self.declared = True
#     #         Id.idCount += 1
        

#     def is_declared(self):
#         for id_loop in Id.eIds:
#             if id_loop is not None and id_loop == self.name:
#                 return True
#         return False


#     def parse_id_decl(self):
#         idStr = tokenizer.idVal()
#         tokenizer.skipToken()
#         self.name = idStr
#         if self.is_declared():
#             raise ValueError("ID '{}' already declared".format(idStr))
#         else:
#             Id.eIds[Id.idCount] = self.name
#             self.declared = True
#             Id.idCount += 1

#     def parse_id_assign(self):
#         idStr = tokenizer.idVal()
#         tokenizer.skipToken()
#         self.name = idStr
#         if not self.is_declared():
#             raise ValueError("ID {}' not declared".format(idStr))
#         self.initialized = True

#         self.value = 0          # default value
#        # newId = Id()
#         # newId.name = idStr
#         # Id.eIds[Id.idCount] = newId
#         # self.declared = True
#         # Id.idCount += 1
#         # return newId

#     def print_id(self):
#         print(self.name, end='')

#     def exec_id(self):
#         # id doesn't have exec
#         pass
    
#     def getName(self):
#         if not self.name:
#             raise ValueError("ID name is not set")
#         return self.name

#     def getValue(self):
#         if self.value is None:
#             raise ValueError("Variable '{}' is not initialized".format(self.name))
#         return self.value
    
#     def setValue(self, val):
#         if not self.name:
#             raise ValueError("ID name is not declared")
#         for id in Id.eIds:
#             if id and id == self.name:
#                 id.value = val
#                 # id.initialized = True
#                 return
#         # raise ValueError("ID '{}' does not exist".format(self.name))
