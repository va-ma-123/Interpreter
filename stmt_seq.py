from stmt import Stmt

class StmtSeq:
    def __init__(self, tokenizer): # <stmt seq>	::= <stmt> | <stmt> <stmt seq>
        self.tokenizer = tokenizer
        self.stmt = None
        self.stmt_seq = None

    def parse_stmt_seq(self):   # Parse stmt seq     
        stmt = Stmt(self.tokenizer) 
        stmt.parse_stmt() 

        # check for more stmt's
        if self.tokenizer.getToken() == 3 or self.tokenizer.getToken() == 7:
            # 3 = end, 7 = else, if end or else is next token, this is end of stmt seq
            return
        self.stmt_seq = StmtSeq(self.tokenizer)

    def print_stmt_seq(self):
        self.stmt.print_stmt()
        if self.stmt_seq is not None:
           self.stmt_seq.print_stmt_seq()

    def exec_stmt_seq(self):
        self.stmt.exec_stmt()
        if self.stmt_seq is not None:
            self.stmt_seq.exec_stmt_seq()
        