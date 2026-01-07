students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

result = sorted(students, key= lambda student: student["grade"])

for student in students:
    print(f"{student["name"]} {student["grade"]}ball")