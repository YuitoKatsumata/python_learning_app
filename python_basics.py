def main():
    # app_name ="Python Learning App"
    # lesson_number = 1
    # is_completed = False

    # print(app_name)
    # print(lesson_number)
    # print(is_completed)

    # print(type(app_name))
    # print(type(lesson_number))
    # print(type(is_completed))

    # user_name = input("名前を入力してください！")

    # print(f"こんにちは、{user_name}さん！")

    # data_type = input("Pythonで文字列を表すデータ型は？")

    # if data_type == "str":
    #     print("正解！")
    # else:
    #     print("不正解！")

    for i in range(1,4):
        ans = input(f"{i}問目のクイズです")
        if ans == "str":
            print("正解！")
        else:
            print("不正解！")

if __name__ == "__main__":
    main()