import random
import time
import datetime as dt

print('I know that you are lazy')
print("That's why made Readme.md")
class BadTimeError(Exception):
  pass

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
    except TypeError as e:
       print('Wrong data type. Not good at identifying data types properly.')
       print('Please try again.')
    except BadTimeError as e:
      print('Your time is not auspicious. Please try again...')

    except IndentationError as e:
       print('Mistake in Indentation. Not good at typing code.')      
       print('Please try again')

    except IndexError as e:
       print('Facing an Index error. Stop accessing an index that is not even in the code.')
       print('Please try again')

    except Exception as e:
       print('Something went wrong please try again')   

    else:
      return final

    finally:
      ('Hope you pass the test....')

strength = {'name':10, 'surname':20, 'nickname': 30, 'alias': 40, 'aka':50} 

def name_strength(**fullname):
  result = 0
  try:
    for key, value in fullname.items():
      result += strength[key]*len(value)
  except KeyError as e:
    print('Perhaps you are giving too many fields', e)
  else: 
    return result
    
def validate(**prelimdata):
  try:
    assert prelimdata['sc'] != None
    assert prelimdata['ns'] != None
  except KeyError as e:
    print('You are really bad at typing, aren\'t you?')
    print('Validation failed due to ', e)
  except AssertionError:
    print('One of the earlier steps has gone wrong.')
    print('Validation failed')
  else:
    print('Looking good so far ...')
    print('Sending for deeper validation')
    print('opening connection to a remote server ...')
    try:
      # parameters based on your luck
      deep_validate(prelimdata)
    except ValueError:
      print('There is something deeply wrong')
      print('Validation failed ...')
    else:
      print('Congrats ... Validation Successful')
      print('Welcome to my world!')
    finally:
      print('Closing connection to the remote server')

def deep_validate(prelimdata):
  print(prelimdata)

  threshold_ns = random.randint(1, 200)
  threshold_sc = random.randint(10, 20)

  print()
  print(threshold_ns, threshold_sc)
  print()

  bad_letters=['a','e','i','o','u']
  ct=dt.datetime.now()
  if ct.second % 2==0:
    raise BadTimeError
  
  if prelimdata['ns'] > threshold_ns or len(prelimdata['sc']) > threshold_sc:
    raise ValueError


print('Welcome to the Programmers\' Den')
print("I hear you have been learning Python")
print('Guess you can use the command line to create your own welcome kit')

print()

print('The process is simple, create a short code, check your name strength and then validate')


print('For short code, use sc = short_form(idx, a few words about youself, prefix = , suffix = ')

print('For name strength code, use ns = name_strength(name =, surname = , aka = , alias = , salutation = ')

print('For validate, use validate (sc = sc, ns = ns)')

print('Alright champ, get going ...')






print(' ')
