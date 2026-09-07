# Dictionary with 5 students and their marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}

# 1. Display all students and their marks
print("Students and their marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")

# 2. Find the student with the highest mark
highest_student = max(students, key=students.get)  # gets the key with max value
highest_mark = students[highest_student]

print(f"\nStudent with highest mark: {highest_student} with {highest_mark}")