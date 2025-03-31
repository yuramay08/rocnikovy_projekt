# Simple Compiler Project
A basic compiler that translates a simple language into x86_64 assembly for Windows. This project demonstrates the fundamental concepts of lexical analysis, parsing, and code generation.

## Features
- Simple language with variable assignments and print statements
- Arithmetic operations (addition, subtraction)
- Compilation to native x86_64 assembly
- Command-line interface
## Requirements
Python 3.6 or higher
NASM (Netwide Assembler) for Windows
GCC or other C compiler (for linking)
## Installation
- Clone or download this repository
- Ensure NASM is installed and added to your PATH
- Ensure GCC is installed and added to your PATH
## Usage
- Create a source file (e.g., program.txt) with your code
- Compile and run:
```
python main.py program.txt
nasm -f win64 program.asm -o program.obj
gcc program.obj -o program.exe
program.exe
```
## Language Syntax
The language supports:
```
LET variable = expression
PRINT expression
```
Where expressions can be:
- Numbers (e.g., 123)
- Variables (e.g., x)
- Binary operations (e.g., x + 5 or 10 - y)
## Example
```
LET x = 10
LET y = 5
PRINT x
PRINT y
PRINT x + y
PRINT 100 - x
```

## How It Works
The compiler follows a standard compilation pipeline:

- Tokenization: Breaks source code into tokens
- Parsing: Builds an abstract syntax tree (AST)
- Code Generation: Translates the AST to x86_64 assembly