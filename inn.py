from id import Id
from globals import data, data_idx

class In:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.ids = []

    def parse_in(self):
        token = self.tokenizer.getToken()
        if token != 10:
            raise ValueError("Expected 'read'")
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
            if not data[data_idx]:
                raise ValueError("not enough data provided")
            id.setValue(data[data_idx])
            data_idx += 1

    def print_in(self):
        print("read ", end="")
        self.ids[0].print_id()
        if len(self.ids) > 1:
            for id in self.ids[1:]:
                print(", ")
                id.print_id()
        print()
