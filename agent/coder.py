from agent.llm import chat


CODER_PROMPT = """
你是一名高级Python工程师。

根据项目规划生成代码。

要求：

1. 代码完整可运行
2. 遵循Python规范
3. 添加必要注释
4. 输出文件名和代码
"""


def generate_code(plan):

    prompt = f"""
{CODER_PROMPT}


项目规划：

{plan}


请生成实现代码。
"""

    result = chat(prompt)

    return result