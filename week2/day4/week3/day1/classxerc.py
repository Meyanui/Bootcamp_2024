# Analyse the code below. What will be the output ?
# Explain the goal of the methods
# Create a method that modifies the name of the person

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)

first_person = Person("John", 36)
first_person.show_details()
#************************************************************************************************


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Hello my name is " + self.name)

    def change_name(self, new_name):
        self.name = new_name

# Example usage
first_person = Person("John", 36)
first_person.show_details()  # Output: Hello my name is John

# Change the person's name
first_person.change_name("David")
first_person.show_details()  # Output: Hello my name is David
