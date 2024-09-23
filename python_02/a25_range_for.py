def main():
    # range를 이용한 for
    for i in range(10):
        print(f"{i}번째 반복 출력입니다.")

    # list를 이용한 for
    li1 = [0, 1, 2, 4, 5, 6, 7, 8, 9]

    for i in li1:
        print(f"{i}번째 반복 출력입니다.")

    for i in range(1, 10, 2):
        print(f"{i}번째 반복 출력입니다.")

    li2 = ['banana', 'apple', 'grape', 'mango', 'dragonfruit']

    for ele in li2:
        print(ele)

if __name__ == "__main__":
    main()