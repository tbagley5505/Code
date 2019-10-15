def sums():
   
   #TODO: Initialize a variable called first_sum and store the sum of 
   # 2 and 2
   first_sum = 2 + 2
   print(first_sum)
   #TODO: Store to first_sum the value of first_sum times 10
   print(first_sum * 10)
   #TODO: Initialize a variable called secret and assign it the value 
   # of first_sum plus 2
   secret = (first_sum + 2)
   return secret

def string_manip(first_name):

   # TODO: Initialize a variable called name and assign it the 
   # parameter.
   name = 'Tom'
   # TODO: Use builtin string functions and slices to replace None with 
   # the appropriate manipulation of your name. I've done the first one.
   all_caps = name.upper('name')
   all_lowercase =('name')
   first_five_letters =('tom')
   last_two_letters =('om')
   return [all_caps, all_lowercase, first_five_letters, last_two_letters]

def greeter_bot():

   # TODO: Use the input() function to prompt the user for their name.
   # Then assign the value to a variable called name and print a greeting.
   # I have started it for you, but you need to modify the input and 
   # print functions.
   # Hint: to get the test to pass, the greeting should be "Hello, input name"
   fname = input()
   fname = 'tom'
   print('Hello, fname')

def temp_calculator(unit):

   # TODO: Write code that prompts the user for a temperature in degrees
   # celsius and prints the equivalent temperature in degrees fahrenheit.
   # The formula is C = (F - 32) * (5/9). 
   unit = unit.lower()
   if unit == "c":
      temp = 9.0 / 5.0 * temp + 32
      return "%s degrees Fahrenheit"% tep
   if unit == "f":
      temp = (temp - 32)  / 9.0 * 5.0
      return "%s degrees Celsius"% temp

   intemp = int(raw_input("What is the temperature?\n"))
   inunit = str(raw_input("Please enter the unit of measure (f or c):\n"))
   print convert(intemp, inunit)
def equitable_bill_splitter():
   
   # TODO: Read the following code and add comments to each line explaining what
   # it does. To write a comment, begin the line with an octothorpe (hashtag, #)
   #How many people are paying? (imput by user)
   people = int(input("How many people are paying? "))
   #Total number of Salaries
   salaries = []
   #total
   total = 0
   # The code uses total plus 1 to ask the user for each salary
   # index zero based aray of salaries
   for i in range(people):
      sal = int(input("What is the salary of person {}?".format(i+1)))
      total += sal
      salaries.append(sal)
   #Total bill based on user imput
   total_bill = int(input("How much is the bill? "))
   # The math to figure out how much everyone should pay based on imputs
   for j in range(len(salaries)):
      print("Person {} should pay ${}\n".format(j + 1, round((total_bill * (salaries[j]/total)), 2)))
