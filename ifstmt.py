from cond import Cond
from globals import tokenizer

class If:
    def __init__(self):
        self.cond = None
        self.ss1 = None
        self.ss2 = None

    def parse_if(self):
        from stmt_seq import StmtSeq
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

    def print_if(self):
        print("if", end=" ")
        self.cond.print_cond()
        print("then", end=" ")
        self.ss1.print_stmt_seq()
        if self.ss2 is not None:
            print("else", end=" ")
            self.ss2.print_stmt_seq()
        print("end;")

    def exec_if(self):
        if self.cond.exec_cond():
            self.ss1.exec_stmt_seq()
            return
        if self.ss2 is not None:
            self.ss2.exec_stmt_seq()
            return
        