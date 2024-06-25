class Farm:
    def __init__(self, name):
        # Initialize the farm with a name and an empty dictionary for animals
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        # Update the count if the animal already exists otherwise, add it
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        # Create the header with the farm name
        info = f"{self.name}'s farm\n\n"
        # Add each animal and its count to the result string
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
         
        return info
##########################################################################################
#EXPANDING THE ANIMAL TYPE

    def get_animal_types(self):
        # Return a sorted list of all animal types in the farm
        return sorted(self.animals.keys())

    def get_short_info(self):
        # Get a sorted list of animal types
        animal_types = self.get_animal_types()
        # Create a list of pluralized animal names
        pluralized_animals = [animal + 's' if self.animals[animal] > 1 else animal for animal in animal_types]
        # Join the animal names with commas, with 'and' before the last item
        if len(pluralized_animals) > 1:
            animals_str = ', '.join(pluralized_animals[:-1]) + ' and ' + pluralized_animals[-1]
        else:
            animals_str = pluralized_animals[0]
        # Construct the final short info string
        return f"{self.name}'s farm has {animals_str}."

# Create a Farm object named "McDonald"
macdonald = Farm("McDonald")

# Add animals to the farm
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Print the farm information
print(macdonald.get_info())

# Get and print the sorted list of animal types
print(macdonald.get_animal_types())

# Get and print the short info about the farm
print(macdonald.get_short_info())
