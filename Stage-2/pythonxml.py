import xml.etree.ElementTree as ET

tree = ET.parse("students.xml")
root = tree.getroot()

for student in root.findall("student"):
    student_id = student.get("id")
    name = student.find("name").text
    age = student.find("age").text

    print("ID:", student_id)
    print("Name:", name)
    print("Age:", age)