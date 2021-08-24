import struct
import bitstring
i = 1024
# s0为一个字符串，长度为4，即占四个字节，这样方便传输与保存二进制数据。
s0 = struct.pack(">I", i)
print(s0)
i2 = struct.unpack(">I",s0)
print(i2)