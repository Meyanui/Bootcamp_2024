# Challenge 1
# Ask a user for a word
  # Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
    # Make sure the letters are the keys.
    # Make sure the letters are strings.
    # Make sure the indexes are stored in a list and those lists are values.

def create_letter_index_dict(word):
    # Initialize an empty dictionary to store the letter indexes
    letter_index_dict = {}

    # Iterate over each letter in the word along with its index
    for index, letter in enumerate(word):
        # Check if the letter is already a key in the dictionary
        if letter not in letter_index_dict:
            # If not, add the letter as a key with an empty list as its value
            letter_index_dict[letter] = []
        # Append the current index to the list of indexes for this letter
        letter_index_dict[letter].append(index)
    
    return letter_index_dict

# Ask the user for a word
word = input("Please enter a word: ")

# Create the letter index dictionary for the given word
letter_index_dict = create_letter_index_dict(word)

# Print the dictionary
print("Letter index dictionary:")
print(letter_index_dict)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money 
# you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

# Define store items with prices
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

# Cash available in the wallet
wallet = "$0"

# Remove dollar sign and comma from the wallet amount and convert to integer
converted_wallet = int(wallet.replace(',', '').replace('$', ''))

# Initialize an empty list to store affordable items
affordable_items_list = []

# Iterate through the items and their prices
for item, price in items_purchase.items():
    # Remove the $ sign and commas from the price and convert to an integer
    item_price = int(price.replace(',', '').replace('$', ''))
    
    # Check if the item is affordable
    if item_price <= converted_wallet:
        affordable_items_list.append(item)

# Sort the list in alphabetical order
affordable_items_list.sort()

# Print the list of affordable items or "Nothing" if the list is empty
if not affordable_items_list:
    print("Nothing")
else:
    print(affordable_items_list)