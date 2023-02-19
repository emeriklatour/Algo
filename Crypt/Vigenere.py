
def encrypt_letter(plaintext_letter, pattern_letter):
    return chr(((ord(pattern_letter) + ord(plaintext_letter)
                 - 2 * ord('A')) % 26) + ord('A'))


def encrypt(plaintext, pattern):
    ciphertext = []
    for i in range(len(plaintext)):
        pattern_letter = pattern[i % len(pattern)]
        plaintext_letter = plaintext[i]
        new_letter = encrypt_letter(plaintext_letter, pattern_letter)
        ciphertext.append(new_letter)
    return "".join(ciphertext)


def decrypt_letter(cross_letter, pattern_letter):
    return chr(((ord(cross_letter) - ord(pattern_letter)
                 - 2 * ord('A')) % 26) + ord('A'))


def decrypt(ciphertext, pattern):
    original_text = []
    for i in range(len(ciphertext)):
        pattern_letter = pattern[i % len(pattern)]
        plaintext_letter = ciphertext[i]
        new_letter = decrypt_letter(plaintext_letter, pattern_letter)
        original_text.append(new_letter)
    return "".join(original_text)


def run():
    plaintext = 'ILOVEPYTHON'
    pattern = 'COLVAL'
    ciphertext = 'ILOVEPYTHON'
    print(f'Pattern is ----------------> {pattern}')
    print(f'Original plaintext is -----> {plaintext}')
    encoded = encrypt(plaintext, pattern)
    print(f'Associated ciphertext is --> {encoded}')
    decoded = decrypt(encoded, pattern)
    print(f'Recovered plaintext is ----> {decoded}')


run()


