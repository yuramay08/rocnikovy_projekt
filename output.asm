BITS 64
section .data
    format_int db "%d", 10, 0  ; Format for printing integers with newline
section .bss
    var_0 resq 1
    var_1 resq 1
    var_2 resq 1
    var_3 resq 1
    var_4 resq 1
    var_5 resq 1
section .text
    global main
    extern printf
main:
    sub rsp, 40  ; Reserve shadow space for Windows x64 calling convention
    ; Assign to x
    mov qword [rel var_0], 10
    ; Assign to y
    mov qword [rel var_1], 20
    ; Assign to sprindel
    mov rax, 5
    sub rax, [rel var_0]
    mov [rel var_2], rax
    ; Assign to sprindel
    mov rax, [rel var_2]
    add rax, [rel var_1]
    mov [rel var_2], rax
    ; Assign to sprindel
    mov rax, [rel var_2]
    add rax, 1
    mov [rel var_2], rax
    ; Print value
    mov rdx, [rel var_5]
    lea rcx, [rel format_int]
    xor rax, rax
    call printf
    ; Print value
    mov rdx, [rel var_5]
    lea rcx, [rel format_int]
    xor rax, rax
    call printf
    ; Assign to nigga
    mov rax, 5
    add rax, 6
    mov [rel var_3], rax
    ; Print value
    mov rax, [rel var_0]
    add rax, 6
    mov [rel var_5], rax
    mov rdx, [rel var_5]
    lea rcx, [rel format_int]
    xor rax, rax
    call printf
    ; Assign to nigg
    mov qword [rel var_5], 5
    ; Print value
    mov rdx, [rel var_5]
    lea rcx, [rel format_int]
    xor rax, rax
    call printf
    ; Print value
    mov rdx, [rel var_5]
    lea rcx, [rel format_int]
    xor rax, rax
    call printf
    ; Exit program
    add rsp, 40  ; Clean up stack space
    xor rax, rax
    ret