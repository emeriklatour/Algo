
class RunLengthEncoding(object):

    @classmethod
    def encode(cls, uncompressed):
        if not uncompressed:
            return ''
        encoded = ''
        previous_char = uncompressed[0]
        count = 1
        for char in uncompressed[1:len(uncompressed)]:
            if char != previous_char:
                encoded += str(count) + previous_char
                count = 1
                previous_char = char
            else:
                count += 1
        encoded += str(count) + previous_char
        return encoded

    @classmethod
    def decode(cls, compressed):
        decode = ''
        count = ''
        for char in compressed:
            if char.isdigit():
                count += char
            else:
                decode += char * int(count)
                count = ''
        return decode


def app_driver():
    original_message = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
    encoded_message = RunLengthEncoding.encode(original_message)
    decoded_message = RunLengthEncoding.decode(encoded_message)
    print(f'{original_message} --> {encoded_message}')
    print(f'{encoded_message} --> {decoded_message}')


app_driver()
