class Student:
    def __init__(self, name, korean, math, english, science):
        self.name =  name
        self.korean =  korean
        self.math =  math
        self.english = english
        self.science =  science
        self.sum = self.get_sum()
        self.average = self.get_average()

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.sum / 4

    def to_string(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average():.2f}"

    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average():.2f}"

    def __eq__(self, value):
        return self.sum  == value.sum

    def __ne__(self, value):
        return self.sum  != value.sum

    def __gt__(self, value):
        return self.sum  > value.sum

    def __ge__(self, value):
        return self.sum  >= value.sum

    def __lt__(self, value):
        return self.sum  < value.sum

    def __le__(self, value):
        return self.sum  <= value.sum

def main():
    students = [
        Student("윤인성", 87, 98, 88, 95),
        Student("연하진", 92, 92, 89, 78),
        Student("구지연", 81, 54, 79, 87),
        Student("나선주", 78, 89, 67, 95),
        Student("윤아린", 36, 43, 34, 76),
        Student("윤명원", 98, 99, 92, 90)
    ]

    print("이름\t총점\t평균")
    for student in students:
        print(student.to_string())
        print(student)

    student_a = Student("윤인성", 87, 98, 88, 95)
    student_b = Student("연하진", 92, 92, 89, 78)
    print(f"student_a == student_b : {student_a == student_b}")
    print(f"student_a is student_b : {student_a is student_b}")
    print(f"student_a != student_b : {student_a != student_b}")

if __name__ == "__main__":
    main()