names = []

for i in range(5):
    name = input("Name: ")
    names.append(name)

nametofind = input("Look for? ")

found = False
for name in names:
  if name == nametofind:
    found = True

if found:
  print(nametofind, "Is on the list")
else:
  print (nametofind, "Is not on the list") 