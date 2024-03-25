import scanner
import sys

class Out:
    def __init__(self):
        self.ids = []

    def parse_out(self):
        try:
            tokenizer1.skipToken()  # skip write

            idName = tokenizer1.idVal()  # gets the name of the id
            Id.parse_id_assign(idName)
            self.ids.append(idName)
            while tokenizer1.getToken() == 13:
                tokenizer1.skipToken()  # skip ,
                idName = tokenizer1.idVal()
                Id.parse_id_assign(idName)
                self.ids.append(idName)
            if tokenizer1.getToken() != 12:
                raise ValueError("Expected ';'")  # Check for ; at end of decl
            tokenizer1.skipToken()  # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_out:", e)
            sys.exit(1)

    def exec_out(self):
        for idName in self.ids:
            print(idName, end ="")
            print(" = ", end="")
            print(Id.getValue(idName))

    def print_out(self, indent=0):
            print("   " * (indent + 1), end="")
            print("write ", end="")
            print(self.ids[0], end="")
            if len(self.ids) > 1:
                for id in self.ids[1:]:
                    print(", ", end="")
                    print(id, end="")
            print(";")

class In:
    def __init__(self):
        self.ids = []
        
    def parse_in(self):
        try:
            tokenizer1.skipToken() # skip read
            idName = tokenizer1.idVal() #gets the name of the id
            Id.parse_id_assign(idName)
            self.ids.append(idName)
            Id.eIds[idName].initialized = True    
            while tokenizer1.getToken() != 12:
                if tokenizer1.getToken() != 13:
                    if tokenizer1.getToken() == 32:                        
                        raise ValueError("Expected ','")
                    else:
                        raise ValueError("Expected ';'")              
                tokenizer1.skipToken() # skip ","
                idName = tokenizer1.idVal() #gets the name of the id
                Id.parse_id_assign(idName)
                self.ids.append(idName)
                Id.eIds[idName].initialized = True    
            tokenizer1.skipToken() # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_in:", e)
            sys.exit(1)

    def exec_in(self):        
        global data_idx     #(if doesnt work in seperate class)
        for idName in self.ids:
            val = data[data_idx]
            #print("Read Val = {}".format(val), end="") # Houssam
            Id.setValue(idName,val)
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
            tokenizer1.skipToken() # Skip the ID
        except ValueError as e:
            # Handle the error
            print("Error in parse_id_decl:", e)
            sys.exit(1)
        

    @staticmethod
    def parse_id_assign(idName):
        tokenizer1.skipToken() # Skip the ID
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
        # print(self, end='')

    def exec_id(self):
        # id doesn't have exec
        pass
    
    # def getName(self):
    #     if not self.is_declared():
    #         raise ValueError("Variable '{}' is not declared".format(self))
    #     return self

    @staticmethod
    def getValue(idName):
        return Id.eIds[idName].value
    
    @staticmethod
    def setValue(idName, val):
        if not Id.is_declared(idName):
            raise ValueError("ID '{}' name is not declared".format(idName))
        Id.eIds[idName].value = val
        #Id.eIds[idName].initialized = True

compops = ['!=','==','<','>','<=','>=']

class Comp:
    def __init__(self):
        self.op1 = None
        self.op2 = None
        self.compop = None

    def parse_comp(self):
        try:
            tokenizer1.skipToken() # skip '('
            self.op1 = Op()
            self.op1.parse_op()
            if 25 <= tokenizer1.getToken() <= 30:
                self.compop = tokenizer1.getToken() - 25
                tokenizer1.skipToken()
                self.op2 = Op()
                self.op2.parse_op()
                if tokenizer1.getToken() != 21:
                    raise ValueError("Expected ')'")
                tokenizer1.skipToken()
            else:
                raise ValueError("Invalid comparison operator")
        except ValueError as e:
            # Handle the error
            print("Error in parse_comp:", e)
            sys.exit(1)
    
    def exec_comp(self):
        val1 = self.op1.exec_op()
        val2 = self.op2.exec_op()
        operation = compops[self.compop]
        comp_expr = f"{val1}{operation}{val2}"
        return eval(comp_expr)
    
    def print_comp(self):
        print("(", end="")
        self.op1.print_op()
        print("", compops[self.compop], "", end="")
        self.op2.print_op()
        print(")", end="")

