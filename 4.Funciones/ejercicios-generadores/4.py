def my_generator(word):
    my_dict = {}
    for letter in word:
        my_dict[letter] = word.count(letter)
        yield my_dict


for x in my_generator('humanidad'):
    print(x)