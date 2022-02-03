#!/usr/bin/env python3
from random import randint
import brain_games


brain_games.main()
print ("Answer \"yes\" if the number is even, otherwise answer \"no\".")
test_num=3
test=1
if test <=test_num:
    digit=randint(1,100)
    print ("Question: "+str(digit))
    answer=prompt.string(empty=True,prompt='Your answer: ')
    print (answer)
    test+=1

         #def check_even(digit):
       #   return if digit % 2 ==0

