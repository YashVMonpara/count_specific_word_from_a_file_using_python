file_path = r'text.txt'
total_words = 0

with open(file_path, 'r') as file:
    data = file.read().lower()
    word = 'google'
    clean_data = data.replace('.', ' ').replace(',', ' ')
    splitted_list = clean_data.split(' ')
    for w in splitted_list:
        if w == word:
            total_words += 1
        else:
            pass
    print(total_words)

#You can also use python's inbuilt function count()
