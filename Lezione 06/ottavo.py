# gzip file1.txt
# genera file1.txt.gz, la versione compressa del file

# hexdump -C file1.txt.gz
# mostra in base 16 i byte del file

# 123 -> in binario -> 1111011

# 8 bit   01111011 ->hex-> 7B
# 16 bit  0000000001111011 ->hex-> 007B
# 32 bit  00000000000000000000000001111011 ->hex-> 0000007B

# 007B -> in bytes -> 1) 00 7B  big endian
#                     2) 7B 00  little endian

# AABBCCDD -> in bytes -> 1) AA BB CC DD  big endian
#                         2) DD CC BB AA  little endian

a = int.from_bytes(b'\xAA\xBB\xCC\xDD', byteorder='little', signed=False)
b = a.to_bytes(4, byteorder='little', signed=False)

with open('file1.txt.gz', 'rb') as f:
    print(f.read(1))
    print(f.read(1))
    print(f.read(1))
    print(f.read(1))
    print(f.read(1))
