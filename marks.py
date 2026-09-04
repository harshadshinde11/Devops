# Student Marks Calculator

# Accept marks for 5 subjects
mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))
mark4 = int(input("Enter marks for Subject 4: "))
mark5 = int(input("Enter marks for Subject 5: "))

# Calculate total and percentage
total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

# Calculate grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display final result
print("\n--- Final Result ---")
print("Total Marks:", total, "/500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
