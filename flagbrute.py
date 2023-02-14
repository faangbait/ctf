#!/usr/bin/env python

s = "lactf{000000000000001l0000_000000000t}"
bytes = bytearray()
bytes.extend(map(ord,s))

bytes[0] = ord('l')
bytes[1] = ord('a')
bytes[2] = ord('c')
bytes[3] = ord('t')
bytes[4] = ord('f')
bytes[5] = ord('{')
bytes[6] = ord('.')
bytes[7] = ord('.')
bytes[8] = ord('d')
bytes[9] = ord('0')
bytes[10] = ord('n')
bytes[11] = ord('.')
bytes[12] = ord('_')
bytes[13] = ord('s')
bytes[14] = ord('e')
bytes[15] = ord('e')
bytes[16] = ord('_')
bytes[17] = ord('3')
bytes[18] = ord('_')
bytes[19] = ord('b')
bytes[20] = ord('1')
bytes[21] = ord('l')
bytes[22] = ord('l')
bytes[23] = ord('1')
bytes[24] = ord('0')
bytes[25] = ord('n')
bytes[26] = ord('_')
bytes[27] = ord('s')
bytes[28] = ord('0')
bytes[29] = ord('l')
bytes[30] = ord('v')
bytes[31] = ord('3')
bytes[32] = ord('s')
bytes[33] = ord('_')
bytes[34] = ord('y')
bytes[35] = ord('3')
bytes[36] = ord('t')
bytes[37] = ord('}')


ins = (24, 9, 17, 0xB9)

brute=2

while ((bytes[ins[0]] ^ bytes[ins[1]] * 7 ^ ~bytes[ins[2]] + 13) & 0xFF) != ins[3]:
    bytes[ins[brute]] = bytes[ins[brute]]+1
    print(f"testing {chr(bytes[ins[brute]])}")

if (bytes[ins[0]] ^ bytes[ins[1]] * 7 ^ ~bytes[ins[2]] + 13) & 0xFF == ins[3]:
    print(f"{ins[brute]} === {chr(bytes[ins[brute]])}")
    print(f"{bytes}")
else:
    print("errr not found")
