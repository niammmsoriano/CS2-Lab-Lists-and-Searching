quizscores = []

for i in range(5):
    quiz = int(input("Score: "))
    quizscores.append(quiz)

total = 0
for quiz in quizscores:
    total = total + quiz

average = total / 5
print("Total:", total)
print("Average:", average)