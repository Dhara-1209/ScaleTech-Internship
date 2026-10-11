import json

# Read JSON
with open("student.json", "r") as file:
    data = json.load(file)

print("Name:", data["name"])
print("Python Marks:", data["marks"]["python"])

# Modify
data["age"] = 21
data["marks"]["python"] = 95

# Write JSON
with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data updated successfully")