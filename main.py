from random import choice, randint

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\\', ';', '\'', ',', '.', '/', '`', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?', '~']


def gen_data(size):
    data = []
    for x in range(size):
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


def gen_file(names_array, extensions, size_range, count):
    used_names = []
    for i in range(count):
        while True:
            name = gen_filename(names_array, extensions)
            if not(name in used_names):
                used_names.append(name)
                break
        size = randint(size_range[0], size_range[1])
        data = gen_data(size)
        out_file = open(name, 'w+')
        out_file.write(data)
        out_file.close


'''
#===== Example =====

names_array = [['blue', 'red', 'green', 'yellow'],
               ['Tim', 'John', 'Aaron'], ['hello', 'goodbye']]

file_types = ['txt', 'docx', 'odt', 'doc', 'png', 'jpg', 'mp3', 'mp4']

file_size = 1000000

file_count = 5


gen_file(names_array, file_types, file_size, file_count)

#===== Enjoy! =====

'''
