# The Lempel–Ziv–Markov chain algorithm(LZMA)

import lzma


def test_round_trip():
    input_data = b'abracadabra.'
    print(f'Original text is : {input_data}')

    lzma_compressor = lzma.LZMACompressor()
    cdata = lzma_compressor.compress(input_data) + lzma_compressor.flush()
    print(f'Compressed text is : {cdata}')

    lzma_decompressor = lzma.LZMADecompressor()
    ddata = lzma_decompressor.decompress(cdata)
    print(f'Uncompressed text is : {ddata}')


test_round_trip()
