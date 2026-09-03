from agent.workflow import AgentWorkflow



def main():

    workflow = AgentWorkflow()


    print(
        "MiniCursor Agent"
    )


    while True:

        task = input(
            "\n需求:"
        )


        if task == "exit":
            break


        state = workflow.run(task)


        print("\n=====结果=====")

        print(
            "文件:",
            state.filename
        )


        print(
            "执行:",
            state.execution
        )


        print(
            "审查:",
            state.review
        )



if __name__ == "__main__":
    main()