students = [
    ("thara", 85),
    ("Riya", 92),
    ("Aman", 78)
]

result = sorted(students, key=lambda x: x[0])

print(result)