from random import choice, randint
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\\', ';', '\'', ',', '.', '/', '`', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', '~']


def gen_data(bytes):
    data = []
    for byte_count in range(bytes):
        rand_byte = choice(characters)
        data.append(rand_byte)
    return ''.join(data)


def gen_filename(names_array, extensions):
    filename = []
    for sublist_num in range(len(names_array)):
        sublist_pick = randint(0, len(names_array[sublist_num]) - 1)
        subname = names_array[sublist_num][sublist_pick]
        filename.append(subname)
    filename = '_'.join(filename)
    extension = choice(extensions)
    return f'out_files/{filename}.{extension}'


print(gen_filename([['dog', 'cat'], ['blue', 'red']], ['txt', 'png']))
print(gen_data(100))
