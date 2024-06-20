my_name = "Jack"
hello = "Hello World"
my_age = 27

my_list = [my_name, my_age, hello]
my_tuples = (my_name, my_age, hello)
# print(my_list[0:3]) # to print all elements in my_list
# print(my_list[0:2]) # to print first & second elements in my_list

# to modify an element in the my_list
# my_list[0] = 1500
# print("\nMy new list is ", my_list)

# to remove an element in the my_list
# my_list.remove(my_age) # or my_list.pop() to remove the last element from the list
# print("\nMy new list is ", my_list)

# # to remove my_age from the list
# my_list.pop(1)

# # adding an element to a list
# my_list.append("Josmingo is a student")
# print("\nMy new list is ", my_list)

# adding two lists
# list_1 = ["Dauda", "James", "Edwin" ]
# list_2 = ["Dembele", "Loic", "Timol" ]
# # list_sum = list_1 + list_2
# print(list_1 + list_2)

# Given this list:
# list1 = [5, 10, 15, 20, 25, 50, 20]
# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
# Hint : Look at the index method

# Solution
list1 = [5, 10, 15, 20, 25, 50, 20]

# Check if 20 is in the list
if 20 in list1:
    # Find the index of the first occurrence of 20
    nouvelle_valeur = list1.index(20)
    print(nouvelle_valeur)

    # Replace the first occurrence of 20 with 200
    list1[nouvelle_valeur] = 200

    # print(list1)


# Unpack the following tuple into 4 variables
# a_tuple = (10, 20, 30, 40)

my_tuple = (10, 20, 30, 40)
m, n, o, p = my_tuple

print(o)
print(m)


