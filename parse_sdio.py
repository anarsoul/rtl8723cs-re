#!/usr/bin/env python

import re
import sys
from registers import registers

sdio_pattern = '.*sdio_(read|write)(b|w|l): ([0-9a-f]+)=([0-9a-f]+).*'

def decode_reg(op, size, addr, data):
    reg_addr = addr & ~0x10000
    if reg_addr in registers.keys():
        print(f"sdio_{op}{size} {registers[reg_addr]} = {data:x}")
        return

    if reg_addr >= 0x1000 and reg_addr < 0x2000:
        print(f"sdio_{op}{size} FWDL_{reg_addr - 0x1000:04x} = {data:08x}")
        return

    for key in registers.keys():
        if (key & 3) == 0 and reg_addr > key and (reg_addr - key) <= 3:
            print(f"sdio_{op}{size} {registers[key]}+{reg_addr-key} = {data:x}")
            return

    print(f"sdio_{op}{size} {addr:08x} = {data:x}")


def decode(op, size, addr, data):
    if addr & 0x10000:
        decode_reg(op, size, addr, data)
    else:
        print(f"sdio_{op}{size} {addr:08x} = {data:x}")

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} filaname")
    sys.exit(1)

with open(sys.argv[1]) as file:
    for line in file:
        match = re.match(sdio_pattern, line)
        if match:
            decode(match[1], match[2], int(match[3], 16), int(match[4], 16))
