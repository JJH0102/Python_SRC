def main():
    # 선언
    dict_a = {'a':123}
    # set_a = set()
    set_b = {1, 2, 3}
    # set_a.add(1)

    print(type(dict_a))
    print(type(set_a))
    print(type(set_b))
    print(dict_a, set_a, set_b)

    # 요소 추가
    dict_a['b'] = 456
    dict_a['a'] = '123'

    print(dict_a)

    # 요소 접근
    print(dict_a['a'], dict_a['b'])
    print(dict_a['c']) # --> 존재하지 않는 요소에 접근하면 오류
    print(dict_a.get('c')) # --> 요소가 존재하는지 확인

if __name__ == "__main__":
    main()