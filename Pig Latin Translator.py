#Created in python 3.0.3
#Created by Marc2540, guide from codeacademy.com

pyg = 'ay'
original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  #print original  #debugging
  word = original.lower()
  first = word[0]
  if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
    #print ('vowel')  #debugging
    new_word=original + pyg
    print (new_word)
  else:
      #print ('consonant')  #debugging
      new_word=word[1:]+word[0]+pyg
      print (new_word)
else:
  print ('Try again, you wrote something invalid.')
