import re, time
from parser import Parser
# Token types
KEYWORDS = {"LET", "PRINT"}
TOKEN_TYPES = {
    "NUMBER": r"\d+",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "OPERATOR": r"[=+\-]",
    "WHITESPACE": r"\s+",
}

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

def tokenize(code):
    tokens = []
    #print(1)
    while code:
        #print(code)
        match = None
        for type_, pattern in TOKEN_TYPES.items():
            regex = re.match(pattern, code)
            if regex:
                match = regex.group(0)
                if type_ == "WHITESPACE":
                    "sigma"
                elif type_ == "IDENTIFIER" and match in KEYWORDS:
                    tokens.append(Token("KEYWORD", match))
                else:
                    tokens.append(Token(type_, match))
                code = code[len(match):]
                break

        if not match:
            raise SyntaxError(f"Unexpected character: {code[0]}")

    return tokens


code = """
LET x = 10
LET y = 20
LET sprindel = 5 - x
LET sprindel = sprindel + y
LET sprindel = sprindel + 1
PRINT 5
PRINT x
LET nigga = 5 + 6
PRINT x + 6
LET nigg = 5
PRINT 55
PRINT 555
"""

tokens = tokenize(code)
for token in tokens:
    print(token)
    


parser = Parser(tokens)
ast = parser.parse()
print(ast)

from asm_compiler import AsmCompiler

compiler = AsmCompiler("nigga.asm")
output_file = compiler.compile(ast)
print(f"\nAssembly code written to {output_file}")
print("To compile and run, use these commands:")
print("nasm -f win64 output.asm -o output.obj")
print("gcc output.obj -o output.exe")
print("output.exe")