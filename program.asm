BITS 64
section .data
    format_int db "%d", 10, 0  ; Format for printing integers with newline
section .bss
    var_0 resq 1
    var_1 resq 1
section .text
    global main
    extern printf
main:
    sub rsp, 40  ; Reserve shadow space for Windows x64 calling convention
    ; Assign to x
    mov qword [rel var_0], 70
    ; Print value
    mov rdx, [rel var_0]
    lea rcx, [rel format_int]
    xor rax, rax
    call printf
    ; Print value
    mov qword [rel var_1], 100
    mov rdx, [rel var_1]
    lea rcx, [rel format_int]
    xor rax, rax
    call printf
    ; Print value
    mov rax, 80
    sub rax, [rel var_0]
    mov [rel var_1], rax
    mov rdx, [rel var_1]
    lea rcx, [rel format_int]
    xor rax, rax
    call printf
    ; Exit program
    add rsp, 40  ; Clean up stack space
    xor rax, rax
    ret