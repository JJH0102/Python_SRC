def main():
    dictionary = {
        "name" : "7D 건조 망고",
        "type" : "당절임",
        "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
        "origin" : "필리핀",
    }

    # print(f'name : {dictionary["name"]}')
    # print(f'type : {dictionary["type"]}')
    # print(f'ingredient : {dictionary["ingredient"]}')
    # print(f'origin : {dictionary["origin"]}')

    # for key in dictionary:
    #     print(f"{key} : {dictionary[key]}")

    for key, value in dictionary.items():
        print(f"{key} : {value}")

    dictionary["name"] = "8D 건조 망고"
    print(f'name : {dictionary["name"]}')
    print(f'ingredient[1] : {dictionary["ingredient"][1]}')

    key = input("키를 입력해 주세요 : ")

    # if key in dictionary:
    #     print(f"value : {dictionary[key]}")
    # else:
    #     print("해당 키는 dictionary에 존재하지 않습니다.")

    value = dictionary.get(key)
    print(f"value : {value}")

    # delete
    del dictionary["ingredient"]
    print(dictionary)
    re = dictionary.pop("name")
    print(dictionary, re)

    # value error
    dict_test = { 1: "123"}
    print(dict_test[1])

if __name__ == "__main__":
    main()