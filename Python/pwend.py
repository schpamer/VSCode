import pwnlib.util
from pwn import *

io = remote('msn.com', 80)
io.send('GET /\r\n\r\n')
io.recvline()