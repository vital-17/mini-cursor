from agent.manager import AgentManager


def main():
    manager = AgentManager()

    print("MiniCursor Agent")
    print("输入 exit 退出")

    while True:
        requirement = input("\n需求: ").strip()

        if requirement.lower() == "exit":
            break

        if not requirement:
            continue

        try:
            result = manager.run(requirement)

            print("\n========== RESULT ==========")
            print(f"文件: {result['filepath']}")

            print("\n运行结果:")
            print(result["execution"])

            print("\n代码审查:")
            print(result["review"])

        except Exception as exc:
            print(f"\nAgent运行失败: {exc}")


if __name__ == "__main__":
    main()