class Op:
    def __init__(self):
        self.value = None
        self.id = None
        self.exp = None

    def parse_op(self):

        try:
            token = tokenizer1.getToken()
            if token == 31: # int
                tokenVal = tokenizer1.intVal()
                self.value = tokenVal
                tokenizer1.skipToken()
            elif token ==32: # id
                self.id = tokenizer1.idVal()
                if not Id.is_initialized(self.id):
                    raise ValueError(f"ID '{self.id}' not initialized")
                Id.parse_id_assign(self.id)
            elif token == 20: # (Exp)
                tokenizer1.skipToken()
                self.exp = Exp()
                self.exp.parse_exp()
                if tokenizer1.getToken() != 21:
                    raise ValueError("Expected ')")
                tokenizer1.skipToken()
        except ValueError as e:
            # Handle the error
            print("Error in parse_op:", e)
            sys.exit(1)

    def exec_op(self):
        if self.id is not None:
            return Id.getValue(self.id)
        elif self.exp is not None:
            return self.exp.exec_exp()
        else:
            return self.value
        
    def print_op(self):
        if self.id is not None:
            print (self.id, end="")
        elif self.exp is not None:
            print("(", end="")
            self.exp.print_exp()
            print(")", end="")
        else:
            print(self.value, end="")

class Fac:
    def __init__(self):
        self.op = None
        self.fac = None

    def parse_fac(self):

        self.op = Op()
        self.op.parse_op()
        if tokenizer1.getToken() == 24:
            tokenizer1.skipToken()
            self.fac = Fac()
            self.fac.parse_fac()


    def exec_fac(self):
        result = self.op.exec_op()
        if self.fac:
            result *= self.fac.exec_fac()
        return result

    def print_fac(self):
        self.op.print_op()
        if self.fac:
            print(" * ", end="")
            self.fac.print_fac()
    
class Exp:
    def __init__(self):
        self.fac = None
        self.op = None
        self.exp = None

    def parse_exp(self):
        self.fac = Fac()
        self.fac.parse_fac()

        token = tokenizer1.getToken()
        if(token in (22,23)):
            if token == 22:
                self.op = 0
            elif token == 23:
                self.op = 1
            tokenizer1.skipToken()
            self.exp = Exp()
            self.exp.parse_exp()
        
            

    def print_exp(self):
        self.fac.print_fac()
        if self.op is not None:
            print(" ", end="")
            if self.op == 0:
                print("+", end="")
            else:
                print("-", end="")
            print(" ", end="")
            self.exp.print_exp()

    def exec_exp(self):
        result = self.fac.exec_fac()
        if self.exp:
            if self.op == 0:
                result += self.exp.exec_exp()
            elif self.op == 1:
                result -= self.exp.exec_exp()
        return result
    
class Cond:
    def __init__(self):
        self.comp = None
        self.negation = False
        self.cond1 = None
        self.cond2 = None
        self.andor = None

    def parse_cond(self):
        try:
            if tokenizer1.getToken() == 15: # negation
                self.negation = True
                tokenizer1.skipToken()
                self.cond1 = Cond()
                self.cond1.parse_cond()
            elif tokenizer1.getToken() == 20: # comp
                self.comp = Comp()
                self.comp.parse_comp()
            elif tokenizer1.getToken() == 16:
                tokenizer1.skipToken() # skip [
                self.cond1 = Cond()
                self.cond1.parse_cond()
                if tokenizer1.getToken() != 18 and tokenizer1.getToken() != 19:
                    raise ValueError("Expected '&&' or '||'")
                if(tokenizer1.getToken() == 18):
                    self.andor = 0
                else:
                    self.andor = 1
                tokenizer1.skipToken()
                self.cond2 = Cond()
                self.cond2.parse_cond()
                if tokenizer1.getToken() != 17:
                    raise ValueError("Expected ']")
                tokenizer1.skipToken() # skip ]
            else:
                raise ValueError("Expected a condition")
        except ValueError as e:
            # Handle the error
            print("Error in parse_cond:", e)
            sys.exit(1)
        
    def exec_cond(self):
        if self.comp is not None:
            return self.comp.exec_comp()
        elif self.negation:
            return not self.cond1.exec_cond()
        elif self.andor == 0:
            return self.cond1.exec_cond() and self.cond2.exec_cond()
        else: 
            return self.cond1.exec_cond() or self.cond2.exec_cond()
        
    def print_cond(self):
        if self.comp is not None:
            self.comp.print_comp()
        elif self.negation:
            print("!", end="") 
            self.cond1.print_cond()
        elif self.andor == 0:
            print("[", end="")
            self.cond1.print_cond() 
            print(" && ", end="") 
            self.cond2.print_cond()
            print("]", end="")
        else: 
            print("[", end="")
            self.cond1.print_cond() 
            print(" || ", end="")
            self.cond2.print_cond() 
            print("]", end="")            
        
