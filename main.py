from agent.reviewer import review


def main():

    code = """
print(message)
"""


    result = {
        "success":False,
        "stderr":
        "NameError: name 'message' is not defined"
    }


    answer = review(
        code,
        result
    )


    print(answer)


if __name__=="__main__":
    main()