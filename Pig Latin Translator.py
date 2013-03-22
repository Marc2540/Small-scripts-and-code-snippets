#Created in python 3.3.0
#Created by Marc2540, guide from codeacademy.com

pyg = 'ay'
original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  #print original  #debugging
  word = original.lower()
  first = word[0]
  if word[0] in ['a','e','i','o','u']:
    #print ('vowel')  #debugging
    new_word=original + pyg
    print (new_word)
  else:
      #print ('consonant')  #debugging
      new_word=word[1:]+word[0]+pyg
      print (new_word)
else:
  print ('Try again, you wrote something invalid.')