class Loop:
    def __init__(self): # <loop>	::=	while <cond> loop <stmt seq> end;
        self.cond = None
        self.ss = None

    def parse_loop(self):
        try:
            tokenizer1.skipToken() # skip "while"
            self.cond = Cond()
            self.cond.parse_cond()
            if tokenizer1.getToken() != 9:
                raise ValueError("'loop' expected")
            tokenizer1.skipToken()
            self.ss = StmtSeq()
            self.ss.parse_stmt_seq()
            if tokenizer1.getToken() != 3:
                raise ValueError("'end' expected")
            tokenizer1.skipToken()
            if tokenizer1.getToken() != 12:
                raise ValueError("';' expected")
            tokenizer1.skipToken()
        except ValueError as e:
            # Handle the error
            print("Error in parse_loop:", e)
            sys.exit(1)

    def exec_loop(self):
        while self.cond.exec_cond():
            self.ss.exec_stmt_seq()

    def print_loop(self, indent=0):
        print("   " * (indent + 1), end="")
        print("while ", end="")
        self.cond.print_cond()
        print(" loop")
        self.ss.print_stmt_seq(indent + 1)
        print("   " * (indent + 1), end="")
        print("end;")

class If:
    def __init__(self):
        self.cond = None
        self.ss1 = None
        self.ss2 = None

    def parse_if(self):
        try: 
            tokenizer1.skipToken() # skip "if"
            self.cond = Cond()
            self.cond.parse_cond()

            if tokenizer1.getToken() != 6:
                raise ValueError("'then' Expected")

            tokenizer1.skipToken() # skip "then"

            self.ss1 = StmtSeq()
            self.ss1.parse_stmt_seq()

            if tokenizer1.getToken() == 7:
                tokenizer1.skipToken() # skip "else"
                self.ss2 = StmtSeq()
                self.ss2.parse_stmt_seq()
            
            if tokenizer1.getToken() != 3:
                raise ValueError("'end' Expected")
                
            tokenizer1.skipToken() # skip "end"
            if tokenizer1.getToken() != 12:
                raise ValueError("';' Expected")
                
            tokenizer1.skipToken() # skip ";"
            #print("ENd If: ", tokenizer.getToken())
        except ValueError as e:
            # Handle the error
            print("Error in parse_if:", e)
            sys.exit(1)

 
    def exec_if(self):
        if self.cond.exec_cond():
            self.ss1.exec_stmt_seq()
            return
        if self.ss2 is not None:
            self.ss2.exec_stmt_seq()
            return
        
    def print_if(self, indent=0):
        print("   " * (indent + 1), end="")
        print("if ", end="")
        self.cond.print_cond()
        print(" then")
        self.ss1.print_stmt_seq(indent + 1)
        if self.ss2:
            print("   " * (indent + 1), end="")
            print("else")
            self.ss2.print_stmt_seq(indent + 1)
        print("   " * (indent + 1), end="")
        print("end;")
        
