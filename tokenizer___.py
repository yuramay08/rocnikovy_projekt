import re, time
from parser import Parser
# Token types


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"






# tokens = tokenize(code)
# for token in tokens:
#     print(token)
    


# parser = Parser(tokens)
# ast = parser.parse()
# print(ast)

# from asm_compiler import AsmCompiler

# compiler = AsmCompiler("output.asm")
# output_file = compiler.compile(ast)
# print(f"\nAssembly code written to {output_file}")
# print("To compile and run, use these commands:")
# print("nasm -f win64 output.asm -o output.obj")
# print("gcc output.obj -o output.exe")
# print("output.exe")