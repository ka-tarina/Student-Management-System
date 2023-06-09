from subject import Subject
from typing import List


class Student:
    """Model of an instance Student."""

    def __init__(self, name: str, surname: str, index_number: str, department: str, marks: dict):
        """Initialize the Student object."""
        self.__name = name
        self.__surname = surname
        self.index_number = index_number
        self.department = department
        self.marks = marks

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def add_subject_for_student(self, subject: Subject, mark: int):
        """Add subject to an instance of the Student object."""
        self.marks[subject.name] = mark

    def get_passed_subjects_for_student(self) -> List[str]:
        """Gets the list of all the subjects that an instance of the Student has passed."""
        passed_subjects = []
        for subject, mark in self.marks.items():
            if mark >= 6:
                passed_subjects.append(subject)
        return passed_subjects

    def calculate_average_mark(self) -> float:
        """Calculates average mark of an instance of the Student."""
        total_marks = 0
        num_subjects = 0
        for subject, mark in self.marks.items():
            if mark == 0:
                pass
            else:
                total_marks += mark
                num_subjects += 1
        return round(total_marks / num_subjects, 2)

    @staticmethod
    def get_student_with_highest_average(students: List["Student"]) -> "Student":
        """Get the student with the highest average mark."""
        highest_average = 0
        highest_student = None
        for student in students:
            average = student.calculate_average_mark()
            if average > highest_average:
                highest_average = average
                highest_student = student
        return highest_student

    def calculate_num_passed_subjects(self) -> int:
        """Get the number of passed subjects for an instance of the Student."""
        return len(self.get_passed_subjects_for_student())

    @staticmethod
    def get_students_that_passed_least_subjects(students: List["Student"]) -> "Student":
        """Get the student with that passed the least exams."""
        min_passed = 100
        min_student = None
        for student in students:
            num_passed = student.calculate_num_passed_subjects()
            if num_passed <= min_passed:
                min_passed = num_passed
                min_student = student
        return min_student

    @staticmethod
    def get_students_that_passed_all_subjects(students: List["Student"]) -> List["Student"]:
        """Get students that passed all subjects."""
        passed_students = []
        for student in students:
            if student.calculate_num_passed_subjects() == len(student.marks):
                passed_students.append(student)
        return passed_students

    @staticmethod
    def get_subjects_not_passed(students: List["Student"]) -> List[str]:
        """Get all subjects that no student has passed."""
        all_subjects = set()
        passed_subjects = set()
        for student in students:
            all_subjects.update(student.marks.keys())
            passed_subjects.update(student.get_passed_subjects_for_student())
        return list(all_subjects - passed_subjects)

    @staticmethod
    def get_subject_with_highest_grade(students: List["Student"]) -> str:
        """Get the subject with the highest grade."""
        highest_grade = 0
        highest_grade_subject = ""
        for student in students:
            for subject, mark in student.marks.items():
                if mark > highest_grade:
                    highest_grade = mark
                    highest_grade_subject = subject
        return highest_grade_subject
