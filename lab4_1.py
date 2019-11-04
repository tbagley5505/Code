def is_even():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input('Please give me an integer.'))
   out = None
   
   # Create a conditional that sets out to True if the user enters
   # an even integer and False if the user enters an odd integer.
   if user_data%2 == 0 :
      print('user_data is even')
   else :
      print('user_data is odd')

   # This is for the test.
   return out 

def multi_condition():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input('Please give me an integer.'))
   if user_data == 0:
      print ('Do not be such a zero!')
   elif user_data < 0:
      print('Negative Nelly!') 
   else:
      if user_data % 2 == 0:
         print('Positively odd!')  
      else:
         print('Even Steven!')
    

   # Now evaluate the user_data again and have several conditions
   # if the value is zero, print "Don't be such a zero!"
   # if the value is positive and odd, print "Positively odd!"
   # if the value is positive and even, print "Even Steven!"
   # if the value is negative and odd or even, print "Negative Nelly!"
   # remember, with multiple conditions you can use if, elif, elif, else
   
   return None


def is_underage():

   # Prompt the user for their age and store it to a variable. Don't
   # forget to convert the input to an integer.
   is_underage = int(input('What is your age?/n'))
   print(is_underage)   


   # Set up a conditional with four cases
   # if the age is equal to or above 21, 
   # print "You may drink, smoke, and drive if you wish!"
   # if the age is equal to or above 18 but less than 21, 
   # print "You may smoke and drive!"
   # if the age is equal to or above 16 but less than 18,
   # print "You may drive!"
   # if the age is less than 16, 
   # print "Enjoy your bike, kid!"
def is_underage(): 
   is_underage = int(input('What is your age?/n'))
      if is_underage >= 21
         print('you may drink, smoke, and drive if you wish!')
      elif is_underage >= 18
         print('You may smoke and drive!')
      elif is_underage >= 16
         print('you may drive!')
      else is_underage > 16
         print('Enjoy your bike and the buss kid!')
   # So the tests fail and they don't throw errors
   return None

def countdown():
   
   # Use a loop to print a countdown from 10 to zero with
   # one number on each new line. If you do not use a loop
   # you will not get points for this problem.
   n = 10
   while n > 0:
      print(n)
      n = n - 1
   Print('none')
   # So the tests fail and they don't throw errors
   return None

def guessing_game(num):
   # This is a guessing game. I have set up a parameter that will be
   # a random integer that your user will have to try to guess.
   # To use num in your condition, you should write something like
   # 
   # if user_input == num: 
   #    
   # You should give your user at most 10 guesses to guess
   # the number. If the guess is too high or too low, you should tell 
   # them "Too High!" or "Too Low!" with the print statement.
   # If they guess the number, you should tell them "You win!"
   # otherwise, if they run out of guesses, tell them, "You lose!"
   # If they want to, your condition should also check for "q" and 
   # if the user enters that the program should exit, saying 
   # "Goodbye, quitter!"
   # No, it's not a very nice program. 
   num = int(input('what is your guess?'))
      if user_input == num:
         print('winner winner chicken Dinner!!')
      elif user_input == q
         print('Goodbye, Quitter!')
      n = 10
   while n > 0:
      elif user_input >= num
         print('too low!')
      elif user_input >= num
         print('too high!')
       n = n - 1
       Print('game over')
   # So the tests fail and they don't throw errors
   return None