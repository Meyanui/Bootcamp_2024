#Defining a simple function
def greet_typhon():
  print("Hello students")

greet_typhon() # Its function is only to print "Hello students"
#*********************************************************************************

#parameters with Functions
def greet_typhon(username):
  print(f"Hello dear student, {username.upper()}")

greet_typhon("alex") # It replaces "username" with ALEX
greet_typhon("meyanui") # It replaces "username" with Meyanui - 2nd call, etc
#************************************************************************************

#Functions with multi parameters
def display_course(course_topic, course_name, course_hours):
  # """Display info about the course"""
  print(f"\nCourse Topic : {course_topic}")
  print(f"\nCourse Name : {course_name}")
  print(f"\nCourse Hours : {course_hours} Hours")
display_course("Logarithmes", "The fast and easy way", 4)
#************************************************************************************

#Returning variables in Functions
def get_car_info(car_maker, car_model, car_year):
  #Return full car info
  car_info = f"\nCAR INFO : {car_maker.upper()} {car_model.title()} {car_year}"
  return car_info

bmw = get_car_info("bmw", "528i", 2016)
print(bmw)
volvo = get_car_info("volvo", "s40", 2014)
print(f"My Volvo is Super {volvo}")
#*************************************************************************************
#*************************************************************************************

# A Function That Accept More Than One Argument
def say_hello(username, language):
    if language == "EN":
        print("Hello "+username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello("Rick", "FR")
#**************************************************************************

#Exercise - class
# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

def calculation(a, b):
  addition = a + b
  subtraction = a - b
  return addition, subtraction
sum, difference = calculation(20, 5)
print(f"addition: {sum}, subtraction: {difference}")



