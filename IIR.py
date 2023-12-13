#відмінювання іменників другої групи реверсивне

from random import choice

DATA_US = [('N, sg', '-us', 'us'), ('G, sg', '-i', 'us'), ('D, sg', '-o', 'us'),
           ('Ac, sg', '-um', 'us'), ('Ab, sg', '-o', 'us'), ('V, sg', '-e', 'us'),
           ('N, pl', '-i', 'us'), ('G, pl', '-orum', 'us'), ('D, pl', '-is', 'us'),
           ('Ac, pl', '-os', 'us'), ('Ab, pl', '-is', 'us'), ('V, pl', '-i', 'us')]

DATA_ER = [('N, sg', '-er', 'er'), ('G, sg', '-i', 'er'), ('D, sg', '-o', 'er'),
           ('Ac, sg', '-um', 'er'), ('Ab, sg', '-o', 'er'), ('V, sg', '-a', 'er'),
           ('N, pl', '-i', 'er'), ('G, pl', '-orum', 'er'), ('D, pl', '-is', 'er'),
           ('Ac, pl', '-os', 'er'), ('Ab, pl', '-is', 'er'), ('V, pl', '-i', 'er')]

DATA_UM = [('N, sg', '-a', 'um'), ('G, sg', '-i', 'um'), ('D, sg', '-o', 'um'),
           ('Ac, sg', '-om', 'um'), ('Ab, sg', '-o', 'um'), ('V, sg', '-um', 'um'),
           ('N, pl', '-a', 'um'), ('G, pl', '-orum', 'um'), ('D, pl', '-is', 'um'),
           ('Ac, pl', '-a', 'um'), ('Ab, pl', '-is', 'um'), ('V, pl', '-a', 'um')]

hint_template_us = """|       |     sg     |     pl    |
|   N   |    -us     |    -i     |
|   G   |    -i      |    -orum  |
|   D   |    -o      |    -is    |
|   Ac  |    -um     |    -os    |
|   Ab  |    -o      |    -is    |
|   V   |    -e      |    -i     |"""

hint_template_er = """|       |     sg     |     pl    |
|   N   |    -er     |    -i     |
|   G   |    -i      |    -orum  |
|   D   |    -o      |    -is    |
|   Ac  |    -um     |    -os    |
|   Ab  |    -o      |    -is    |
|   V   |    -er     |    -i     |"""

hint_template_um = """|       |     sg     |     pl    |
|   N   |    -um     |    -a     |
|   G   |    -i      |    -orum  |
|   D   |    -o      |    -is    |
|   Ac  |    -um     |    -a     |
|   Ab  |    -o      |    -is    |
|   V   |    -um     |    -a     |"""


def get_random_decl(data):
    ending = data[0][-2:]

    if ending == 'us':
        rand_end = choice(DATA_US)[1]
        print(data[0][:-2] + rand_end[1:])
        # print(choice(DATA_US)[0])
        print(hint_template_us)
    elif ending == 'er':
        rand_end = choice(DATA_ER)[1]
        print(data[0][:-2] + 'r' + rand_end[1:])
        # print(choice(DATA_ER)[0])
        print(hint_template_er)
    elif ending == 'um':
        rand_end = choice(DATA_UM)[1]
        print(data[0][:-2] + rand_end[1:])
        # print(choice(DATA_UM)[0])
        print(hint_template_um)
    return ''


words_list = [['animus', 'душа', 'us'], ['initium', 'початок', 'um'], ['imperium', 'влада', 'um'],
              ['bellum', 'війна', 'um'], ['ager', 'поле', 'um']]

var = ''

while var != '1':
    random_word = choice(words_list)
    random_decl = get_random_decl(random_word)
    print(random_decl)
    var = input()

print("bye-bye")
