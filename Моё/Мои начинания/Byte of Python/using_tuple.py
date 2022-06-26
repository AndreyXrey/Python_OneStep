zoo = ("Python", "Elephant", "Penguin") # следует помпить, что скобки необязательны
print("Quantity of animals in zoo - ", len(zoo))

new_zoo = "Monkey", "Caml", zoo
print("Quantity of cages or sells -", len(new_zoo))
print("All animals are in new zoo:", new_zoo)
print("Animals delivered from old zoo", new_zoo[2])
print("The last animal delivered from old zoo-", new_zoo[2][2])
print("Quantity of animals in new zoo -", len(new_zoo)-1+len(new_zoo[2]))

print(1,2,3)
print((1,2,3))
myEmpty = ()
singleton = (2,)
print(myEmpty, singleton)