class Assign:
    def __init__(self): # <assign> ::= <id> = <exp>;
        self.id = None
        self.exp = None

    def parse_assign(self):
        
        try:
            self.id = tokenizer1.idVal() #returns the name of the id
            Id.parse_id_assign(self.id) #parse the id
            if tokenizer1.getToken() != 14:
                raise ValueError("'=' Expected")
            tokenizer1.skipToken() # skip =
            self.exp = Exp()
            self.exp.parse_exp()
            Id.eIds[self.id].initialized = True
            if tokenizer1.getToken() != 12:
                raise ValueError("';' Expected")
            tokenizer1.skipToken() # skip ;
        except ValueError as e:
            # Handle the error
            print("Error in parse_assign:", e)
            sys.exit(1)
        
        

    def exec_assign(self):
        val = self.exp.exec_exp()
        Id.setValue(self.id,val)

    def print_assign(self, indent=0):
        print("   " * (indent + 1), end="")
        print (self.id, end="")
        print(" = ", end="")
        self.exp.print_exp()
        print(";")

class Stmt:
    def __init__(self):
        self.assign = None
        self.if_stmt = None
        self.loop = None
        self.in_stmt = None
        self.out_stmt = None

    def parse_stmt(self):
        token = tokenizer1.getToken()  # Fetch the next token
        # if token is None:
        #     return  # Return if there are no more tokens
        
        try:
            if token == 5:
                # If the token is 'if', parse if
                self.if_stmt = If()
                self.if_stmt.parse_if()
            elif token == 8:
                # If the token is 'while', parse loop
                self.loop = Loop()
                self.loop.parse_loop()
            elif token == 10:
                # If the token is 'read', parse in
                self.in_stmt = In()
                self.in_stmt.parse_in()
            elif token == 11:
                # If the token is 'write', parse out
                self.out_stmt = Out()
                self.out_stmt.parse_out()
            elif token == 32:
                # parse assign
                self.assign = Assign()
                self.assign.parse_assign()
            elif token == 33:
                raise ValueError("end Expected")
            else:
                raise ValueError("Invalid statement")
        except ValueError as e:
            # Handle the error
            print("Error in parse_stmt:", e)
            sys.exit(1)
    
    def exec_stmt(self):
        if self.assign:
            self.assign.exec_assign()
        elif self.if_stmt:
            self.if_stmt.exec_if()
        elif self.loop:
            self.loop.exec_loop()
        elif self.in_stmt:
            self.in_stmt.exec_in()
        elif self.out_stmt:
            self.out_stmt.exec_out()

    def print_stmt(self, indent=0):
        # Updated method to print the statement
        if self.assign:
            self.assign.print_assign(indent)
        elif self.if_stmt:
            self.if_stmt.print_if(indent)
        elif self.loop:
            self.loop.print_loop(indent)
        elif self.in_stmt:
            self.in_stmt.print_in(indent)
        elif self.out_stmt:
            self.out_stmt.print_out(indent)

    # def _print_indented(self, indent):
    #     print(" " * indent, end="")

class Decl:
    def __init__(self): #<decl> ::= int  <id list>;
        self.ids = []

    def parse_decl(self): # Parse decl         
        # Check for "int"
        try:
            if tokenizer1.getToken() != 4: 
                raise ValueError("'int' Expected")
            
            tokenizer1.skipToken() # skip "int"

            idName = tokenizer1.idVal() #gets the name of the id
            #self.id_list = IDList(tokenizer)
            Id.parse_id_decl(idName)
            self.ids.append(idName)
            while tokenizer1.getToken() != 12:
                if tokenizer1.getToken() != 13:
                    if tokenizer1.getToken() == 32:                        
                        raise ValueError("Expected ','")
                    else:
                        raise ValueError("Expected ';'") 
                tokenizer1.skipToken() # skip ,
                idName = tokenizer1.idVal() #gets the name of the id
                #self.id_list = IDList(tokenizer)
                Id.parse_id_decl(idName)
                self.ids.append(idName)                    
            
            tokenizer1.skipToken() # skip ";"
        except ValueError as e:
            # Handle the error
            print("Error in parse_decl:", e)
            sys.exit(1)

    def exec_decl(self):
        pass

    def print_decl(self, indent=0):
        print("   " * (indent + 1), end="")
        print("int ", end="")
        print(self.ids[0], end="")
        if len(self.ids) > 1:
            for idName in self.ids[1:]:
                print(", ", end="")
                print(idName, end="")
        print(";")

