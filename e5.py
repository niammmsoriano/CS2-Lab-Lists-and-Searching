names = []
n = int(input("How many fruits? "))
for i in range(n):
    name = input("fruit: ")
    names.append(name)
print(names)
print(len(names), "fruits stored")