

def encrypt(plaintext, key):
    cypher_text = ''
    for symbol in plaintext:
        if symbol.isalpha():
            new_code = ord(symbol)+key
            if symbol.isupper():
                if new_code > ord('Z'):
                    new_code -= 26
                elif new_code < ord('A'):
                    new_code += 26
            elif symbol.islower():
                if new_code > ord('z'):
                    new_code -= 26
                elif new_code < ord('a'):
                    new_code += 26
            cypher_text += chr(new_code)
        else:
            cypher_text += symbol
    return cypher_text


def decrypt(cipher_text, key):
    return encrypt(cipher_text, -key)


def run():
    # plaintext= 'Hide the gold in the tree stump'
    plaintext = '5P6 F20 DATA STRUCTURES AND ALGORITHMS.'
    print(f'Original plaintext is ----> {plaintext}')
    cipher_text = '5C6 S20 Qngn fgehpgherf naq nytbevguzf'
    shift_over = 13
    encoded = encrypt(plaintext, shift_over)
    print(f'Associated ciphertext is -> {encoded}')
    decoded = decrypt(encoded, shift_over)
    print(f'Recovered plaintext is ---> {decoded}')


run()
