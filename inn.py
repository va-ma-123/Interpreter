from globals import tokenizer, data_arr, data_idx
import sys
import id

class In:
    def __init__(self):
        self.ids = []
        
    def parse_in(self):
        try:
            tokenizer.skipToken() # skip read
            idName = tokenizer.idVal() #gets the name of the id
            id.Id.parse_id_assign(idName)
            self.ids.append(idName)
            id.Id.eIds[idName].initialized = True    
            while tokenizer.getToken() != 12:
                if tokenizer.getToken() != 13:
                    if tokenizer.getToken() == 32:                        
                        raise ValueError("Expected ','")
                    else:
                        raise ValueError("Expected ';'")              
                tokenizer.skipToken() # skip ","
                idName = tokenizer.idVal() #gets the name of the id
                id.Id.parse_id_assign(idName)
                self.ids.append(idName)
                id.Id.eIds[idName].initialized = True    
            tokenizer.skipToken() # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_in:", e)
            sys.exit(1)

    def exec_in(self):        
        global data_idx     #(if doesnt work in seperate class)
        for idName in self.ids:
            val = data_arr[data_idx]
            #print("Read Val = {}".format(val), end="") # Houssam
            id.Id.setValue(idName,val)
            data_idx += 1

    def print_in(self, indent=0):
        print("   " * (indent + 1), end="")
        print("read ", end="")
        print (self.ids[0], end="")
        if len(self.ids) > 1:
            for id in self.ids[1:]:
                print(", ", end="")
                print(id, end="")
        print(";")