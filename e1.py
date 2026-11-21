names = []
n = int(input("How many snacks? "))
for i in range(n):
    name = input("Snack: ")
    names.append(name)
print(names)
print(len(names), "snacks stored")