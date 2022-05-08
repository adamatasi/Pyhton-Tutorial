#!/bin/python3

#Importing
import sys #system functions and parameters
from datetime import datetime #print(datetime.now())
#from datetime import datetime as AT ###print(AT.now())
import pyfiglet # This used for the banner - to download 'pip3 install pyfiglet'

#Nice banner using your name
my_name = pyfiglet.figlet_format("Adam Atasi", font = "slant")
print(my_name)

#Print a string
print("Strings and things:")
print('Hello, world!')
print("""Hello, this is
amulti-line string!""")
print("This is" + "a string")

print('########################################################')
print('\n') #new line
print('########################################################')

#Maths
print("Math time")
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 // 6) #number without leftovcer ex: 8.0 = 8

print('########################################################')
print('\n') #new line
print('########################################################')

#Varibales & Methods
print("Varibales and Methods")
quote = "All is fair in love and war"
print(len(quote)) #Length
print(quote.upper()) #Uppercase
print(quote.lower()) #Lowercase
print(quote.title()) #title (Capitalize the first letter of each word)

name = "Adam"
age = 29 #int int(29)
gpa = 3.7 #flaot float(3.7)

print(int(age))
print(int(29.9)) #Does not round
print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('########################################################')
print('\n') #new line
print('########################################################')

#Functions
print("Now, some functions:")
def who_am_i():
	name = "Adam"
	age = 29
	print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()

#adding in parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(50)

#add in multiple parameters
def add(x,y):
	print(x + y)

add(7,7)
add(305,207)

#Using return
def multipy(x,y):
	return x * y

print(multipy(7,7))

def square_root(x):
	return x ** .5

print(square_root(64))

print('########################################################')
print('\n') #new line
print('########################################################')

#Boolean expressions (True or False)
print("Boolean expressions:")
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

bool6 = 9
print(type(bool6))

#Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7<= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (5 < 7) #True and True = True
test_or = (7 > 5) or (5 < 7) # True or True = True
test_not = not True # not True = False

print(test_and, test_or, test_not)

print('########################################################')
print('\n') #new line
print('########################################################')

#Conditinal Statements
print("Conditinal Statements:")
def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "No soda for you!"

print(soda(3))
print(soda(1))

#More difficult one
def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "You can get alcohol (True Statement)"
	elif (age >= 21) and (money < 5):
		return "Come back with more money!"
	elif (age < 21) and (money >= 5):
		return "You are too young"
	else:
		return "You're too young and too poor"

print(alcohol(23,6))
print(alcohol(22,4))
print(alcohol(18,7))
print(alcohol(20,3))

print('########################################################')
print('\n') #new line
print('########################################################')

#Lists
print("Lists have brackets:")
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a wallflower", "The Exorcist"]

print(movies[0])
print(movies[1])
print(movies[2])
print(movies[3])
print('\n') #new line
print(movies[0:1])
print(movies[0:2])
print(movies[0:3])
print(movies[0:4])
print('\n') #new line
print(movies[0:])
print(movies[1:])
print(movies[2:])
print(movies[3:])
print('\n') #new line
print(movies[:0])
print(movies[:1])
print(movies[:2])
print(movies[:3])
print('\n') #new line
print(movies[-0])
print(movies[-1])
print(movies[-2])
print(movies[-3])
print('\n') #new line
print(len(movies))
print('\n') #new line
movies.append("Cards") #add a movie to the list
print(movies)
print('\n') #new line
movies.pop() #remove item from the list (The last item)
print(movies)
movies.pop(1) #remove a specific item from the list
print(movies)

print('\n') #new line
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a wallflower", "The Exorcist"]
person = ["Heath", "Adam", "Jake", "Jeff"]
combined = zip(movies, person)
print(list(combined))

print('########################################################')
print('\n') #new line
print('########################################################')

#Tuples
print("Tuples have parantheses and cannot change")
grades = ("A", "B", "C", "D", "F") #Tuples are static (cannot change 'add or remove')
print(grades[1])

print('########################################################')
print('\n') #new line
print('########################################################')

#Looping
print("For loops - start to finish of iterate:")
vegetables = ["cucumber", "spinach", "cabbage", "tomatos"]
for x in vegetables:
	print(x)

print('\n') #new line
print("While loops - Execute as long as True:")
a = 1
while a < 10:
	print(a)
	a += 1

print('\n') #new line
b = 2
while b <= 10:
	print(b)
	b += 1

print('\n') #new line
c = 2
while c <= 10:
	print(c)
	c += 2

print('########################################################')
print('########################################################')
print('########################################################')
print('########################################################')
print('########################################################')
print('########################################################')
print('########################################################')
print('########################################################')
print('########################################################')
print('########################################################')

# Define the new line
def new_line():
	print('\n')

new_line()

#Advanced Strings
print("Advanced Strings:")
my_name = "Adam"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

new_line()

sentence = "This is a sentence."
print(sentence[:4]) #first word
print(sentence[-9:]) #last word with the period (.)
print(sentence[-9:-1]) #last word without the period (.)

new_line()

print(sentence.split()) #split sentence by delimiter (space)
#another way
sentence_split = sentence.split()
print(sentence_split)

new_line()

sentence_join = ' '.join(sentence_split)
print(sentence_join)

