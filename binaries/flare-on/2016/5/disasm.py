#!/usr/bin/env python

import struct

'''
import idaapi
import os, sys

with open('newestthing.bytes', 'wb') as ok:
	ok.write(GetManyBytes(0x40A140, 386, True))
'''

# now to deal with the bytes...

code = []

with open('vmOPcodes.bytes', 'r') as readable:
    while 1:
        byte = readable.read(2)
        if not byte:
            break
        byter = struct.unpack("<h", byte)
        code.append(byter[0])


mnem = {
    0: "push",
    1: "pop",
    2: "add",
    3: "sub",
    4: "ror",
    5: "rol",
    6: "xor",
    7: "not",
    8: "eq",
    9: "if",
    10: "br",
    11: "store",
    12: "load",
    13: "nop",
}

regs = {
    0: "r1",
    1: "r2",
    2: "sp",
    3: "pc",
}

i = 0

while i < len(code):
    opcode = code[i]
    line = "%04d: %s" % (i, mnem[opcode])
    if opcode == 0: # push
        i += 1
        val = code[i]
        line = "%s %d" % (line, val)
    elif opcode in (11, 12): # store or load
        i +=1
        reg_type = code[i]
        opnd = regs[reg_type]
        line = "%s %s" % (line, opnd)
    print line

    i += 1
