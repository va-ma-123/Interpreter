from id import Id
from globals import tokenizer

class Out:
    def __init__(self):
        self.ids = []

    def parse_out(self):
        token = tokenizer.getToken()

        # print ("Out, Start: ", token)   # Debugging

        if token != 11:
            raise ValueError("Expected 'write'")
        tokenizer.skipToken() # skip write

        id = Id()
        id.parse_id_assign()
        self.ids.append(id)

        # Debugging
        # for id in self.ids:
        #     print(id.getName(), end ="")
        #     print(" = ", end="")
        #     print(id.getValue())

        while tokenizer.getToken() == 13:
            tokenizer.skipToken() # skip ,
            id = Id()
            id.parse_id_assign()
            self.ids.append(id)
        if tokenizer.getToken() != 12:
            raise ValueError("Expected ';'") # Check for ; at end of decl
        tokenizer.skipToken() # skip ";"

        # print ("Out, End: ", token)

    def exec_out(self):
        for id in self.ids:
            print(id.getName(), end ="")
            print(" = ")
            print(id.getValue())

    def print_out(self):
        print("write ", end="")
        self.ids[0].print_id()
        if len(self.ids) > 1:
            for id in self.ids[1:]:
                print(", ")
                id.print_id()
        print()
