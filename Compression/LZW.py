# https://asecuritysite.com/comms/lz
# pseudo-code of compression and decompression
# https://marknelson.us/posts/2011/11/08/lzw-revisited.html

class LZW(object):

    @classmethod
    def compress(cls, uncompressed):
        # Build the dictionary.
        dict_size = 256
        code_book = {chr(i): chr(i) for i in range(dict_size)}
        previous = uncompressed[0]
        compressed_text = []
        for current in uncompressed[1:]:
            pc = previous + current
            if pc in code_book:
                previous = pc
            else:
                code_book[pc] = dict_size
                dict_size += 1
                compressed_text.append(code_book[previous])
                previous = current
        if previous:
            compressed_text.append(code_book[previous])
        return compressed_text, code_book

    @classmethod
    def decompress(cls, compressed):
        dict_size = 256
        code_book = dict((chr(i), chr(i)) for i in range(dict_size))
        old = uncompressed_text = compressed.pop(0)
        for new in compressed:
            if new in code_book:
                Sequence = code_book[new]
            else:
                Sequence = old + old[0]
            uncompressed_text += Sequence
            code_book[dict_size] = old + Sequence[0]
            dict_size += 1
            old = Sequence
        return uncompressed_text


def copy(source_dic, start):
    target_dic = {}
    i = 0
    for key in source_dic:
        i += 1
        if i > start:
            target_dic[key] = source_dic[key]
    return target_dic


def app_driver():
    # to compare : https://asecuritysite.com/comms/lz
    # original_text = 'TOBEORNOTTOBEORTOBEORNOT'
    # original_text = 'BABAABAAAA'
    original_text = 'abracadabra'
    # original_text = 'Cows graze in groves on grass which grows in grooves in groves'

    compressed_text, code_book = LZW.compress(original_text)
    print(f'Original text is   :  {original_text}')
    print(f'Compressed text is :  {compressed_text}')

    limited_code_book = copy(source_dic=code_book, start=256)
    print(f'Code Book is       : {limited_code_book}')

    uncompressed_text = LZW.decompress(compressed_text)
    print(f'Uncompressed text is: {uncompressed_text}')


app_driver()
