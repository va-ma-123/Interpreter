from id import Id

class Out:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.ids = []

    def parse_in(self):
        token = self.tokenizer.getToken()
        if token != 11:
            raise ValueError("Expected 'write'")
        self.tokenizer.skip_token()

        id = Id(self.tokenizer)
        id.parse_id()
        self.ids.append(id)
        while self.tokenizer.getToken() != 12:
            id = Id(self.tokenizer)
            id.parse_id()
            self.ids.append(id)
        self.tokenizer.skipToken()

    def exec_in(self):
        for id in self.ids:
            print(id.getName(), end ="")
            print(" = ")
            print(id.getValue())

    def print_in(self):
        print("write ", end="")
        self.ids[0].print_id()
        if len(self.ids) > 1:
            for id in self.ids[1:]:
                print(", ")
                id.print_id()
        print()
