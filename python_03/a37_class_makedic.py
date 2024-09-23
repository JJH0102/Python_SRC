def create_student(name, korean, math, english, science) :
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def main():
    students = [
        create_student("윤인성", 87, 98, 88, 95),
        create_student("연하진", 92, 92, 89, 78),
        create_student("구지연", 81, 54, 79, 87),
        create_student("나선주", 78, 89, 67, 95),
        create_student("윤아린", 36, 43, 34, 76),
        create_student("윤명원", 98, 99, 92, 90)
    ]

    print("이름\t총점\t평균")

    for students in students :
        score_sum = (students["korean"] + students["math"] + students["english"] + students["science"])
        score_average = score_sum / 4

        print(f"{students['name']}\t{score_sum}\t{score_average:.2f}")

if __name__ == "__main__":
    main()