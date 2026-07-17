import csv
import random
with open ('LEV3/fc25_top_100_no_rank_by_position.csv', mode='r') as file:
    csvFile=csv.DictReader(file)
    all_cards=list(csvFile)

def display_card(card):
    max_chars=0
    for keys in card:
        if len(keys)>max_chars:
            max_chars=len(keys)
    for keys in card:
        print(keys,(max_chars-len(keys))*' ',':',card[keys])        

def determine_winner(m1, m2, order = 1):
  # Explain why this concise code is useful
  dct = {'player': m1, 'computer': m2}
  v = list(dct.values())
  k = list(dct.keys())

  if m1 == m2:
    return 'draw'
  else:
    if order == 1:
      return k[v.index(max(v))]
    else:
      return k[v.index(min(v))]
    
#Intro

print('Welcome to Baller Clash.')
print('This is a game where you need fight with Computer and win the Card.')
print('Click enter to begin.')

input()


Releventkeys=list(all_cards[0].keys())
Releventkeys=Releventkeys[3::]

random.shuffle(all_cards)
player_cards=all_cards[0::2]
computer_cards=all_cards[1::2]
table_cards=[]

chance=random.randint(0,1)

chance='Player'

mapping_dict={}

for key in Releventkeys:
  mapping_dict[key[0]] = key

game = True

while game:
    print('Players Card', len(player_cards), 'Computer card',len(computer_cards),'Table Cards',len(table_cards))
    player=player_cards.pop(0)
    Computer=computer_cards.pop(0)

    table_cards.append(player)
    table_cards.append(Computer)

    print()
    
    print('It is',chance, 'Chance now')
    print()
    print('The player cards are:')
    display_card(player)
    print()

    if chance=='Player':
        print('O = Overall, P = Physical position, D = Defending Position, S = Shooting')
        choosen_key = input("Choose a stat (O/P/S/D): ").upper()
        if choosen_key not in list(mapping_dict.keys()):
           print('Invalid input!!')
           choosen_key=random.choice(list(mapping_dict.keys()))
           
        chance=='Computer'
    elif chance=='Computer':
        choosen_key=random.choice(list(mapping_dict.keys()))   
        chance='Player'
    key_requested = mapping_dict[choosen_key]
    Value_player = player[key_requested]
    Value_Computer=Computer[key_requested]
    print('Player ', key_requested, 'is', Value_player)
    print('Computer ', key_requested, 'is', Value_Computer)
    print()
    
    winner = determine_winner(float(Value_player), float(Value_Computer))
    
    print('Player ', key_requested, 'is', Value_player)
    print('Computer ', key_requested, 'is', Value_Computer)
    print()
    print('Winner is ... ', winner)
    input()

    if winner == 'Player':
        player_cards.extend(table_cards)
        table_cards.clear()
    elif winner == 'Computer':
        computer_cards.extend(table_cards)
        table_cards.clear()

    if len(player_cards) == 0:
        print('Computer Won')
        game_over = False
    elif len(computer_cards) == 0:
        print('Player Won')
        game_over = False

        