print('\n'.join(sentence_split))

new_line()

quoteception = "I said, 'give me all the money'"
print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

new_line()

#Advanced Boolean
print("A" in "Apple") #True
print("c" in "Apple") #False
#1
letter = "A"
word = "Apple"
print(letter in word) #True
#2
letter = "a"
word = "Apple"
print(letter in word) #False
#3
letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) #True "Improved - case insensitive"

new_line()

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower())) 
     #(letter.lower() in word.lower() 'True'   (letter.lower() in word_two.lower() 'False'
     # True not Flase = True

new_line()

#Removing Spaces
too_much_space = "                 Hello                 "
print(too_much_space.strip())

new_line()

#Replacing
full_name = "dam Atasi" #but my name is Adam...!
print(full_name.replace("dam", "Adam")) #This will return "Adam Atasi"

new_line()

#Find position of a word 'Where does it start'
#Trying to find where my last name occurs
print(full_name.find("Atasi")) #This will return 4

new_line()

#Cool thing
mov = "The hangover"
print("My favourite movie is {}.".format(mov)) #This will add the movie name inside {}

new_line()

def favourite_book(title, author):
	fav = "My favourite book is \"{}\", which is written by {}.".format(title, author)
	return fav

print(favourite_book("The Great Gatsby", "F. Scott Fitzgerald"))

print('########################################################')
new_line()
print('########################################################')

#Dictionaries
print("Dictionaries are keys and values:")

#Lists [] - Tuples () - Dictionaries {}

drinks = {"White Russians": 7, "Old Fashion": 10, "Lemon Drop": 8, "Buttery Nipple": 6}
								#drink is key, price is value
print(drinks)

new_line()

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"],
"HR": ["Jimmy", "Mark"]}
print(employees)

new_line()

employees['Legal'] = ["Mr. Frond"] #add a new key: value pair
print(employees)

new_line()

employees.update({"Sales": ["Andie", "Olive"]}) #add a new key: value pair (this time using 'update')
print(employees)

new_line()

#Will go back to 'drinks'.
#lets say there is an update on the price
#say the price of White Russians has changed from 7 to 8
drinks["White Russians"] = 8
print(drinks) # Now the price has been updated

new_line()

#Lets say we want to know the price of the 'White Russians'
print(drinks.get("White Russians")) #This will return 8 not 7 OK?
#We can also use
print(drinks["White Russians"])

new_line()

#Lets say we call a drink that is not exist
print(drinks.get("Martini")) #This will return 'None'

new_line()

#List and Dictionaries (Compained)
movs = ["When Harry Met Sally", "The Hangover", "The Perks of Being a wallflower", "The Exorcist"]
people = ["Heath", "Adam", "Jake", "Jeff"]

combined_2 = zip(movs, people)
movie_dictionary = {key: value for key, value in combined_2} #We put them in a dictionary instead of a list
#We actually added two lists into a dictionary
print(movie_dictionary)

new_line()
print('########################################################')
new_line()
print('########################################################')
new_line()



#Color texts
import os

# System call
os.system("")

# Class of different styles
class style():
	Color_RESET		= '\033[0m'
	Color_BOLD 		= '\033[1m'
	Color_ITALIC   	= '\033[3m'
	Color_URL      	= '\033[4m'
	Color_BLINK    	= '\033[5m'
	Color_BLINK2   	= '\033[6m'
	Color_SELECTED 	= '\033[7m'

	Color_BLACK  	= '\033[30m'
	Color_RED    	= '\033[31m'
	Color_GREEN  	= '\033[32m'
	Color_YELLOW 	= '\033[33m'
	Color_BLUE   	= '\033[34m'
	Color_VIOLET 	= '\033[35m'
	Color_BEIGE  	= '\033[36m'
	Color_WHITE  	= '\033[37m'

	Color_BLACKBG  	= '\033[40m'
	Color_REDBG    	= '\033[41m'
	Color_GREENBG  	= '\033[42m'
	Color_YELLOWBG 	= '\033[43m'
	Color_BLUEBG   	= '\033[44m'
	Color_VIOLETBG 	= '\033[45m'
	Color_BEIGEBG  	= '\033[46m'
	Color_WHITEBG  	= '\033[47m'

	Color_GREY    	= '\033[90m'
	Color_RED2    	= '\033[91m'
	Color_GREEN2  	= '\033[92m'
	Color_YELLOW2 	= '\033[93m'
	Color_BLUE2   	= '\033[94m'
	Color_VIOLET2 	= '\033[95m'
	Color_BEIGE2  	= '\033[96m'
	Color_WHITE2  	= '\033[97m'

	Color_GREYBG    = '\033[100m'
	Color_REDBG2    = '\033[101m'
	Color_GREENBG2  = '\033[102m'
	Color_YELLOWBG2 = '\033[103m'
	Color_BLUEBG2   = '\033[104m'
	Color_VIOLETBG2 = '\033[105m'
	Color_BEIGEBG2  = '\033[106m'
	Color_WHITEBG2  = '\033[107m'

print(style.Color_WHITEBG2 + style.Color_RED + "Colors time" + style.Color_RESET)
print(style.Color_GREEN + "Adam Atasi" + style.Color_RESET)


print('########################################################')
print('########################################################')
print('########################################################')
print('########################################################')