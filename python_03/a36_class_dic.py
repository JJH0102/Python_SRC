def main():
    students = [
        {"name" : "윤인성", "korean" : 87, "math" : 98, "english" : 88, "science" : 95},
        {"name" : "연하진", "korean" : 92, "math" : 92, "english" : 89, "science" : 78},
        {"name" : "구지연", "korean" : 81, "math" : 54, "english" : 79, "science" : 87},
        {"name" : "나선주", "korean" : 78, "math" : 89, "english" : 67, "science" : 95},
        {"name" : "윤아린", "korean" : 56, "math" : 43, "english" : 34, "science" : 76},
        {"name" : "윤명원", "korean" : 98, "math" : 99, "english" : 92, "science" : 90}
    ]

    print("이름\t총점\t평균")

    for students in students :
        score_sum = (students["korean"] + students["math"] + students["english"] + students["science"])
        score_average = score_sum / 4

        print(f"{students['name']}\t{score_sum}\t{score_average:.2f}")

if __name__ == "__main__":
    main()