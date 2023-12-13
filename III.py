#відмінювання іменників третьої групи

from random import choice

hint_template = """============================================================
|          |  consonant      | mixed           | vowel  |
|          |-----------------|-----------------|--------|
|          |   m/f  |    n   |       m/f       |   n    |
|----------|--------|--------|-----------------|--------|
|   | N.   |        |        |        |        |        |
|   | -----|--------|--------|--------|--------|--------|
|   | G.   |  -is   |  -is   |  -is   |  -is   |  -is   |
|   | -----|--------|--------|--------|--------|--------|
|Sg | D.   |  -i    |  -i    |  -i    |  -i    |  -i    |
|   | -----|--------|--------|--------|--------|--------|
|   | Ac.  |  -em   |        |  -em   |  -em   |        |
|   | -----|--------|--------|--------|--------|--------|
|   | Ab.  |  -e    |  -e    |  -e    |  -e    |  -i    |
|---| -----|--------|--------|--------|--------|--------|
|   | N.   |  -es   |  -a    |  -es   |  -es   |  -ia   |
|   | -----|--------|--------|--------|--------|--------|
|   | G.   |  -um   |  -um   |  -um   |  -um   |  -ium  |
|   | -----|--------|--------|--------|--------|--------|
|Pl | D.   |  -ibus |  -ibus |  -ibus |  -ibus |  -ibus |
|   | -----|--------|--------|--------|--------|--------|
|   | Ac.  |  -es   |  -a    |  -es   |  -es   |  -ia   |
|   | -----|--------|--------|--------|--------|--------|
|   | Ab.  |  -ibus |  -ibus |  -ibus |  -ibus |  -ibus |
|-------------------------------------------------------|
============================================================"""

decl_list = ['G, sg', 'D, sg',
             'Ac, sg', 'N, pl', 'G, pl',
             'Ac, pl', 'Ab, sg']

words_list = [['mons', 'гора', '(montis)', 'm'], ['amor', 'любов', '(amoris)', 'm'],
              ['civis', 'громадянин', '(civis)', 'm'],
              ['mare', 'море', '(maris)', 'n'], ['pars', 'частина', '(partis)', 'f'],
              ['tempus', 'час', '(temporis)', 'n'],
              ['flumen', 'ріка', '(fluminis)', 'n'], ['animal', 'тварина', '(animalis)', 'n'],
              ['exemplar', 'зразок', '(exemplaris)', 'n'],
              ['lex', 'закон', '(legis)', 'f'], ['mercator', 'торговець', '(mercatoris)', 'm'],
              ['cupiditas', 'бажання', '(cupiditatis)', 'f'], ['nobilitatus', 'знаменитість', '(nobilitatis)', 'm'],
              ['homo', 'людина', '(hominis)', 'm'],
              ['multitudo', 'множина', '(multitudinis)', 'f'], ['fortitudo', 'сила', '(fortitudinis)', 'f'],
              ['longitudo', 'довжина', '(longitudinis)', 'f'], ['virtus', 'мужність', '(virtutis)', 'f'],
              ['finis', 'кінець', '(finis)', 'm'],
              ['septentrio', 'велика ведмедиця', '(septentrionis)', 'm'], ['consul', 'консул', '(consulis)', 'm'],
              ['ratio', 'причина, пояснення', '(rationis)', 'f'], ['civitas', 'громадянин', '(civitatis)', 'f'],
              ['dolor', 'біль', '(doloris)', 'm']
              ]


def get_random_decl(data):
    var = choice(words_list)
    print(var[0], var[-2], var[-1], var[1])
    print(choice(decl_list))
    print(hint_template)
    return ''


var = ''

while var != '1':
    random_word = choice(words_list)
    random_decl = get_random_decl(random_word)
    print(random_decl)
    var = input()

print("bye-bye")
