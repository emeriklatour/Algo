# Hacking the Caesar Cipher with the frequency analysis technique

english_letter_frequency = [8.167, 1.492, 2.782,
                            4.253, 12.702, 2.228,
                            2.015, 6.094, 6.966,
                            0.153, 0.772, 4.025,
                            2.406, 6.749, 7.507,
                            1.929, 0.095, 5.987,
                            6.327, 9.056, 2.758,
                            0.978, 2.360, 0.150,
                            1.974, 0.074]


# Normalised frequency table
# return frequency of [A, B, C, ..., Z]
def get_letter_frequency(ciphertext):
    symbol_frequency = [0] * 26
    for symbol in ciphertext:
        if symbol.isalpha():
            symbol_frequency[ord(symbol) - ord('A')] += 1
    total = sum(symbol_frequency)
    # Normalize frequencies
    for i in range(0, len(symbol_frequency)):
        symbol_frequency[i] /= (float(total) / 100)
    return symbol_frequency


# Calculates a weighted score for a given shift value
def shift_score(letter_frequency, shift):
    score = 0
    for i in range(0, 26):
        shiftIndex = (i + shift) % 26
        score += abs(letter_frequency[i] - english_letter_frequency[shiftIndex])
    return score / 26


# Calculates the most likely shift value for a substring
# by comparing weighted scores of different shift values
def guess_shift(letter_frequency):
    bestGuess = ''
    bestGuessVal = float('inf')
    for shift in range(1, 27):
        score = shift_score(letter_frequency, shift)
        if score < bestGuessVal:
            bestGuessVal = score
            bestGuess = 26 - shift
    return bestGuess


def caesar(plaintext, shift):
    return "".join(chr(((ord(char) - 65 + shift) % 26) + 65)
                   if not char.isspace() else " " for char in plaintext)


def hack_caesar(ciphertext):
    shift = guess_shift(get_letter_frequency(ciphertext))
    print(f"Guessed shift is : {shift} ({chr(shift + ord('A') - 1)})")
    return caesar(ciphertext, -shift)


def guess():
    ciphertext = 'QNGN FGEHPGHERF NAQ NYTBEVGUZF'
    # Key #13: 5P6 F20 DATA STRUCTURES AND ALGORITHMS.
    # hack_caesar(alphabet, ciphertext)
    shift = guess_shift(get_letter_frequency(ciphertext))
    print(f'Ciphertext is: {ciphertext}')
    print(f'Plaintext is : {hack_caesar(ciphertext)}')


guess()
