from tools.file_tool import create_file


def main():

    print("File Tool Test")


    code = """
print("Hello MiniCursor")
"""


    path = create_file(
        "test.py",
        code
    )


    print(
        "创建文件:",
        path
    )


if __name__ == "__main__":
    main()