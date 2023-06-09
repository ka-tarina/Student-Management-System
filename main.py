from student import Student
from department import Department
from subject import Subject


def main():

    department_fs = Department("Filozofija", "FS", subjects=[], students=[])
    department_sc = Department("Sociologija", "FS", subjects=[], students=[])
    departments = [department_fs, department_sc]

    student1 = Student("Dragana", "Mirković", "cs001", "Filozofija", {"Istorija filozofija": 0, "Logika": 7, "Filozofija religije": 9})
    student2 = Student("Jašar", "Ahmedovski", "cs005", "Filozofija", {"Istorija filozofije": 0, "Logika": 8, "Filozofija religije": 10})
    student3 = Student("Šemsa", "Suljaković", "cs007", "Filozofija", {"Istroija filozofije": 0, "Logika": 8, "Filozofija religije": 0})
    student4 = Student("Marta", "Savić", "py456", "Sociologija", {"Uvod u sociologiju": 9, "Osnovi ekonomije": 10, "Socijalna demografija": 8})
    student5 = Student("Mile", "Kitić", "py781", "Sociologija", {"Uvod u sociologiju": 8, "Osnovi ekonomije": 9, "Socijalna demografija": 10})
    fs = [student1, student2, student3]
    sc = [student4, student5]
    department_fs.students.extend(fs)
    department_sc.students.extend(sc)
    predmet1 = Subject("Istorija filozofija", "fs98")
    predmet2 = Subject("Logika", "fs74")
    predmet3 = Subject("Filozofija religije", "fs25")
    predmet4 = Subject("Uvod u sociologiju", "fs47")
    predmet5 = Subject("Osnovi ekonomije", "sc11")
    predmet6 = Subject("Socijalna demografija", "sc06")
    predmeti_fs = [predmet1, predmet2, predmet3]
    predmeti_sc = [predmet4, predmet5, predmet6]
    department_fs.subjects.extend(predmeti_fs)
    department_sc.subjects.extend(predmeti_sc)



    ans = True

    while ans:
        print("""
        A.  dodaj novog studenta na smer
        B.  dodaj novi predmet na smer
        C.  dodaj novi predmet studentu
        D.  prikaži listu svih položenih ispita određenog studenta
        E.  prikaži srednju ocenu studenta
        F.  prikaži podatake studenta/studenata sa navećom prosečnom ocenom
        G.  prikaži podatake studenta/studenata sa najmanje položenih ispita
        H.  prikaži sve studente koji su položili sve ispite na predmetima koji su im dodeljeni
        I.  prikaži raspodelu studenata po smerovima, u procentima
        J.  prikaži sve studente na odabranom smeru
        K.  prikaži najboljeg studenta na odabranom smeru
        L.  prikaži sve predmete koji nije položio niti jedan student
        M.  prikaži predmet sa najvećom prosečnom ocenom
        X.  kraj programa
        """)

        ans = input("Izabrati opciju iz menija: ").lower()

        if ans == "a":

            # Add new student to department
            name = input("Uneti ime studenta: ")
            surname = input("Uneti prezime studenta: ")
            index_number = input("Uneti broj indexa studenta: ")
            department_name = input("Uneti ime smera: ")
            marks = {}
            department_found = False
            for department in departments:
                if department.name == department_name:
                    department_found = True
                    student = Student(name, surname, index_number, department_name, marks)
                    department.add_student(student)
            if not department_found:
                print("Smer ne postoji.")


        elif ans == "b":
            # Add new subject to department.
            name = input("Uneti ime predmeta: ")
            id = input("Uneti jedinstvenu šifru predmeta: ")
            department_name = input("Uneti ime smera: ")
            department_found = False
            for department in departments:
                if department.name == department_name:
                    department_found = True
                    subject = Subject(name, id)
                    department.add_subject(subject)
            if not department_found:
                print("Smer ne postoji.")


        elif ans == "c":
            # Add new subject to student
            index_number = input("Uneti broj indeksa studenta: ")
            subject_name = input("Unet ime predmeta: ")
            mark = int(input("Uneti ocenu: "))
            student_found = False
            for department in departments:
                for student in department.students:
                    if student.index_number == index_number:
                        student_found = True
                        subject_found = False
                        for subject in department.subjects:
                            if subject.name == subject_name:
                                subject_found = True
                                student.add_subject_for_student(subject, mark)
                                if not subject_found:
                                    print("Predmet ne postoji.")
                                if not student_found:
                                    print("Student ne postoji.")


        elif ans == "d" or ans == "e":
            index_number = input("Uneti broj indeksa studenta: ")
            student = None
            for d in departments:
                for s in d.students:
                    if s.index_number == index_number:
                        student = s
                        break
            if student is None:
                print("Ne postoji student sa unetim brojem indeksa.")
            else:
                if ans == "d":
                    # List all subjects the given student has passed.
                    passed_subjects = student.get_passed_subjects_for_student()
                    print(f"Položeni ispiti za studenta sa brojem indeksa {index_number}:")
                    for subject in passed_subjects:
                        print(f"- {subject}")
                elif ans == "e":
                    # Get the average mark of the given student
                    average = student.calculate_average_mark()
                    print(f"Prosečna ocena studenta sa brojem indexa {index_number} je {average}.")


        elif ans == "f":
            # Get info for student/s with the highest mark.
            for d in departments:
                student = Student.get_student_with_highest_average(d.students)
                print(f"Student sa najvećom prosečnom ocenom je {student.get_name()} {student.get_surname()} sa brojem"
                      f" indeksa {student.index_number}")


        elif ans == "g":
            # Get info for student/s that passed least subjects.
            students = []
            for d in departments:
                students.extend(d.students)
            student_with_least = Student.get_students_that_passed_least_subjects(students)
            print(f"Student sa najmanje položenih ispita je: {student_with_least.get_name()} {student_with_least.get_surname()} "
                  f"sa brojem indeksa {student_with_least.index_number}")


        elif ans == "h":
            # List all students that passed all their exams
            print("Studenti koji su položili sve ispite na predmetima koji su im dodeljeni su:")
            for d in departments:
                students_passed_all = Student.get_students_that_passed_all_subjects(d.students)
                for student in students_passed_all:
                    print(f"- student sa brojem indeksa {student.index_number}")


        elif ans == "i":
            # Get the distribution of students by departments in percentile.
            students = []
            for d in departments:
                students.extend(d.students)
            distribution = Department.get_distribution_by_department(students)
            for dep_name, per in distribution.items():
                print(f"{dep_name}: {per}%")


        elif ans == "j":
            # List all students in given department
            department_name = input("Uneti ime smera: ")
            department_found = False
            for department in departments:
                if department.name == department_name:
                    department_found = True
                    print("Studenti:")
                    for student in department.students:
                        print(f"- {student.get_name()} {student.get_surname()} {student.index_number}")


        elif ans == "k":
            # Get the best student at department
            department_name = input("Uneti ime smera: ")
            department_found = False
            for department in departments:
                if department.name == department_name:
                    department_found = True
                    best_student = department.get_best_student_in_department()
                    print(f"Najbolji student na smeru {department.name} je {best_student.get_name()} "
                          f"{best_student.get_surname()} sa brojem indeksa {best_student.index_number}.")
                    break
            if not department_found:
                print("Smer ne postoji.")


        elif ans == "l":
            # Get all subjects that no student passed
            print("Predmeti koje nije položio nijedan student:")
            for d in departments:
                not_passed = Student.get_subjects_not_passed(d.students)
                for subject in not_passed:
                    print(f"- {subject}")


        elif ans == "m":
            # Get the subject with the highest average mark
            for d in departments:
                highest_subject = Student.get_subject_with_highest_grade(d.students)
                print(f"Predmet sa najvećom prosečnom ocenom je {highest_subject}")


        elif ans == "x":
            print("Kraj programa.")
            ans = False
        else:
            print("Nepravilan unos.")

if __name__ == "__main__":
    main()
