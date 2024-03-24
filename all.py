from globals import tokenizer
from globals import data, data_idx


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

        while tokenizer.getToken() == 13:
            tokenizer.skipToken() # skip ,
            id = Id()
            id.parse_id_assign()
            self.ids.append(id)
        if tokenizer.getToken() != 12:
            raise ValueError("Expected ';'") # Check for ; at end of decl
        tokenizer.skipToken() # skip ";"

    def exec_out(self):
        for id in self.ids:
            print(id.getName(), end ="")
            print(" = ")
            print(id.getValue())

    def print_out(self, indent=0):
            print("   " * (indent + 1), end="")
            print("write ", end="")
            self.ids[0].print_id()
            if len(self.ids) > 1:
                for id in self.ids[1:]:
                    print(", ", end="")
                    id.print_id()
            print(";")

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
        for id in self.ids:
            val = data[data_idx]
            print("Read Val = {}".format(val), end="")
            id.setValue(val)
            data_idx += 1
        data_idx += 1

    def print_in(self, indent=0):
        print("   " * (indent + 1), end="")
        print("read ", end="")
        self.ids[0].print_id()
        if len(self.ids) > 1:
            for id in self.ids[1:]:
                print(", ", end="")
                id.print_id()
        print(";")

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
        tokenizer.skipToken()
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

compops = ['!=','==','<','>','<=','>=']

class Comp:
    def __init__(self):
        self.op1 = None
        self.op2 = None
        self.compop = None

    def parse_comp(self):
        if tokenizer.getToken() != 20:
            raise ValueError("Expected '('")
        tokenizer.skipToken()
        self.op1 = Op()
        self.op1.parse_op()
        if 25 <= tokenizer.getToken() <= 30:
            self.compop = tokenizer.getToken() - 25
            tokenizer.skipToken()
            self.op2 = Op()
            self.op2.parse_op()
            if tokenizer.getToken() != 21:
                raise ValueError("Expected ')'")
            tokenizer.skipToken()
        else:
            raise ValueError("Invalid comparison operator")
    
    def exec_comp(self):
        val1 = self.op1.exec_op()
        print("Val 1 : ",val1)
        val2 = self.op2.exec_op()
        print("Val 2 : ",val2)
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

        token = tokenizer.getToken()
        if token == 31:
            tokenVal = tokenizer.intVal()
            self.value = tokenVal
            tokenizer.skipToken()
        elif token ==32:
            self.id = Id()
            self.id.parse_id_assign()
        elif token == 20:
            tokenizer.skipToken()
            self.exp = Exp()
            self.exp.parse_exp()
            if tokenizer.getToken() != 21:
                raise ValueError("Expected ')")
            tokenizer.skipToken()

    def exec_op(self):
        if self.id is not None:
            return self.id.getValue()
        elif self.exp is not None:
            return self.exp.exec_exp()
        else:
            return self.value
        
    def print_op(self):
        if self.id is not None:
            self.id.print_id()
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
        if tokenizer.getToken() == 24:
            tokenizer.skipToken()
            self.fac = Fac()
            self.fac.parse_fac()

    def print_fac(self):
        self.op.print_op()
        if self.fac:
            print(" * ", end="")
            self.fac.print_fac()

    def exec_fac(self):
        result = self.op.exec_op()
        if self.fac:
            result *= self.fac.exec_fac()
        return result
    
class Exp:
    def __init__(self):
        self.fac = None
        self.op = None
        self.exp = None

    def parse_exp(self):
        self.fac = Fac()
        self.fac.parse_fac()

        token = tokenizer.getToken()
        if(token in (22,23)):
            if token == 22:
                self.op = 0
            elif token == 23:
                self.op = 1
            tokenizer.skipToken()
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
        if tokenizer.getToken() == 15: # negation
            self.negation = True
            tokenizer.skipToken()
            self.cond1 = Cond()
            self.cond1.parse_cond()
        elif tokenizer.getToken() == 20: # comp
            self.comp = Comp()
            self.comp.parse_comp()
        elif tokenizer.getToken() == 16:
            tokenizer.skipToken() # skip [
            self.cond1 = Cond()
            self.cond1.parse_cond()
            if tokenizer.getToken() != 18 and tokenizer.getToken() != 19:
                raise ValueError("Expected '&&' or '||'")
            if(tokenizer.getToken() == 18):
                self.andor = 0
            else:
                self.andor = 1
            tokenizer.skipToken()
            self.cond2 = Cond()
            self.cond2.parse_cond()
            if tokenizer.getToken() != 17:
                raise ValueError("Expected ']")
            tokenizer.skipToken() # skip ]
        else:
            print("ERROR: not a condition")
            return
        
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
        if tokenizer.getToken() != 8:
            print("ERROR: 'while' expected")
            return
        tokenizer.skipToken()
        #print ("Loop: While", tokenizer.getToken())
        self.cond = Cond()
        self.cond.parse_cond()
        if tokenizer.getToken() != 9:
            print("ERROR: 'loop' expected")
            return
        tokenizer.skipToken()
        self.ss = StmtSeq()
        self.ss.parse_stmt_seq()
        if tokenizer.getToken() != 3:
            print("ERROR: 'end' expected")
            return
        tokenizer.skipToken()
        if tokenizer.getToken() != 12:
            print("ERROR: ';' expected")
            return
        tokenizer.skipToken()
        #print("ENd Loop: ", tokenizer.getToken())

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
        if tokenizer.getToken() != 5:
            print("ERROR: expected 'if'")
            return
        tokenizer.skipToken() # skip "if"

        #print("If: ", tokenizer.getToken())

        self.cond = Cond()
        self.cond.parse_cond()

        if tokenizer.getToken() != 6:
            print("ERROR: expected 'then'")
            return
        tokenizer.skipToken() # skip "then"

        self.ss1 = StmtSeq()
        self.ss1.parse_stmt_seq()

        if tokenizer.getToken() == 7:
            tokenizer.skipToken() # skip "else"
            self.ss2 = StmtSeq()
            self.ss2.parse_stmt_seq()
        
        if tokenizer.getToken() != 3:
            print("ERROR: expected 'end'")
            return
        tokenizer.skipToken() # skip "end"
        if tokenizer.getToken() != 12:
            print("ERROR: expected ';'")
            return
        tokenizer.skipToken() # skip ";"
        #print("ENd If: ", tokenizer.getToken())

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

    def exec_if(self):
        if self.cond.exec_cond():
            self.ss1.exec_stmt_seq()
            return
        if self.ss2 is not None:
            self.ss2.exec_stmt_seq()
            return
        
