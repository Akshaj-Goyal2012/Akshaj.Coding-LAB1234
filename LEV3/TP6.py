import csv
 
print('Welcome to F1 Drives...')
print('This project helps in doing comparison in F1 and Autosport... ')
print('This analysis.data for the comparison.')
 
def printline(report_line):
    file_name='analysis.data'
    with open (file_name, mode='a') as file:
        file.write(report_line)
 
def print_table(table):
  # Pass in a list of dictionaries and print it. 
  
  file_name = 'analysis.dat'
 
  with open(file_name, mode ='a') as file:
    all_keys = list(table[0].keys())
 
    keys_line = ''
    for key in all_keys:
      keys_line = keys_line + key + (20 - len(key))*' '
      
    file.write(keys_line + '\n')
 
    for data in table:
      # Each data is a dictionary, we print the values.
      values_line = ''
      for values in data.values():
        values_line = values_line + str(values) + (20-len(str(values)))*' '
 
      file.write(values_line + '\n')
 
def initialize():
  file_name = 'analysis.dat'
 
  with open(file_name, mode ='w') as file:
    file.write('Analysis Results \n') 
 
def print_set(winner_set):
  # Pass in a set and print its members one on each line. 
  file_name = 'analysis.dat'
 
  with open(file_name, mode ='a') as file:
    for winner in winner_set:
       file.write(winner + ' , ')
    file.write('\n\n')      
 
def readcsvdata(tournament_name):
  filename = tournament_name + '.csv'
  # Open the file
  # Read the data into a list of dictionaries
  with open(filename, mode ='r') as file:
    csvFile = csv.DictReader(file)
    tournament_data = list(csvFile)
 
  return tournament_data
 
def analyze(tname, tdata):
  # Create a list of winners
  winners_list = []
  
  for winner in tdata:
    winners_list.append(winner['Champion'])
 
  # Find out the unique winners (Since one player may have won the tournament more than once)
  # Easiest method -- Convert to a set
  winners_set = set(winners_list)
 
  printline('Reporting for ' + tname + '\n' )
  printline('Total Winners : ' + str(len(winners_list)) + '\n')
  printline('Unique Winners : ' + str(len(winners_set)) + '\n')
 
  winners_info_list = []  
  for player in winners_set:
    player_info = {}
    selected = [chosen for chosen in tdata if chosen['Champion'] == player]
    player_info['Name'] = player
    player_info['Country'] = selected[0]['Country']
    player_info['Times Won'] = len(selected)
    player_info['Years Won'] = []
    for kk in selected:
      player_info['Years Won'].append(kk['Year'])
 
    winners_info_list.append(player_info)
 
  print_table(winners_info_list)
  mto_winners_set = set()
 
  for player in winners_set:
    mto_winners_set.add(player)
 
  for player in winners_set:
    selected = [chosen for chosen in winners_info_list if chosen['Name'] == player]
    if selected[0]['Times Won'] == 1:
      mto_winners_set.remove(player)
 
  # NEW: print out the repeat (more-than-once) champions for this tournament
  printline('Repeat Champions in ' + tname + ' : ' + str(len(mto_winners_set)) + '\n')
  printline('These are: \n')
  print_set(mto_winners_set)
 
  return winners_set, mto_winners_set
 
 
 
 
def comparative_analysis(winner_set1, winner_set2):
 
  winners_eitheror = winner_set1 | winner_set2
  winners_both = winner_set1 & winner_set2
  winners_only1 = winner_set1 - winner_set2
  winners_only2 = winner_set2 - winner_set1
  winners_onlyone_notboth = winner_set1 ^ winner_set2
 
  printline('Winners (Either/Or): ' + str(len(winners_eitheror)) + '\n')
  printline('These are: \n')
  print_set(winners_eitheror)
  
  printline('Winners (Both): ' + str(len(winners_both)) + '\n')
  printline('These are: \n')
  print_set(winners_both)
  
  printline('Winners (Only 1, not both): ' + str(len(winners_onlyone_notboth)) + '\n')
 
  printline('These are: \n')
  print_set(winners_onlyone_notboth)
 
  
  printline('Winners (Only F1, not Autosport):'+ str(len(winners_only1)) + '\n')
  printline('These are: \n')
  print_set(winners_only1)
 
  
  printline('Winners (Only Autosprt,Not F1 ):'+ str(len(winners_only2))+'\n')
  printline('These are: \n')
  print_set(winners_only2)
  
 
      
initialize()
F1_data = readcsvdata('F1')
Autosport_data = readcsvdata('Autosport')
 
F1_winners, F1_mto_winners = analyze('F1', F1_data)
Autosport_winners, Autosport_mto_winners = analyze('Autosport', Autosport_data)
 
comparative_analysis(F1_winners, Autosport_winners)
 
