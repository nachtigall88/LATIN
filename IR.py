#відмінювання іменників першої групи реверсивне

from random import choice

DATA_DICT = [
    ('-a', 'N, sg', 'Ab, sg', 'V, sg'),
    ('-ae', 'G, sg', 'N, pl', 'D, sg', 'V, pl'),
    ('-arum', 'G, pl'),
    ('-is', 'D, pl', 'Ab, pl'),
    ('-am', 'Ac, sg'),
    ('-as', 'Ac, pl')
]

hint_template = """|       |     sg     |     pl    |
|   N   |    -a      |    -ae    |
|   G   |    -ae     |    -arum  |
|   D   |    -ae     |    -is    |
|   Ac  |    -am     |    -as    |
|   Ab  |    -a      |    -is    |
|   V   |    -a      |    -ae    |"""


def get_random_decl(data, dict_data):
    rand_base = choice(data)
    rand_ending = choice(dict_data)
    print(rand_base[0][:-1] + rand_ending[0][1:])
    print(hint_template)

    return ''


words_list = [['lingua', 'мова'], ['causa', 'причина'], ['copia', 'запас'],
              ['natura', 'природа'], ['amica', 'подруга']]



var = ''

while var != '1':


    random_word = words_list
    random_dict = DATA_DICT
    random_decl = get_random_decl(random_word, random_dict)
    print(random_decl)
    var = input()

print('bye-bye')
