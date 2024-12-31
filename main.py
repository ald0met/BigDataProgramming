from student import Student
from grading_system import GradingSystem

students_data = [
    (1, "서강일", "남", 22, 90, 80, 85),
    (2, "서강이", "여", 22, 90, 85, 95),
    (3, "서강삼", "남", 21, 80, 80, 80),
    (4, "서강사", "여", 20, 90, 92, 83),
    (5, "서강오", "남", 20, 85, 90, 90),
]

grading_system=GradingSystem()

for data in students_data:
    student=Student(*data)
    grading_system.register_student(student)

grading_system.process()
grading_system.print_students()
grading_system.print_class_info()
grading_system.print_execution_time()
