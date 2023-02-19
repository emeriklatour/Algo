# Hacking the Caesar Cipher with the brute-force technique
def hack_caesar(alphabet, ciphertext):
    for key in range(len(alphabet)):
        plaintext = ''
        for symbol in ciphertext:
            if symbol in alphabet:
                symbol_order = alphabet.find(symbol)
                symbol_order = symbol_order - key
                if symbol_order < 0:
                    symbol_order = symbol_order + len(alphabet)
                plaintext = plaintext + alphabet[symbol_order]
            else:
                plaintext = plaintext + symbol
        print('Key #%s: %s' % (key, plaintext))


def driver():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = '5C6 S20 QNGN FGEHPGHERF NAQ NYTBEVGUZF.'
    # Key #13: 5P6 F20 DATA STRUCTURES AND ALGORITHMS.
    hack_caesar(alphabet, ciphertext)


driver()
