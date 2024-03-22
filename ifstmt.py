from cond import Cond
import stmt_seq as StmtSeq

class If:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.cond = None
        self.ss1 = None
        self.ss2 = None

    def parse_if(self):
        if self.tokenizer.getToken() != 5:
            print("ERROR: expected 'if'")
            return
        self.tokenizer.skipToken() # skip "if"
        self.cond = Cond(self.tokenizer)
        self.cond.parse_cond()

        if self.tokenizer.getToken() != 6:
            print("ERROR: expected 'then'")
            return
        self.tokenizer.skipToken() # skip "then"

        self.ss1 = StmtSeq(self.tokenizer)
        self.ss1.parse_stmt_seq()

        if self.tokenizer.getToken() == 7:
            self.tokenizer.skipToken() # skip "else"
            self.ss2 = StmtSeq(self.tokenizer)
            self.ss2.parse_stmt_seq()
        
        if self.tokenizer.getToken() != 3:
            print("ERROR: expected 'end'")
            return
        self.tokenizer.skipToken() # skip "end"
        if self.tokenizer.getToken() != 12:
            print("ERROR: expected ';'")
            return
        self.tokenizer.skipToken() # skip ";"

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
        