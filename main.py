from agent.llm import chat


def main():

    print("MiniCursor启动成功")

    while True:

        user_input = input("\nYou: ")

        if user_input == "exit":
            break

        answer = chat(user_input)

        print("\nMiniCursor:")
        print(answer)


if __name__ == "__main__":
    main()