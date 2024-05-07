from pwn import *

# all green, fmt string exploit 100%, or crypto problem?, xoring with 0x30

x = "y\x17FU\x10S_]U\x10XUBU\x10D_:"

payload = b"I've come here to\n"

p = process('./chall_09')

p.sendline(payload)

p.interactive()