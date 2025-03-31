import time
class AsmCompiler:
    def __init__(self, target_file="output.asm"):
        # print("__init__")
        self.target_file = target_file
        self.output = []
        self.variables = {}
        self.var_counter = 0

    def compile(self, ast):
        # Clear previous output
        self.output = []

        # Setup assembly file structure
        self.output.extend([
            "BITS 64",
            "section .data",
            "    format_int db \"%d\", 10, 0  ; Format for printing integers with newline",
            "section .bss",
        ])

        isVariable = False
        # Identify all variables
        for node in ast:
            if node[0] == "assign":
                isVariable = True
                var_name = node[1]
                if var_name not in self.variables:
                    self.variables[var_name] = f"var_{self.var_counter}"
                    self.output.append(f"    {self.variables[var_name]} resq 1")
                    self.var_counter += 1
        if isVariable:
            yeet = self.variables[var_name]
            self.variables[var_name] = f"var_{self.var_counter}"
            self.output.append(f"    {self.variables[var_name]} resq 1") #reserve for PRINT's
            self.variables[var_name] = yeet
        else:
            self.output.append(f"    var_0 resq 1")

        # Start code section
        self.output.extend([
            
            "section .text",
            "    global main",
            "    extern printf",
            "main:",
            "    sub rsp, 40  ; Reserve shadow space for Windows x64 calling convention"
        ])
        
        # Process each AST node
        for node in ast:
            self.compile_node(node)
            
        # Add exit code
        self.output.extend([
            "    ; Exit program",
            "    add rsp, 40  ; Clean up stack space",
            "    xor rax, rax",
            "    ret"
        ])
            
        # Write the output to a file
        with open(self.target_file, "w") as f:
            f.write("\n".join(self.output))
            
        return self.target_file
    
    def compile_node(self, node):
        node_type = node[0]
        
        if node_type == "assign":
            var_name = node[1]
            self.output.append(f"    ; Assign to {var_name}")
            self.compile_expression(node[2], var_name)
            
        elif node_type == "print":
            self.output.append("    ; Print value")
            target_var = self.compile_expression(node[1])
            self.output.extend([
                f"    mov rdx, [rel {target_var}]",  # Second arg in rdx for Windows
                "    lea rcx, [rel format_int]",     # First arg in rcx for Windows
                "    xor rax, rax",
                "    call printf"
            ])
    
    def compile_expression(self, expr, target=None):
        expr_type = expr[0]
        
        if expr_type == "literal":
            value = expr[1]
            if target:  # If we have a target, store directly there
                self.output.append(f"    mov qword [rel {self.variables.get(target, target)}], {value}")
                return self.variables.get(target, target)
            else:  # Otherwise create a temp variable
                temp_var = f"var_{self.var_counter}"
                if str(value) in self.variables:
                    return self.variables[str(value)]
                self.output.append(f"    mov qword [rel {temp_var}], {value}")
                return temp_var
                
        elif expr_type == "binop":
            op = expr[1]
            left = expr[2]
            right = expr[3]
            
            # Handle variable references
            if left in self.variables:
                left_var = self.variables[left]
                self.output.append(f"    mov rax, [rel {left_var}]")
            else:
                self.output.append(f"    mov rax, {left}")
                
            if right in self.variables:
                right_var = self.variables[right]
                if op == "+":
                    self.output.append(f"    add rax, [rel {right_var}]")
                elif op == "-":
                    self.output.append(f"    sub rax, [rel {right_var}]")
            else:
                if op == "+":
                    self.output.append(f"    add rax, {right}")
                elif op == "-":
                    self.output.append(f"    sub rax, {right}")
            
            # Store result in target variable
            target_var = self.variables.get(target, target) if target else f"var_{self.var_counter}"
            self.output.append(f"    mov [rel {target_var}], rax")
            
            return target_var