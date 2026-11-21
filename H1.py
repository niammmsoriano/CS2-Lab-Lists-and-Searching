def find(items, target):
  for i in range(len(items)):
    if items[i] == target:
      return i
  return -1

members = []
while True:
  name = input("Member (done to stop): ")
  if name == "done":
    break
  members.append(name)

target = input("Look for: ")
index = find(members, target)

if index == -1:
  print(target, "is not a member")
if index != -1:
  print(target, "is a member")