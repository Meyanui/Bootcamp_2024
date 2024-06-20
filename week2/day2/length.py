number = int(input("Enter your number"))
length = int(input("Enter the length in the list"))

nb = number
my_liste = []
while len(my_liste) < length:
  my_liste.append(nb)
  nb += number
print(f"\n{my_liste}\n")