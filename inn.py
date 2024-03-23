from id import Id
from globals import data, data_idx
from globals import tokenizer


class In:
    def __init__(self):
        self.ids = []

    def parse_in(self):
        token = tokenizer.getToken()

        #print ("Inn, Start: ", token)

        if token != 10:
            raise ValueError("Expected 'read'")
        tokenizer.skipToken()

        id = Id()
        id.parse_id_assign()
        self.ids.append(id)
        while tokenizer.getToken() != 12:
            id = Id()
            id.parse_id_assign()
            self.ids.append(id)
        tokenizer.skipToken()

        # print ("Inn, End: ", token)

    def exec_in(self):        
        global data_idx
        # for id in self.ids:
        #     if not data[data_idx]:
        #         raise ValueError("not enough data provided")
        #     id.setValue(data[data_idx])
        # print("self.ids = ", len(self.ids))
        # print("data = ", len(data))
        # if len(self.ids) == len(data):
        for id in self.ids:
            val = data[data_idx]
            print("Read Val = {}".format(val), end="")
            id.setValue(val)
            data_idx += 1
        #print("Read Val", end="") # Debugging
        data_idx += 1

    def print_in(self):
        print("read ", end="")
        self.ids[0].print_id()
        if len(self.ids) > 1:
            for id in self.ids[1:]:
                print(", ")
                id.print_id()
        print()
