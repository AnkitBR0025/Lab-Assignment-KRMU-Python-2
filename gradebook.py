# Name=Ankit Kumar Pandey,  Date=06/11/2025
#Title : Gradebook Analyzer

print("\nWelcome to the Gradebook Analyzer\n")

#Student data input
def get_student_data():
    marks = {}
    num_students = int(input("Enter the number of students in the class: "))
    for _ in range(num_students):
        name = input("\nEnter student name: ")
        mark = int(input(f"Enter marks for {name}: "))
        marks[name] = mark
    return marks
#Statistics calculations
def calculate_average(marks_dict):
    if not marks_dict:
        return 0
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    if not marks_dict:
        return 0
    sorted_marks = sorted(marks_dict.values())
    n = len(sorted_marks)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
    else:
        return sorted_marks[mid]

def find_max_score(marks_dict):
    if not marks_dict:
        return None
    max_student = max(marks_dict, key=marks_dict.get)
    return max_student, marks_dict[max_student]

def find_min_score(marks_dict):
    if not marks_dict:
        return None
    min_student = min(marks_dict, key=marks_dict.get)
    return min_student, marks_dict[min_student]

#Grade distribution and pass/fail lists
def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark>=90:
            grade='A'
        elif mark>=80:
            grade='B'
        elif mark>=70:
            grade='C'
        elif mark>=60:
            grade='D'
        else:
            grade='F'
        grades[name]=grade
    return grades

def count_grades(grades_dict):
    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades_dict.values():
        if grade in grade_counts:
            grade_counts[grade] += 1
    return grade_counts

def pass_fail_lists(marks_dict):
    passed_students = [name for name, m in marks_dict.items() if m >= 40]
    failed_students = [name for name, m in marks_dict.items() if m < 40]
    return passed_students, failed_students

def print_statistics(marks_dict, grades_dict):
    print("\nStatistics:")
    print(f"Average Marks: {calculate_average(marks_dict):.2f}")
    print(f"Median Marks: {calculate_median(marks_dict):.2f}")
    max_student, max_mark = find_max_score(marks_dict)
    print(f"Highest Score: {max_mark} (Student: {max_student})")
    min_student, min_mark = find_min_score(marks_dict)
    print(f"Lowest Score: {min_mark} (Student: {min_student})")

    grade_counts = count_grades(grades_dict)
    print("\nGrade Distribution:")
    for grade, count in grade_counts.items():
        print(f"Grade {grade}: {count}")

    passed_students, failed_students = pass_fail_lists(marks_dict)
    print(f"\nPassed Students ({len(passed_students)}): {passed_students}")
    print(f"Failed Students ({len(failed_students)}): {failed_students}")

#Results table
def print_results_table(marks_dict, grades_dict):
    print("\nResults Table:")
    print(f"{'Name':<12}{'Marks':<8}{'Grade'}")
    print("-" * 28)
    for name in marks_dict:
        print(f"{name:<12}{marks_dict[name]:<8}{grades_dict[name]}")


# print("Gradebook Analyzer\n")
marks = get_student_data()
if not marks:
    print("No student data entered. Exiting.")
else:
    grades = assign_grades(marks)
    print_statistics(marks, grades)
    print_results_table(marks, grades)
print("\nDone. Exiting.")



