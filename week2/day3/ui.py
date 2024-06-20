# Create a program that prints a list of the items you can afford in the store with the money 
# you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
# # Cash available in my wallet
# wallet = "$20"

# # Remove dollar sign and comma from the amount string
# converted_wallet = int(wallet.replace(',', '').replace('$', ''))

# # initialize an empty list to store affordable items
# affordable_items_list = []

# # iterate through the items and their prices 
# for item, price in items_purchase.items():
        
#         # Remove the $ sign and commas from the price and convert to an integer
#         Item_price = int(price.replace(',', '').replace('$', ''))

#         # Check if the item is affordable
#         if Item_price <= converted_wallet:
#             affordable_items_list.append(item)
        
#         # sort the list in alphabetical order
#         affordable_items_list.sort()

#         # print the list of affordable items or "there is nothing affordable" if the list is empty
#         if not affordable_items_list:
#             print("There is nothing affordable")
#         else:
#             print(affordable_items_list)
    

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

