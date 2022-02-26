from random import *

randomNum=randint(1,10)
chances=15
guess=0
while chances>10:
     print("random",randomNum)
     guess=int(input("Guess goes here"))
     print("guess",guess)
    
     if guess==randomNum:
          print("Winner!")
          exit
     else:
          print("Incorrect")
          chances=chances-1
          if guess>randomNum:
               print("The answer is lower")
          if randomNum>guess:
               print("The answer is higher")

print("Lose.","The answer was",randomNum)
