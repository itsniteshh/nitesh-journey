# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
counter = 0

for h in student_heights:
    total_height += h
    counter += 1

avg_height = total_height / counter
print(avg_height)


