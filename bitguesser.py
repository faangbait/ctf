#!/usr/bin/env python
import pwn

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


def solve(n,a,c):
    if c%a == 0:
        if is_square(c):
            return b'0'
        else:
            return b'1'
    return b'0'

pwn.context(arch = 'amd64', os = 'linux')

r = pwn.remote('lac.tf', 31190)
exec(r.recvline().strip()) #n 
exec(r.recvline().strip()) #a
exec(r.recvline().strip()) #c
print(n)
print(a)
print(c)
r.recvuntil(b'What is your guess?', drop=True)
r.sendline(solve(n,a,c))
for _ in range(149):
    
    new = r.recvline().strip()
    r.recvuntil(b'What is your guess?', drop=True)
    print(new)
    exec(new)
    r.sendline(solve(n,a,c))

r.interactive()
