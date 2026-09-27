import tkinter as tk
import random

#Screen Setup
window=tk.Tk()
window.title('Minesweeper')
window.geometry('400*400')
Nrows=9
Ncols=9

#Neighbours
def Find_Neighbours(r0,c0):
    neighbours=[]
    valid_cols=[c0-1,c0,c0+1]
    valid_rows=[r0-1,r0,r0+1]
    #Corner cells
    valid_cols=[ x for x in valid_cols if x > -1 and x < Ncols ]
    valid_rows=[ x for x in valid_rows if x > -1 and x < Nrows ]
    for r in valid_rows:
        for c in valid_cols:
            neighbours.append((r,c))

    neighbours.remove((r0,c0))
    return neighbours

colours=['white', 'blue', 'green', 'red', 'dark blue', 'brown', 'cyan', 'black', 'gray']

field = [[0 for _ in range(Ncols)] for _ in range(Nrows)]

buttons=[]

def openup(r,c):
    if buttons[r][c]['state']=='disabled':
        return

    buttons[r][c]['state']=='disabled'
    buttons[r][c].config(relief=tk.SUNKEN)

    if field[r][c]==0:
        neighbours=Find_Neighbours(r,c)
        for nn in neighbours:
            openup(nn[0],nn[1])
    else:
        buttons[r][c]['text'] = str(field[r][c])
        buttons[r][c].config(disabledforeground=colours[field[r][c]])

def click_on (r,c):
    if field[r][c]==10:
        for i in range (0,Nrows):
            for j in range(0,Ncols):
                buttons[i][j]['state']='disabled'
                buttons[i][j].config(relief=tk.SUNKEN)
                if field[i][j]==10:
                    buttons[i][j]['text']='*'
                    buttons[i][j].config(background='red',disabledforeground='black')

    elif field[r][c] !=0:  
        buttons[r][c]['state'] = 'disabled'
        buttons[r][c].config(relief=tk.SUNKEN)
        buttons[r][c]["text"] = str(field[r][c])
        buttons[r][c].config(disabledforeground=colours[field[r][c]])    

    else:
                      


        
    
                              

   