students = {
    "Rajan": "A",
    "Sajan": "B",
    "Gunja": "C"
}
print("Existing students")
for name, grade in students.items():
    print(name, ":", grade)
name= input("Enter Students name:")
grade= input("Enter grade:").upper()

if name in students:
    students[name] = grade
    print("Student grade updated successfully.")
else:
    students[name] = grade
    print("New student added successfully")

print("\nUpdated Student:")
for name, grade in students.items():
    print(name, ":", grade)