class Assign:
    def __init__(self): # <assign> ::= <id> = <exp>;
        self.id = None
        self.exp = None

    def parse_assign(self):
        self.id = Id()
        self.id.parse_id_assign()
        if tokenizer.getToken() != 14:
            print("ERROR: '=' expected")
            return
        tokenizer.skipToken() # skip =
        self.exp = Exp()
        self.exp.parse_exp()
        if tokenizer.getToken() != 12:
            print("ERROR: ';' expected")
            return
        tokenizer.skipToken() # skip ;

    def exec_assign(self):
        val = self.exp.exec_exp()
        self.id.setValue(val)

    def print_assign(self, indent=0):
        print("   " * (indent + 1), end="")
        self.id.print_id()
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
        token = tokenizer.getToken()  # Fetch the next token
        if token is None:
            return  # Return if there are no more tokens
        
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
        else:
            raise ValueError("Invalid statement")
    
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

    def _print_indented(self, indent):
        print(" " * indent, end="")

class Decl:
    def __init__(self): #<decl> ::= int  <id list>;
        self.ids = []

    def parse_decl(self): # Parse decl         
        # Check for "int"
        if tokenizer.getToken() != 4: 
            print("ERROR: Expected 'int'")
            return
        tokenizer.skipToken() # skip "int"

        id = Id()
        #self.id_list = IDList(tokenizer)
        id.parse_id_decl()
        self.ids.append(id)
        while tokenizer.getToken() == 13:
            tokenizer.skipToken() # skip ,
            id = Id()
            id.parse_id_decl()
            self.ids.append(id)
        if tokenizer.getToken() != 12: # Check for ; at end of decl
            print("Decl.py line 25 ")
            print (tokenizer.getToken())
            print("ERROR: Expected ';'")
            return
        tokenizer.skipToken() # skip ";"

    def exec_decl(self):
        self.ids[0].exec_id()
        if len(self.ids)>1:
            for id in self.ids[1:]:
                id.exec_id()

    def print_decl(self, indent=0):
        print("   " * (indent + 1), end="")
        print("int ", end="")
        print(self.ids[0].getName(), end="")
        if len(self.ids) > 1:
            for id in self.ids[1:]:
                print(", ", end="")
                id.print_id()
        print(";")

class StmtSeq:
    def __init__(self): # <stmt seq>	::= <stmt> | <stmt> <stmt seq>
        self.stmt = None
        self.stmt_seq = None

    def parse_stmt_seq(self):   # Parse stmt seq     
        self.stmt = Stmt() 
        self.stmt.parse_stmt() 

        # check for more stmt's
        if tokenizer.getToken() == 3 or tokenizer.getToken() == 7:
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

        if tokenizer.getToken() != 4:  # Check for "int"
            return
        self.decl_seq = DeclSeq()    
        self.decl_seq.parse_decl_seq()

    def exec_decl_seq(self):
        self.decl.exec_decl()
        if self.decl_seq is not None:
            self.decl_seq.exec_decl_seq()

    def print_decl_seq(self, indent=0):
        self.decl.print_decl()
        if self.decl_seq is not None:
            self.decl_seq.print_decl_seq(indent)

class Prog:
    def __init__(self): #<prog> ::= program <decl seq> begin <stmt seq> end
        self.ds = None
        self.ss = None

    def parse_prog(self): # Parse program    
        if tokenizer.getToken() != 1:  # Check if the token is "program"
            print("ERROR: Expected 'program'")
            return
        
        tokenizer.skipToken()  # Skip "program"
        self.ds = DeclSeq()
        self.ds.parse_decl_seq() # Parse <decl seq>

        # Parse begin
        if tokenizer.getToken() != 2:  # Check if the token is "begin"
            print("ERROR: Expected 'begin'")
            return
        tokenizer.skipToken()  # Skip "begin"
        self.ss = StmtSeq()
        self.ss.parse_stmt_seq() # Parse <stmt seq>
        
        # Parse "end"
        if tokenizer.getToken() != 3:  # Check if the token is "end"
            print("ERROR: Expected 'end'")
            return
        tokenizer.skipToken()  # Skip "end"

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
    data_file = "testdata/5data.txt"
    
    with open(data_file, 'r') as file:
        for line in file:
            data.append(int(line.strip()))
    prog = Prog()
    
    # Parse the program
    prog.parse_prog()
    #prog.print_prog()
    prog.exec_prog()