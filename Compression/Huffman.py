
data_path = "C:/Users/smart/OneDrive/Desktop/Workspace"


class File_Helper(object):

    def __init__(self, filename, buffer_size=8):
        self.buffer = []
        self.buffer_limit = buffer_size
        self.out_file = open(filename, "wb")

    # add bit to buffer
    def write_bit(self, bit):
        self.buffer.append(bit)
        # if buffer is full (8 bits), write out as a single byte
        if len(self.buffer) == self.buffer_limit:
            # Return an array of bytes representing an integer.
            symbol = int(''.join(self.buffer), 2)\
                .to_bytes(length=self.buffer_limit//8, byteorder='big')
            self.out_file.write(symbol)
            self.buffer.clear()

    # bits = '1010101010'
    def write_bits(self, bit_stream: str):
        for bit in bit_stream:
            self.write_bit(bit)

    def flush(self):
        if len(self.buffer) == 0:
            return
        # Align bits to buffer_limit, i.e. add "0" to tail
        bits = "0" * (self.buffer_limit - len(self.buffer))
        self. write_bits(bits)
        # write number of added 0 first
        if len(bits) > 0:
            symbol = len(bits).to_bytes(
                length=self.buffer_limit // 8, byteorder='big')
            self.out_file.write(symbol)
            self.buffer.clear()


def test_buffer():
    # 23 bits
    string = "ABCD"
    zero_one_string = "010000010100001001000011010001"
    fh = File_Helper(f'{data_path}/huffman.bin', 8)
    fh.write_bits(zero_one_string )
    fh.flush()


test_buffer()




