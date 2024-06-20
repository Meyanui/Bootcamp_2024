# Access the value of key "history"
# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict["class"]["student"]["marks"]["history"])

# # To modify a value
# sample_dict["class"]["student"]["marks"]["history"] = 120

# # add an entry to an exixting .....
# sample_dict["class"]["student"]["marks"]["Chemistry"] = 90
# print(sample_dict)

# # Delete an entry from an exixting .....
# del sample_dict["class"]["student"]["marks"]["physics"] 
# print(sample_dict)


# BUild in methods
# rick_dict = {
#     'first_name':'Rick',
#     'last_name':'Sanchez'
# }
# print(rick_dict.values())

# Exercise
# Delete set of keys from Python Dictionary

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# print(sample_dict)

# del sample_dict["name"]
# print(sample_dict)

# del sample_dict["salary"]
# print(sample_dict)
#**********************************************************

# Advanced List, Dictionaries And Loops

my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for x, y in my_books.items():
    print(" the " + x + " is " + y)

# Enumerate(Iterable) : Enumerate Each Item In The Iterable
for item in enumerate('abcd'):
    print(item)

#SETS AND DICTIONARY COMPREHENSION
# to capitalize
name = {"tom", "james", "anna", "john"}
names = {n.capitalize() for n in name}
print(f"\n {names} \n")

# Making each key and value of the dict tripple
d1 = {"a":1, 'b':2, 'c':3}
d2 = {k*3 : v*3 for k,v in d1.items()}
print(d2)

# Modify the key only
d3 = {k.upper(): v*2 for k, v in d1.items()}
print(d3)
