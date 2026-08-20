from agent.planner import create_plan
from agent.coder import generate_code


def main():

    print("MiniCursor Agent启动")


    while True:

        user_input = input("\n需求: ")

        if user_input == "exit":
            break


        plan = create_plan(user_input)


        print("\n=====规划结果=====")
        print(plan)


        code = generate_code(plan)


        print("\n=====代码生成=====")
        print(code)


if __name__ == "__main__":
    main()