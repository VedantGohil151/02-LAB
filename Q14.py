m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

total = m1 + m2 + m3
average = total / 3

if m1 == 0:
    grade1 = "Absent"
elif m1 <= 39:
    grade1 = "F"
elif m1 <= 44:
    grade1 = "P"
elif m1 <= 49:
    grade1 = "C"
elif m1 <= 54:
    grade1 = "B"
elif m1 <= 59:
    grade1 = "B+"
elif m1 <= 69:
    grade1 = "A"
elif m1 <= 79:
    grade1 = "A+"
elif m1 <= 100:
    grade1 = "O"
else:
    grade1 = "Invalid"

if m2 == 0:
    grade2 = "Absent"
elif m2 <= 39:
    grade2 = "F"
elif m2 <= 44:
    grade2 = "P"
elif m2 <= 49:
    grade2 = "C"
elif m2 <= 54:
    grade2 = "B"
elif m2 <= 59:
    grade2 = "B+"
elif m2 <= 69:
    grade2 = "A"
elif m2 <= 79:
    grade2 = "A+"
elif m2 <= 100:
    grade2 = "O"
else:
    grade2 = "Invalid"

if m3 == 0:
    grade3 = "Absent"
elif m3 <= 39:
    grade3 = "F"
elif m3 <= 44:
    grade3 = "P"
elif m3 <= 49:
    grade3 = "C"
elif m3 <= 54:
    grade3 = "B"
elif m3 <= 59:
    grade3 = "B+"
elif m3 <= 69:
    grade3 = "A"
elif m3 <= 79:
    grade3 = "A+"
elif m3 <= 100:
    grade3 = "O"
else:
    grade3 = "Invalid"

if m1 <= 39 or m2 <= 39 or m3 <= 39:
    result = "Fail"
else:
    result = "Pass"

print("Total Marks:", total)
print("Average:", average)
print("Subject 1 Grade:", grade1)
print("Subject 2 Grade:", grade2)
print("Subject 3 Grade:", grade3)
print("Result:", result)
