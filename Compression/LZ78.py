

class LZ78(object):

    @classmethod
    def compress(cls, uncompressed):
        # dict(key=sequence, value=code)
        code_book = {}
        compressed = []
        sequence_code = 1
        sequence = ''
        for symbol in uncompressed:
            sequence = sequence + symbol
            if sequence not in code_book:
                known_sequence = sequence[:-1]
                if len(known_sequence) == 0:
                    compressed_sequence = sequence
                else:
                    compressed_sequence = \
                        str(code_book[known_sequence])+symbol
                compressed.append(compressed_sequence)
                code_book[sequence] = sequence_code
                sequence_code += 1
                sequence = ''
        return ''.join(compressed), code_book

    @classmethod
    def decompress(cls, compressed):
        # dict(key=code, value=sequence)
        code_book = {}
        uncompressed = []
        sequence_code = 1
        while len(compressed) > 0:
            code, token, compressed = cls.extract_next_token(compressed)
            if len(code) > 0:
                sequence = code_book[int(code)]+token
                code_book[sequence_code] = sequence
                sequence_code += 1
                uncompressed.append(sequence)
            else:
                for symbol in token:
                    code_book[sequence_code] = symbol
                    sequence_code += 1
                    uncompressed.append(symbol)
            code = code
        return ''.join(uncompressed), code_book

    @classmethod
    def extract_next_token(cls, sequence):
        i = 0
        # find code
        while sequence[i].isdigit():
            i += 1
        code = sequence[0:i]
        # find token
        j = i
        while j <= len(sequence)-1:
            if sequence[j].isdigit():
                break
            else:
                j += 1
        token = sequence[i:j]
        sequence = sequence[j:]
        return code, token, sequence


def app_driver():
    # original_text = 'TOBEORNOTTOBE'
    original_text = 'AABABBABBAABA'
    # original_text = 'abracadabra'

    compressed_text, code_book = LZ78.compress(original_text)
    print(f'Original text is : {original_text} --> Compressed text is: {compressed_text}')
    print(f'Code book is: {code_book}')

    decompressed_text, recovered_code_book = LZ78.decompress(compressed_text)
    print(f'Compressed text is: {compressed_text} --> Original text is : {decompressed_text}')
    print(f'Code book is: {recovered_code_book}')


app_driver()

