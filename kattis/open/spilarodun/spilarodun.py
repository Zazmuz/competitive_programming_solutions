card_types = [
    ('Skrimsli', [
        'Venjulegt',
        'Ahrifa',
        'Bodunar',
        'Samruna',
        'Samstillt',
        'Thaeo',
        'Penduls',
        'Tengis'
    ]),
    ('Galdur', ['Venjulegur',
                'Bunadar',
                'Svida',
                'Samfelldur',
                'Bodunar',
                'Hradur'
                ]),
    ('Gildra', ['Venjuleg',
                'Samfelld',
                'Mot'
                ],),]

type_order = {}
index = 0
for core_type, sub_types in card_types:
    type_order[core_type] = index
    index += 1
    for sub_type in sub_types:
        type_order[f"{core_type} - {sub_type}"] = index
        index += 1
type_order['Annad'] = index

import datetime
cards = []
for _ in range(int(input())):
    NAME, ID, TYPE, DATE = input().split(', ')
    cards.append({'name': NAME, 'id': ID, 'type': TYPE, 'date': datetime.datetime.strptime(DATE, '%Y-%m-%d')})

order = input().split()
cards2 = []
for card in cards:
    to_add = []
    for crit in order:
        if crit == 'flokkur':
            to_add.append(type_order[card['type']])
        elif crit == 'nafn':
            to_add.append(card['name'])
        elif crit == 'id':
            to_add.append(card['id'])
        elif crit == 'dagsetning':
            to_add.append(card['date'])

    cards2.append(tuple(to_add) + (card['name'],))
cards2.sort()
for card in cards2:
    print(card[-1])