import csv
import random
with open ('fc25_top_100_no_rank_by_position.csv', mode='r') as file:
    csvFile=csv.DictReader(file)
    CARDS=list(csvFile)