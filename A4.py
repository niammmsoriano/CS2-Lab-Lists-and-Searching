quizscores = []

for i in range(5):
    quiz = int(input("Score: "))
    quizscores.append(quiz)

highest = quizscores[0]
for quizscores in quizscores:
  if quizscores > highest:
    highest = quizscores
print("Highest:", highest)