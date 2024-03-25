from globals import tokenizer
import sys
import id

class Out:
    def __init__(self):
        self.ids = []

    def parse_out(self):
        try:
            tokenizer.skipToken()  # skip write

            idName = tokenizer.idVal()  # gets the name of the id
            id.Id.parse_id_assign(idName)
            self.ids.append(idName)
            while tokenizer.getToken() == 13:
                tokenizer.skipToken()  # skip ,
                idName = tokenizer.idVal()
                id.Id.parse_id_assign(idName)
                self.ids.append(idName)
            if tokenizer.getToken() != 12:
                raise ValueError("Expected ';'")  # Check for ; at end of decl
            tokenizer.skipToken()  # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_out:", e)
            sys.exit(1)

    def exec_out(self):
        for idName in self.ids:
            print(idName, end ="")
            print(" = ", end="")
            print(id.Id.getValue(idName))

    def print_out(self, indent=0):
            print("   " * (indent + 1), end="")
            print("write ", end="")
            print(self.ids[0], end="")
            if len(self.ids) > 1:
                for id in self.ids[1:]:
                    print(", ", end="")
                    print(id, end="")
            print(";")
