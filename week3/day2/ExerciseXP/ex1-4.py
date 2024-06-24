#🌟 Exercise 1 : Pets
# Define the Pets class to manage multiple pets
class Pets:
    def __init__(self, animals):
        # Initialize with a list of animal objects
        self.animals = animals

    def walk(self):
        # Iterate through each animal and call their walk method
        for animal in self.animals:
            print(animal.walk())

# Define the Cat class as the base class for all cats
class Cat:
    is_lazy = True

    def __init__(self, name, age):
        # Initialize with a name and age
        self.name = name
        self.age = age

    def walk(self):
        # Define the walk method for the cat
        return f'{self.name} is just walking around'

# Define the Bengal class, inheriting from Cat
class Bengal(Cat):
    def sing(self, sounds):
        # Define the sing method for the Bengal cat
        return f'{sounds}'

# Define the Chartreux class, inheriting from Cat
class Chartreux(Cat):
    def sing(self, sounds):
        # Define the sing method for the Chartreux cat
        return f'{sounds}'

# Define the Siamese class, inheriting from Cat
class Siamese(Cat):
    def sing(self, sounds):
        # Define the sing method for the Siamese cat
        return f'{sounds}'

# Create instances of each cat breed
bengal_cat = Bengal(name="Tiger", age=2)
chartreux_cat = Chartreux(name="Blue", age=3)
siamese_cat = Siamese(name="Sassy", age=1)

# Create a list of all cat instances
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Create an instance of the Pets class, passing the list of cats
sara_pets = Pets(all_cats)

# Take all the cats for a walk using the walk method
sara_pets.walk()
#####################################################################################

# 🌟 Exercise 2 : Dogs
# Define the Dog class
class Dog:
    def __init__(self, name, age, weight):
        # Initialize the dog with name, age, and weight attributes
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        # Return a string stating that the dog is barking
        return f"{self.name} is barking"

    def run_speed(self):
        # Calculate and return the dog's running speed
        return self.weight / self.age * 10

    def fight(self, other_dog):
        # Calculate the fight score for this dog
        self_score = self.run_speed() * self.weight
        # Calculate the fight score for the other dog
        other_score = other_dog.run_speed() * other_dog.weight
        # Determine the winner based on the fight scores
        if self_score > other_score:
            return f"{self.name} wins the fight against {other_dog.name}"
        elif self_score < other_score:
            return f"{other_dog.name} wins the fight against {self.name}"
        else:
            return f"The fight between {self.name} and {other_dog.name} is a tie"

# Create instances of the Dog class
dog1 = Dog(name="Buddy", age=4, weight=20)
dog2 = Dog(name="Rex", age=5, weight=25)
dog3 = Dog(name="Bella", age=3, weight=18)

# Test the methods with each dog instance
print(dog1.bark())  # Buddy is barking
print(dog2.bark())  # Rex is barking
print(dog3.bark())  # Bella is barking

print(f"{dog1.name}'s running speed is {dog1.run_speed()}")  # Buddy's running speed
print(f"{dog2.name}'s running speed is {dog2.run_speed()}")  # Rex's running speed
print(f"{dog3.name}'s running speed is {dog3.run_speed()}")  # Bella's running speed

# Test the fight method
print(dog1.fight(dog2))  # Fight between Buddy and Rex
print(dog2.fight(dog3))  # Fight between Rex and Bella
print(dog1.fight(dog3))  # Fight between Buddy and Bella
######################################################################################

#🌟 Exercise 3 : Dogs Domesticated
# pet_dog.py
from dog import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        # Initialize the parent Dog class
        super().__init__(name, age, weight)
        # Add the trained attribute, default to False
        self.trained = False

    def train(self):
        # Print the output of bark and switch trained to True
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # Print the names of all dogs playing together
        dog_names = ", ".join([dog.name for dog in args])
        print(f"{self.name} and {dog_names} all play together")

    def do_a_trick(self):
        # If trained, print a random trick
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))

# Create instances of PetDog
dog1 = PetDog(name="Buddy", age=4, weight=20)
dog2 = PetDog(name="Rex", age=5, weight=25)
dog3 = PetDog(name="Bella", age=3, weight=18)

# Train the dogs
dog1.train()

# Play with the dogs
dog1.play(dog2, dog3)

# Make the dogs do a trick
dog1.do_a_trick()
dog2.do_a_trick()  # This dog is not trained yet, so it should not do a trick
dog1.train()       # Training again just to ensure it remains trained
dog1.do_a_trick()
