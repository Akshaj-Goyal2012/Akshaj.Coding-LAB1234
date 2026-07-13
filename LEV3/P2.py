import csv
import random
with open ('LEV3/fc25_top_100_no_rank_by_position.csv', mode='r') as file:
    csvFile=csv.DictReader(file)
    all_cards=list(csvFile)

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

if chance ==0:
    chance='Player'
else:
    chance='Computer'

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
    


 
 