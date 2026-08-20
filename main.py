from agent.planner import create_plan


def main():

    print("MiniCursor Planner启动")


    while True:

        user_input = input("\n需求: ")

        if user_input == "exit":
            break


        plan = create_plan(user_input)

        print("\n规划结果:")
        print(plan)


if __name__ == "__main__":
    main()