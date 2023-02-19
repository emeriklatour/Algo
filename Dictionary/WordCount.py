
input_file = 'D:\\GDrive\\F20\\5P6.SDA\\TD\\SDAF20TD\\src\\datasets\\input_file.txt'
freq = {}
for token in open(input_file).read().lower().split():
    # only consider alphabetic characters within this piece
    word = ''.join(c for c in token if c.isalpha())  #select c from token where c is alpha
    # print(f'Adding {word} ')
    if word:  # require at least one alphabetic character
        freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0
for (word, count) in freq.items():
    # (key, value) tuples represent (word, count)
    if count > max_count:
        max_word = word
        max_count = count
print(f'The most frequent word is {max_word}')
print(f'Its number of occurrences is {max_count}')

