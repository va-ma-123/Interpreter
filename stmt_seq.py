import stmt

class StmtSeq:
    # constructor
    def __init__(self, tokenizer = None):
        self.tokenizer = tokenizer
        self.stmt = None
        self.stmt_seq = None
 
    # parse the statement sequence
    def parse_stmt_seq(self):   # Parse stmt seq     
        self.stmt = stmt.Stmt(self.tokenizer)  # create an instance of the Stmt class
        self.stmt.parse_stmt()  # Parse stmt

        # check for more stmt's
        if self.tokenizer.getToken() == 3 or self.tokenizer.getToken() == 7: 
            # 3 = end, 7 = else, if end or else is next token, this is end of stmt seq
            return
        self.stmt_seq = StmtSeq(self.tokenizer) # create an instance of the StmtSeq class
        self.stmt_seq.parse_stmt_seq() # Parse stmt seq

    # execute the statement sequence
    def exec_stmt_seq(self):
        self.stmt.exec_stmt() # Execute stmt
        if self.stmt_seq is not None: # if stmt seq is not None
            self.stmt_seq.exec_stmt_seq() # Execute stmt seq

    # pretty print the statement sequence
    def print_stmt_seq(self, indent=2): 
        self.stmt.print_stmt(indent) # pretty print stmt
        if self.stmt_seq: # if stmt seq exists
           self.stmt_seq.print_stmt_seq(indent) # pretty print stmt seq
        