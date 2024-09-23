from dataclasses import dataclass

@dataclass
class Student:
    name: str
    korean: int
    math: int
    english: int
    science: int

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
        score_sum = (student.korean + student.math + student.english + student.science)
        score_average = score_sum / 4
        
        print(f"{student.name}\t{score_sum}\t{score_average:.2f}")

if __name__ == "__main__":
    main()