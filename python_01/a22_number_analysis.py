# 사용자가 여러 숫자를 쉼표로 구분하여 입력
# ex) 10, 20, 30, abc
# 합계 계산, 평균 계산, 최대값 계산, 최소값 계산
# 만약 문자가 존재하면 무시하고 계산하고 어떤 값이 무시되었는지 출력
# 입력에 숫자가 존재하지 않으면 '유효한 숫자가 없습니다' 출력
# format을 써서 자리수를 유효숫자 소수점 3번째 자리까지 출력

def main():
    user_input = input("숫자를 쉼표로 구분하여 입력 : ")

    split_values = user_input.split(',')

    # 초기 변수
    index = 0
    total = 0
    count = 0
    max = None
    min = None

    while index < len(split_values):
        current_number = split_values[index].strip()

        try:
            number = float(current_number)
            total += number
            count += 1

            if max is None or number > max :
                max = number
            if min is None or number < min:
                min = number

        except ValueError:
            print(f"무시된 값 : {current_number}")

        index += 1

    if count > 0:
        average = total / count
        print(f"합계 : {total:.3f}")
        print(f"평균 : {average:.3f}")
        print(f"최대값 : {max}")
        print(f"최소값 : {min}")
    else:
        print("유효한 숫자가 없습니다.")

if __name__ == "__main__":
    main()