def main():
    quizzes = [
        {
            "question": "Pythonで文字列を表す型は？",
            "answer": "str"
        },
        {
            "question": "Pythonで整数を表す型は？",
            "answer": "int"
        },
        {
            "question": "Pythonで真偽値を表す型は？",
            "answer": "bool"
        }
    ]

    current_score = 0

    for index, quiz in enumerate(quizzes, start=1):
        print(f"{index}問目：{quiz['question']}")
        ans = input("答えを書いてください")

        if ans == quiz["answer"]:
            print("正解！")
            current_score += 1
        else:
            print("不正解！")

    print(f"結果：{current_score}/{len(quizzes)}問正解")

if __name__ == "__main__":
    main()