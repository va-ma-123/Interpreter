from cond import Cond
from globals import tokenizer

class Loop:
    def __init__(self): # <loop>	::=	while <cond> loop <stmt seq> end;
        self.cond = None
        self.ss = None

    def parse_loop(self):
        from stmt_seq import StmtSeq
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
    
    def print_loop(self):
        print("while ")
        self.cond.print_cond()
        print("loop ")
        self.ss.print_stmt_seq()
        print("end;")

    def exec_loop(self):
        while self.cond.exec_cond():
            self.ss.exec_stmt_seq()
