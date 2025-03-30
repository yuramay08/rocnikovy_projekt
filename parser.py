class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        ast = []
        while not self.end_of_tokens():
            ast.append(self.parse_statement())
        return ast

    def parse_statement(self):
        token = self.peek()
        if token.value == "LET":
            return self.parse_assignment()
        elif token.value == "PRINT":
            return self.parse_print()
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def parse_assignment(self):
        # Expect LET IDENTIFIER = expression
        let_token = self.consume("KEYWORD", "LET")
        ident = self.consume("IDENTIFIER")
        eq_token = self.consume("OPERATOR", "=")
        expr = self.parse_expression()
        return ("assign", ident.value, expr)

    def parse_print(self):
        # Expect PRINT expression
        print_token = self.consume("KEYWORD", "PRINT")
        expr = self.parse_expression()
        return ("print", expr)

    def parse_expression(self):
        # Simple expression handling, e.g. NUMBER or IDENTIFIER, optionally +/-
        left_token = self.consume_any(["NUMBER","IDENTIFIER"])
        if not self.end_of_tokens() and self.peek().type == "OPERATOR":
            op_token = self.consume("OPERATOR")
            right_token = self.consume_any(["NUMBER","IDENTIFIER"])
            return ("binop", op_token.value, left_token.value, right_token.value)
        return ("literal", left_token.value)

    def consume(self, type_, value=None):
        token = self.peek()
        if token.type != type_ or (value and token.value != value):
            raise SyntaxError(f"Expected {type_}:{value}, got {token}")
        self.pos += 1
        return token

    def consume_any(self, types):
        token = self.peek()
        if token.type not in types:
            raise SyntaxError(f"Expected one of {types}, got {token}")
        self.pos += 1
        return token

    def peek(self):
        return self.tokens[self.pos]

    def end_of_tokens(self):
        return self.pos >= len(self.tokens)
