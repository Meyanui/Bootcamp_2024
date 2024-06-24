# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# # Instantiate three Cat (Creating the 3 cats)
# cat1 = Cat("Whiskers", 2)
# cat2 = Cat("Mittens", 3)
# cat3 = Cat("Shadow", 4) 
# 
# # Print details of the cats to verify
# print(f"Cat 1: Name = {cat1.name}, Age = {cat1.age}")
# print(f"Cat 2: Name = {cat2.name}, Age = {cat2.age}")
# print(f"Cat 3: Name = {cat3.name}, Age = {cat3.age}")

# # OR ********************

cat1 = Cat(cat_name = "Minou", cat_age= 2)
cat2 = Cat(cat_name = "Shamba", cat_age= 8)
cat3 = Cat(cat_name = "Dimba", cat_age= 6)

cats = [cat1, cat2, cat3]

# create a function to find the oldest cat
def find_oldest_cat(cats):
    oldest_cat = max(cats, key = lambda cat: cat.age)
    return oldest_cat

oldest_cat = find_oldest_cat(cats)
print(f"\nThe oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old \n")
#****************************************************************************************************
# 🌟 Exercise 2 : Dogs
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!!")
    

    # Create an object for David's dog
davids_dog = Dog(name="Rex", height=50)

# Print details and call methods for David's dog
print(f"\nDavid's dog: Name = {davids_dog.name}\n ")
print(f"David's dog: height = {davids_dog.height} \n")

davids_dog.bark()
davids_dog.jump()

# Create an and display an object for Sarah's dog
sarahs_dog = Dog(name = "Teacup", height= 20)
print(f"Sarahs dog: Name = {sarahs_dog.name} \n")
print(f"Sarahs dog: Height = {sarahs_dog.height} \n")

#Calling the bark and Jump methods
sarahs_dog.bark()
sarahs_dog.jump()

# Do a comparison to check the bigger dog
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the biggest dog ")
else:
    print(f"{sarahs_dog.name} is the biggest dog")


# 🌟 Exercise 3 : Who’s The Song Producer?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example: stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

our_song = [
    "There’s a lady who's sure", 
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
    ]

#To create object of the song class
new_song = Song(our_song)

 #to call the class
new_song.sing_me_a_song()


#Exercise 4 : Afternoon At The Zoo
class Zoo:
    def __init__(self, zoo_name):
        # Initialize the zoo with a name and an empty list for animals
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        # Add the new animal to the list if it isn't already present
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        # Print all animals in the zoo
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        # Remove the animal from the list if it exists
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        # Sort animals alphabetically and group them by their first letter
        self.animals.sort()
        self.animal_groups = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in self.animal_groups:
                self.animal_groups[first_letter] = [animal]
            else:
                self.animal_groups[first_letter].append(animal)
        # Convert the dictionary to the required format with integer keys
        self.animal_groups = {i+1: group for i, group in enumerate(self.animal_groups.values())}

    def get_groups(self):
        # Print the animals in each group
        print("Animal groups:")
        for key, group in self.animal_groups.items():
            print(f"{key}: {group}")

# Create a Zoo object named "Ramat Gan Safari"
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Add animals to the zoo
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Eel")
ramat_gan_safari.add_animal("Emu")

# Print the animals in the zoo
ramat_gan_safari.get_animals()

# Remove an animal from the zoo
ramat_gan_safari.sell_animal("Giraffe")

# Sort the animals into groups
ramat_gan_safari.sort_animals()

# Print the animal groups
ramat_gan_safari.get_groups()
