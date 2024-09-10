def defines_rhyme(list_1):
    dict_1 = {}
    for word in list_1:
        dict_1[word] = vowel(word)
    first_value = dict_1[next(iter(dict_1))]
    for key, value in dict_1.items():
        if value != first_value:
            return 'Пам парам'
    return 'Парам пам-пам'


def vowel(word):
    vowels = 'аеёиоуыэюя'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


poem = list(input('Введите фразу: ').lower().split())
print(defines_rhyme(poem))