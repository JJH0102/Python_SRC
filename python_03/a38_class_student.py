class Student :
    def __init__(self, name, korean, math, english, science) :
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
        # (*this) == self

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

    for students in students :
        score_sum = (Student.korean + Student.math + Student.english + Student.science)
        score_average = score_sum / 4

        print(f"{Student.name}\t{score_sum}\t{score_average:.2f}")

        a_student = Student("A", 11, 22, 33, 44)
        print(a_student.name)

if __name__ == "__main__":
    main()