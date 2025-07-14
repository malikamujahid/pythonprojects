import json

# Create dummy student data
students = [
    {"name": "Alice", "id": "S001", "grade": "A"},
    {"name": "Bob", "id": "S002", "grade": "B"},
    {"name": "Charlie", "id": "S003", "grade": "A"},
    {"name": "Diana", "id": "S004", "grade": "C"},
    {"name": "Ethan", "id": "S005", "grade": "B"}
]

# Save to a JSON file
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("students.json file created successfully!")
