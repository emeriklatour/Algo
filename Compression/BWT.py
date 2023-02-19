

class BWT(object):
    @classmethod
    def encode(cls, plaintext):
        # Get list of rotations of input string plaintext
        tt = plaintext * 2
        rotations = [tt[i:i + len(plaintext)] for i in range(len(plaintext))]

        # get lexicographically sorted list of t’s rotations
        sorted_rotations = sorted(rotations)
        # take the final character of every row
        # and join them together
        return ''.join(map(lambda x: x[-1], sorted_rotations))

    @classmethod
    def decode(cls, compressed_text):
        pass


def bwt_driver():
    print(BWT.encode('abaaba$'))


bwt_driver()
