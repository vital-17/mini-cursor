from agent.llm import chat


PLANNER_PROMPT = """
你是一名高级软件架构师和项目规划专家。

你的任务：
分析用户需求，并拆解开发步骤。

要求：
1. 理解目标
2. 拆分任务
3. 给出开发顺序
4. 指出技术重点

不要直接写代码。
"""


def create_plan(requirement):

    prompt = f"""
{PLANNER_PROMPT}


用户需求：

{requirement}
"""

    result = chat(prompt)

    return result