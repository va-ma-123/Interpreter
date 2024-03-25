from interpreter import  data_arr, data_idx
import sys
import id

class In:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.ids = []

    # parse the in    
    def parse_in(self):
        try:
            self.tokenizer.skipToken() # skip read
            idName = self.tokenizer.idVal() #gets the name of the id
            id.Id.parse_id_assign(idName,self.tokenizer)
            self.ids.append(idName)
            id.Id.eIds[idName].initialized = True    
            while self.tokenizer.getToken() != 12: # 12 is the token for ";"
                if self.tokenizer.getToken() != 13: # 13 is the token for ","
                    if self.tokenizer.getToken() == 32: # 32 is the token for "end"                    
                        raise ValueError("Expected ','")
                    else:
                        raise ValueError("Expected ';'")              
                self.tokenizer.skipToken() # skip ","
                idName = self.tokenizer.idVal() #gets the name of the id
                id.Id.parse_id_assign(idName,self.tokenizer)
                self.ids.append(idName)
                id.Id.eIds[idName].initialized = True    
            self.tokenizer.skipToken() # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_in:", e)
            sys.exit(1)

    def exec_in(self):        
        global data_idx   
        for idName in self.ids: # loop through the ids     
            val = data_arr[data_idx] # get the value from the data array
            #print("Read Val = {}".format(val), end="") # Houssam
            id.Id.setValue(idName,val) # set the value of the id
            data_idx += 1 # increment the data index

    # pretty print the in
    def print_in(self, indent=0): # pretty print the in
        print("   " * (indent + 1), end="") # print the indentation
        print("read ", end="") # print "read"
        print (self.ids[0], end="") # print the first id
        if len(self.ids) > 1: # if there are more than one id
            for id in self.ids[1:]: # loop through the ids
                print(", ", end="") # print ", "
                print(id, end="") # print the id
        print(";") # print ";"