name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

print("Enter marks of 5 subjects:")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n--- Student Details ---")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
