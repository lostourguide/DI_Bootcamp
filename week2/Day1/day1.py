#functions - reusable set operations. x() is function.
def say_hello():
    print("Hello")

say_hello()
#def - defining a function
# everything indented is part of the function body
# call fuction/invoke function - not indented. executes function
def say_hello(name):
    print(f"Hello! {name}")

say_hello("Ryan")

user_name = input("What's your name?")

say_hello(user_name)

def say_hello(username, language):
    if language == "EN":
        print("Hello" + username)
    elif language == "FR":
        print("bonjour" + username)
    else:
        print("This language is not supported" + username)
say_hello(username + language)
#if keyword arguments are present, no need perfect arrangement,no KW arrangement must follow arrangmeent
#if start KW argument, dont need KWs
#make sure same number of arguments for same arguments you want
#scope - interview question - 
def number_by_three(name, day):
  sentence = f'Hello {name}! Today is {day}.'
  print(sentence)

print(day)
#funct can look outside the funct, but argument cant look inside the book
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title() #capitalizes 1st letter in both names

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)

def doingStuff(a,b):
    print(a**2 + b**3)

    print(doingStuff(2,3))



#Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

#For example:

def calculation(a, b):
    sum = a + b
    difference = a -b

res = calculation(40, 10)
print(res)

#FUNCTIIONS
#Args
def check_arguments(*args):
    print(f"These are the arguments {args}")
check_arguments(1, 2, 'hey')
>> These are the arguments (1, 2, 'hey') // You get a tuple