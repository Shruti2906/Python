
students = ["ram", "sham", "abc", "xyz"]

for student in students:
    if student == "sham":
        continue
    print(student)

print("\n----------------------")
for student in students:
    if student == "abc":
        break;
    print(student)