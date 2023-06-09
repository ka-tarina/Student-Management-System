from student import Student
from subject import Subject
from typing import List, Dict


class Department:
    """Model of an instance of Department."""

    def __init__(self, name: str, module: str, subjects: List[Subject], students: List[Student]):
        """Initialize the Department object."""
        self.name = name
        self.module = module
        self.subjects = subjects
        self.students = students

    def add_student(self, student: Student) -> None:
        """Add student."""
        self.students.append(student)

    def add_subject(self, subject: Subject) -> None:
        """Add subject to department."""
        self.subjects.append(subject)

    @staticmethod
    def get_distribution_by_department(students: List["Student"]) -> Dict[str, int]:
        """Get the distribution of students by department in percentile."""
        distribution = {}
        total_students = len(students)
        for student in students:
            department = student.department
            if department not in distribution:
                distribution[department] = 0
            distribution[department] += 1
        for department in distribution:
            distribution[department] = distribution[department] / total_students * 100
        return distribution

    def get_students_in_department(self) -> List[Student]:
        """Get all students in department."""
        return self.students

    def get_best_student_in_department(self) -> Student:
        """Get the best students in department."""
        department_students = self.get_students_in_department()
        return Student.get_student_with_highest_average(department_students)

