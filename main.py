student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_students = 0
for height in student_heights:
  total_students += height
print(total_students)

number_student = 0
for student in student_heights:  
  number_student += 1
print(number_student)

average = round(total_students/number_student)
print(average)
  