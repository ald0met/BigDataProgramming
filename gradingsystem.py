from student import Student
import time

class checkTime:
    def __init__(self,func):
        self.func=func
    def __call__(*args,**kwargs):
        start=time.time()
        self.func(*args,**kwargs)
        end=time.time()
        print("실행시간은:",end-start)
    
class GradingSystem: 
    
    def __init__(self):
        self.students=[]
        
    def register_student(self,student):
        self.students.append(student)
        
    @checkTime
    def process(self):
        self.students.sort(key=lambda x: x.total, reverse=True)
        rank=1
        for i,student in enumerate(self.students):
            if i>0 and student.total==self.students[i-1].total:
                student.order=self.students[i-1].order
            else:
                student.order=rank
            rank+=1
            
    @checkTime         
    def print_students(self):
        for student in self.students:
            print(f"번호: {student.num},이름: {student.name},국어: {student.kor},영어: {student.eng},수학: {student.math}, 총점: {student.total},평균: {student.avg:.2f}, 등수: {student.order}")

    @checkTime
    def print_class_info(self):
        
        total_sum=sum(student.total for student in self.students)
        kor_sum=sum(student.kor for student in self.students)
        eng_sum=sum(student.eng for student in self.students)
        math_sum=sum(student.math for student in self.students)

        total_avg=round(total_sum/len(self.students),2)
        kor_avg=round(kor_sum/len(self.students),2)
        eng_avg=round(eng_sum/len(self.students),2)
        math_avg=round(math_sum/len(self.students),2)

        kor_max=max(student.kor for student in self.students)
        eng_max=max(student.eng for student in self.students)
        math_max=max(student.math for student in self.students)

        kor_max_students=[student.name for student in self.students if student.kor==kor_max]
        eng_max_students=[student.name for student in self.students if student.eng==eng_max]
        math_max_students=[student.name for student in self.students if student.math==math_max]

        print(f"\n총점 반평균: {total_avg}")
        print(f"\n국어 반평균: {kor_avg}")
        print(f"\n영어 반평균: {eng_avg}")
        print(f"\n수학 반평균: {math_avg}")

        print("\n각 과목의 최고점과 명단")
        print(f"\n국어의 최고점 {kor_max}"," ".join(kor_max_students))
        print(f"\n영어의 최고점 {eng_max}"," ".join(eng_max_students))
        print(f"\n수학의 최고점 {math_max}"," ".join(math_max_students))
