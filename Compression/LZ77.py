
import binascii
import zlib


def str2hex(s):
    return binascii.hexlify(s)


def hex2str(h):
    return binascii.unhexlify(h)

# input_file = 'C:/Users/smart/OneDrive/Desktop/temp.py'
# text = open(input_file, 'r').read()
# print(f'Raw size is {sys.getsizeof(text)}')


text = 'I love python'

# 9 (Z_BEST_COMPRESSION), 1 (Z_BEST_SPEED)
# bytes(str.encode(s))
# text.encode('utf-8')
compressed_data = zlib.compress(bytes(str.encode(text)), 2)
print(f'Original text is: {text}')
print(f'Original size is: {len(bytes(str.encode(text)))} bytes out')
print(f'Compressed text is: {compressed_data}')
print(f'Compressed size is: {len(compressed_data)} bytes out')

data = zlib.decompress(compressed_data)
data = str(data)

print(f'Decompressed data is: {data}')
