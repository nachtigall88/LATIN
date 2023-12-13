#відмінювання іменників першої групи

from random import choice

DATA = [('N, sg', '-us'), ('G, sg', '-i'), ('D, sg', '-o'),
           ('Ac, sg', '-um'), ('Ab, sg', '-o'), ('V, sg', '-e'),
           ('N, pl', '-i'), ('G, pl', '-orum'), ('D, pl', '-is'),
           ('Ac, pl', '-os'), ('Ab, pl', '-is'), ('V, pl', '-i')]

hint_template = """|       |     sg     |     pl    |
|   N   |    -a      |    -ae    |
|   G   |    -ae     |    -arum  |
|   D   |    -ae     |    -is    |
|   Ac  |    -am     |    -as    |
|   Ab  |    -a      |    -is    |
|   V   |    -a      |    -ae    |"""


def get_random_decl(data):
    print(data[0])
    print(choice(DATA)[0])
    print(hint_template)

    return ''


words_list = [['lingua', 'мова'], ['causa', 'причина'], ['copia', 'запас'],
              ['natura', 'природа'], ['amica', 'подруга']]



var = ''

while var != '1':


    random_word = choice(words_list)
    random_decl = get_random_decl(random_word)
    print(random_decl)
    var = input()

print('bye-bye')
