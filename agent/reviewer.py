from agent.llm import chat


REVIEWER_PROMPT = """
你是一名高级代码审查工程师。

你的任务：

分析代码运行结果，
发现Bug并提供修改建议。

要求：

1. 找出错误原因
2. 分析代码问题
3. 给出修复方案

不要直接重写全部代码。
"""


def review(code, result):

    prompt = f"""
{REVIEWER_PROMPT}


代码：

{code}


运行结果：

{result}


请进行代码审查。
"""


    response = chat(prompt)

    return response