import random
import time

def short_forms(idx,*names,**addons):
    final=''
    try:
      for name in names:
        final=final+name[idx]

      for keys in addons:
         if keys == 'Prefix':
            final = addons[keys]+name
         elif keys == 'Suffix':
            final= name+addons[keys]
         else:
            print('You are not a coder who can"t understand python language') 
    except:
          
       

