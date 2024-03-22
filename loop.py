from cond import Cond
import stmt_seq as StmtSeq

class Loop:
    def __init__(self, tokenizer): # <loop>	::=	while <cond> loop <stmt seq> end;
        self.tokenizer = tokenizer
        self.cond = None
        self.ss = None

    def parse_loop(self):
        if self.tokenizer.getToken() != 8:
            print("ERROR: 'while' expected")
            return
        self.tokenizer.skipToken()
        self.cond = Cond(self.tokenizer)
        self.cond.parse_cond()
        if self.tokenizer.getToken() != 9:
            print("ERROR: 'loop' expected")
            return
        self.tokenizer.skipToken()
        self.ss = StmtSeq(self.tokenizer)
        self.ss.parse_cond()
        if self.tokenizer.getToken() != 3:
            print("ERROR: 'loop' expected")
            return
        self.tokenizer.skipToken()
        if self.tokenizer.getToken() != 12:
            print("ERROR: 'loop' expected")
            return
        self.tokenizer.skipToken()
    
    def print_loop(self):
        print("while ")
        self.cond.print_cond()
        print("loop ")
        self.ss.print_stmt_seq()
        print("end;")

    def exec_loop(self):
        while self.cond.exec_cond():
            self.ss.exec_stmt_seq()
