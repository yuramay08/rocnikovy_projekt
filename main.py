import re, time, sys
from tokenizer___ import Token
from parser import Parser
from asm_compiler import AsmCompiler

KEYWORDS = {"LET", "PRINT"}
TOKEN_TYPES = {
    "NUMBER": r"\d+",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "OPERATOR": r"[=+\-]",
    "WHITESPACE": r"\s+",
}

def tokenize(code):
    tokens = []
    while code:
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

def main():
    # Check if a filename is provided as command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        return
    
    # Read from the file
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    
    # Compile the code
    tokens = tokenize(code)
    # for token in tokens:
    #     print(token)
    
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)
    
    output_name = filename.split('.')[0] + ".asm"
    compiler = AsmCompiler(output_name)
    output_file = compiler.compile(ast)
    
    print(f"\nAssembly code written to {output_file}")
    print("To compile and run, use these commands:")
    print(f"nasm -f win64 {output_file} -o {output_file.replace('.asm', '.obj')}")
    print(f"gcc {output_file.replace('.asm', '.obj')} -o {output_file.replace('.asm', '.exe')}")
    print(f"{output_file.replace('.asm', '.exe')}")
    print("*You might need to install nasm and gcc from external source first.")

if __name__ == "__main__":
    main()