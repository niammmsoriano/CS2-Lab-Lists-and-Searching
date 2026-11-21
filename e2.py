names = []
n = int(input("How many names? "))
for i in range(n):
    name = input("Name: ")
    names.append(name)
print(names)
print(len(names), "names stored")