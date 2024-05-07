from pwn import *

p = process('./chall_12')

p.recvuntil(b'ond: ')

leak = int(p.recvline().decode('utf-8').strip(), 16)

#no GOT, no BOF