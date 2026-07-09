import csv
import random
with open ('fc25_top_100_no_rank_by_position.csv', mode='r') as file:
    csvFile=csv.DictReader(file)
    CARDS=list(csvFile)

#Intro

print('Welcome to Baller Clash.')
print('This is a game where you need fight with Computer and win the Card.')
print('Click enter to begin.')

input()


def display_card(card):
  # Display the attributes of a card
  # A card is a dictionary with several attributes

  max_chars = 0
  
  for keys in card:
    if len(keys) > max_chars:
      max_chars = len(keys)
  
  for keys in card:
    print(keys, (max_chars-len(keys))*' ', ': ', card[keys])