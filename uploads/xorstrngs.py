import base64

str1 = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"
str2 = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"

a = base64.b64decode(str1)
b = base64.b64decode(str2)

c = []
length = len(a)

i = 0
while i < length:
 c.append(chr(a[i] ^ b[i]))
 i += 1
for j in c:
    print(j,end="")