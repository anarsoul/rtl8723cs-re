#!/usr/bin/env python

import re
import sys
from registers import registers

sdio_pattern = '.*sdio_(read|write)(b|w|l): ([0-9a-f]+)=([0-9a-f]+).*'

HMEBOX_REGS = [0x01D0, 0x01D4, 0x01D8, 0x01DC]
HMEBOX_EX_REGS = [0x01F0, 0x01F4, 0x01F8, 0x01FC]

hmebox_ex = None

def parse_h2c(op, size, addr, data):
    global hmebox_ex
    if size != 'l' or op != 'write':
        return False

    reg_addr = addr & ~0x10000
    if reg_addr in HMEBOX_REGS and hmebox_ex:
        print(f"H2C (CMD:{data & 0xff:02x}) HMEBOX = {data:08x}, HMEBOX_EX = {hmebox_ex[1]:08x}\t\t# {reg_addr:04x} {hmebox_ex[0]:04x}")
        hmebox_ex = None
        return True

    if reg_addr in HMEBOX_EX_REGS:
        hmebox_ex = [reg_addr, data]
        #print(f"HMEBOX_EX = {data:08x}\t\t# {reg_addr:04x}")
        return True

    return False


def decode_reg(op, size, addr, data):
    reg_addr = addr & ~0x10000

    if parse_h2c(op, size, addr, data):
        return

    if reg_addr in registers.keys():
        print(f"sdio_{op}{size}\t{registers[reg_addr]} = {data:x}\t\t# {reg_addr:04x}")
        return

    if reg_addr >= 0x1000 and reg_addr < 0x2000:
        print(f"sdio_{op}{size}\tFWDL_{reg_addr - 0x1000:04x} = {data:08x}")
        return

    for key in registers.keys():
        if (key & 3) == 0 and reg_addr > key and (reg_addr - key) <= 3:
            print(f"sdio_{op}{size}\t{registers[key]}+{reg_addr-key} = {data:x}\t\t# {reg_addr:04x}")
            return

    print(f"sdio_{op}{size}\t{addr:08x} = {data:x}")


def decode(op, size, addr, data):
    if addr & 0x10000:
        decode_reg(op, size, addr, data)
    else:
        print(f"sdio_{op}{size}\t{addr:08x} = {data:x}")

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} filaname")
    sys.exit(1)

with open(sys.argv[1]) as file:
    for line in file:
        match = re.match(sdio_pattern, line)
        if match:
            decode(match[1], match[2], int(match[3], 16), int(match[4], 16))
        else:
            print(line.replace('\n', ''))
