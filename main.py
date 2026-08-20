from tools.runner import run_python


def main():

    result = run_python(
        "test.py"
    )


    print(result)


if __name__ == "__main__":
    main()