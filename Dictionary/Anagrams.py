import requests

link = 'http://google.com/datasets/dictionary.txt'
input_file = requests.get(link)
input_text = input_file.text

# local_file = 'D:\\GDrive\\F20\\5P6.SDA\\TD\\SDAF20TD\\src\\datasets\\anagrams.txt'
# input_text = open(local_file, 'r').read()


def sort_string(string):
    # tokens = list(string)
    return ''.join(sorted(string))


anagrams = dict()

for word in input_text.split():
    sorted_word = sort_string(word)
    if sorted_word not in anagrams:
        anagrams[sorted_word] = [word]
    else:
        anagrams[sorted_word].append(word)

for key in anagrams.keys():
    print(f'Key={key}, Value={anagrams[key]}')

