import json
import csv 
import logging

logging.basicConfig(level=logging.INFO)

class Student:
    def __init__(self, name, student_id, grade, filename="students.json"):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.filename = filename  

    def addNewStudents(self):
        data = {
            "name": self.name,
            "id": self.student_id,
            "grade": self.grade,
        }

        try:
            with open(self.filename, "r") as f:
                students = json.load(f)
                logging.info("File opened successfully")
        except Exception as e:
            logging.error(f"Unable to open JSON file to add new data {e}")
            return

        # check if student already exists to save from duplication
        if self.student_id not in [student["id"] for student in students]:
            students.append(data)
            with open(self.filename, "w") as f:
                json.dump(students, f)
            print("Student added successfully.")
        else:
            print("Student with this ID already exists.")

    @staticmethod
    def updateGrade(file, student_id, grade):
        try:
            with open(file, "r") as f:
                students = json.load(f)
        except FileNotFoundError:
            print("file not found")
            return
        except Exception as e:
            logging.error(f"Unable to open JSON file to add new data {e}")
            return

        for student in students:
            if student["id"] == student_id:
                student["grade"] = grade

        try:
            with open(file, "w") as f:
                json.dump(students, f)
        except FileNotFoundError:
            print("file not found")
        except Exception as e:
            logging.error(f"Unable to open JSON file to add new data {e}")
            return

    @staticmethod
    def calculateGPA(file):
        try:
            with open(file, "r") as f:
                students = json.load(f)
        except FileNotFoundError:
            print("File not found.")
            return
        except Exception as e:
            print("Error reading JSON file:", e)
            return

        for student in students:
            grade = student.get("grade")

            if grade in ["A", "A+"]:
                student["GPA"] = 3.8
            elif grade in ["B", "B+"]:
                student["GPA"] = 3.0
            elif grade in ["C", "C+"]:
                student["GPA"] = 2.5
            else:
                student["GPA"] = 2.0

        try:
            with open(file, "w") as f:
                json.dump(students, f)
        except Exception as e:
            logging.error(f"Unable to write to JSON file {e}")
            return


    @staticmethod
    def toCSV(json_file, csv_file):
        try:
            with open(json_file, "r") as f:
                jsonfile = json.load(f)
        except FileNotFoundError:
            print("JSON file not found.")
            return
        except Exception as e:
            logging.error(f"Unable to open JSON file to add new data {e}")
            return

        try:
            with open(csv_file, "w", newline="") as f1:
                writer = csv.DictWriter(f1, fieldnames=jsonfile[0].keys())
                writer.writeheader()
                writer.writerows(jsonfile)
        except Exception as e:
            logging.error(f"Unable to open JSON file to add new data {e}")
            return




s = Student("zack", "S006", "A")
s.addNewStudents()
Student.updateGrade("students.json", "S001", "B+")
Student.calculateGPA("students.json")
Student.toCSV("students.json", "students.csv")
Student.updateGrade("students.json", "S001", "C+")
