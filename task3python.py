# This is a guessing game.

import random
# this will allow options for playing and quitting the game.

# user's name
print("hello! What is your Name? ")
myName = input()
print("Hello " + str(myName) + "!" + " Let's play a guessing game!")

def random_game():

    play = True
    while play:

        easy =  random.randint(1, 10)
        medium = random.randint(1, 20)
        hard = random.randint(1, 50)
        #user gets prompted for difficulty to play on
level_selection = True
while level_selection:
    level = input("would you like to play on easy, medium, or hard?"
              "\nType 'e' for easy, 'm' for medium, or 'h' for hard!" )
    if level == "e":
               print("\nAwesome! we'll begin with easy!")
               level_selection = not True
               break
    if level == "m":
               print("\nAwesome! we'll begin with medium!")
               level_selection = not True
               break
    if level == "h":
               print("\nAwesome! we'll begin with hard!")
               level_selection = not True
               break
    else:
                print("invalid input!\nPlease enter either e, m, or h. ")

 # for number of guesses remaining
    
if level == "e":
            print("Because you selected easy, " + myName + "  you will have 6 guesses from number 1-10")
            guesses_left = 6
            while guesses_left != 0:
             easy = random.randint(1, 10)
             try1 = int(input("so, what's your guess? \n"))
             if try1 == easy:
                print("that's correct, you've guessed the right number! " + str(easy))
                print("congratulations " + str(myName) + "!" )
                break
             elif try1 < easy:
                print("Nope, not quite! Guess higher!")
             elif try1 > easy:
                print("Nope, you're a little high. Guess lower!")
             guesses_left -= 1
             print("You now have " + str(guesses_left) + " guesses left! ")

            if guesses_left == 1:
                print("you have got only one chance left!\nYou can do this!")        
# if the user runs out of guesses

            if guesses_left == 0:
                print("Game Over! Better luck next time!")

# if the user selects level 2 for medium - 4 tries
        
if level == "m":
              print("Because you selected medium, " + myName + "  you will have 4 guesses from number 1-20")
              guesses_left = 4
              while guesses_left != 0:
                 medium = random.randint(1, 20)
                 try2 = int(input(" so, what's your guess? \n"))
                 if try2 == medium:
                  print("that's correct, you've guessed the right number! " + str(medium))
                  print("congratulations " + str(myName) + "!" )
                  break
                 elif try2 < medium:
                  print("Nope, not quite! Guess higher!")
                 elif try2 > medium:
                  print("Nope, you're a little high. Guess lower!")
                  guesses_left -= 1
                  print("You now have " + str(guesses_left) + " guesses left!")

                 if guesses_left == 1:
                  print("your last try, you can do this!")

            # if the user runs out of guesses

                 if guesses_left == 0:
                  print("Game Over! Better luck next time!")

 # if the user selects level 3 for hard - 3 tries
if level == "h":
              print("Because you selected hard!, " + myName + "  you will have 3 guesses from number 1-50")
              guesses_left = 3
              while guesses_left != 0:
               hard = random.randint(1, 50)
               try1 = int(input("so, what's your guess?: \n"))
               if try1 == hard:
                print("that's correct, you've guessed the right number! " + str(hard))
                print("congratulations " + myName + "!" )
                break 
              
               elif try1 < hard:
                print("Nope, not quite! Guess higher!")
               elif try1 > hard:
                print("Nope, you're a little high. Guess lower!")
               guesses_left -= 1
               print("You now have " + str(guesses_left) + " guesses left!")
              if guesses_left == 1:
               print("your last try, you can do this!")

 # if the user runs out of guesses

              if guesses_left == 0:
               print("Game Over! Better luck next time!")

              elif level != "e" and level != "m" and level != "h":
               print("Invald input! select either 'e', 'm' or 'h' ")
            
    # to play again!

play_again = True
while play_again:
         again = input("\nWould you care to play again?\nYes or No\n ")
         if again == "No" or again == "no":
            print("\nok, thank you for playing. \nFeel free to come back again! ")
            play_again = not True
            play = not True
         elif again == "yes" or again == "Yes":
            print("\nCool, Let's play again!\n")
            play_again = not True
            play = True
         else:
            print("please enter either yes or no.")
            input()
            play_again = not True
            play = not True
 