class StmtSeq:
    def __init__(self): # <stmt seq>	::= <stmt> | <stmt> <stmt seq>
        self.stmt = None
        self.stmt_seq = None

    def parse_stmt_seq(self):   # Parse stmt seq     
        self.stmt = Stmt() 
        self.stmt.parse_stmt() 

        # check for more stmt's
        if tokenizer1.getToken() == 3 or tokenizer1.getToken() == 7:
            # 3 = end, 7 = else, if end or else is next token, this is end of stmt seq
            return
        self.stmt_seq = StmtSeq()
        self.stmt_seq.parse_stmt_seq()

    def exec_stmt_seq(self):
        self.stmt.exec_stmt()
        if self.stmt_seq is not None:
            self.stmt_seq.exec_stmt_seq()

    def print_stmt_seq(self, indent=2):
        self.stmt.print_stmt(indent)
        if self.stmt_seq:
           self.stmt_seq.print_stmt_seq(indent)

class DeclSeq:
    def __init__(self): # <decl seq>	::= <decl> | <decl> <decl seq>
        self.decl = None
        self.decl_seq = None 

    def parse_decl_seq(self):   # Parse decl seq     
        self.decl = Decl() 
        self.decl.parse_decl() 

        if tokenizer1.getToken() != 4:  # Check for "int"
            return
        self.decl_seq = DeclSeq()    
        self.decl_seq.parse_decl_seq()

    def exec_decl_seq(self):
        pass

    def print_decl_seq(self, indent=0):
        self.decl.print_decl()
        if self.decl_seq is not None:
            self.decl_seq.print_decl_seq(indent)

class Prog:
    def __init__(self): #<prog> ::= program <decl seq> begin <stmt seq> end
        self.ds = None
        self.ss = None

    def parse_prog(self): # Parse program 
        try:
            if tokenizer1.getToken() != 1:  # Check if the token is "program"
                raise ValueError("'program' Expected")
            
            tokenizer1.skipToken()  # Skip "program"
            self.ds = DeclSeq()
            self.ds.parse_decl_seq() # Parse <decl seq>

            # Parse begin
            if tokenizer1.getToken() != 2:  # Check if the token is "begin"
                raise ValueError("'begin' Expected")
            
            tokenizer1.skipToken()  # Skip "begin"

            self.ss = StmtSeq()
            self.ss.parse_stmt_seq() # Parse <stmt seq>

            if tokenizer1.getToken() != 3 and tokenizer1.getToken() != 33:
                raise ValueError("'end' Expected")
            tokenizer1.skipToken()  # Skip "end"
        except ValueError as e:
            # Handle the error
            print("Error in parse_prog:", e)
            sys.exit(1)

    def exec_prog(self):
        self.ds.exec_decl_seq()
        self.ss.exec_stmt_seq()

    def print_prog(self, indent=0):
        print("program")
        if self.ds:
            self.ds.print_decl_seq(indent + 1)
        print("   " * (indent + 1), end="")
        print("begin")
        self.ss.print_stmt_seq(indent + 1)
        print("   " * (indent + 1), end="")
        print("end")
 
if __name__ == "__main__":

    data = []
    data_idx = 0
    

    if len(sys.argv) != 3:
        print("Usage: python program.py <core_program_file> <data_file>")
        sys.exit(1)

    core_program_file = sys.argv[1]
    data_file = sys.argv[2]
    tokenizer1 = scanner.Scanner(core_program_file)

    
    # Read data from the data file
    with open(data_file, 'r') as file:
        for line in file:
            data.append(int(line.strip()))
    
    # Create an instance of the Prog class
    prog = Prog()
    
    # Parse the program
    prog.parse_prog()
    print("\nProgram Execution Output:\n")
    prog.exec_prog()
    print("\nPretty Print Program Output:\n")
    prog.print_prog()
    
