

def encrypt(plaintext, key_matrix):
    print(f'Key matrix is: {key_matrix}')
    if len(plaintext) % 2 != 0:
        plaintext += "Z"
    # split a plaintext every nth character, where n=2
    message = [plaintext[i: i + 2] for i in range(0, len(plaintext), 2)]
    ciphertext = []
    for chunk in message:
        codec = encipher(chunk, key_matrix)
        ciphertext.append(codec)
    return ''.join(ciphertext)


def encipher(message, key_matrix):
    # build the message vector
    x = [ord(message[i]) - ord('a') for i in range(len(message))]
    y = [0 for i in range(len(message))]
    y[0] = (key_matrix[0][0] * x[0] + key_matrix[0][1] * x[1]) % 26
    y[1] = (key_matrix[1][0] * x[0] + key_matrix[1][1] * x[1]) % 26
    ciphertext = []
    for i in range(len(message)):
        ciphertext.append(chr(y[i] + ord('a')))
    return "".join(ciphertext)


def decrypt(ciphertext, key_matrix):
    inv_key_matrix = inverse_keys(key_matrix)
    return encrypt(ciphertext, inv_key_matrix)


def inverse_keys(key_matrix):
    inv_key_matrix = [[0 for j in range(2)] for i in range(2)]
    inv_determinant = get_inv_determinant(key_matrix)
    inv_key_matrix[0][0] = (key_matrix[1][1] * inv_determinant) % 26

    temp = - key_matrix[0][1] * inv_determinant
    while temp < 0:
        temp = temp+26
    inv_key_matrix[0][1] = temp % 26

    temp = - key_matrix[1][0] * inv_determinant
    while temp < 0:
        temp = temp+26
    inv_key_matrix[1][0] = temp % 26

    inv_key_matrix[1][1] = (key_matrix[0][0] * inv_determinant) % 26
    return inv_key_matrix


def get_determinant(keys):
    return keys[0][0] * keys[1][1] - keys[0][1] * keys[1][0]


def get_inv_determinant(keys):
    det = get_determinant(keys)
    inv_det = 1
    while (det * inv_det) % 26 != 1:
        inv_det += 1
    return inv_det


def get_key_matrix(key_string):
    ascii_codes = [ord(c) - ord('a') for c in key_string]
    matrix_dim = int(len(ascii_codes) / 2)
    keys = [[0 for j in range(matrix_dim)] for i in range(matrix_dim)]
    k = 0
    for i in range(matrix_dim):
        for j in range(matrix_dim):
            keys[i][j] = ascii_codes[k] % 26
            k += 1
    return keys


def test_inverse_matrix():
    key_string = 'hill'
    key_matrix = get_key_matrix(key_string)
    print(key_matrix)
    inv_key_matrix = inverse_keys(key_matrix)
    print(inv_key_matrix)
    # print(np.linalg.inv(np.array(key_matrix)))
    # test_inverse_matrix()


def run():
    plaintext = 'ilovesda'
    key_string = 'hill'
    key_matrix = get_key_matrix(key_string)
    encoded = 'obgvsbiffxfc'
    print(key_matrix)
    print(f'Pattern is ----------------> {key_string}')
    print(f'Original plaintext is -----> {plaintext}')
    encoded = encrypt(plaintext, key_matrix)
    print(f'Associated ciphertext is --> {encoded}')
    decoded = decrypt(encoded, key_matrix)
    print(f'Recovered plaintext is ----> {decoded}')

run()
