from agent.llm import chat
from agent.prompt_loader import load_prompt


REVIEWER_PROMPT = load_prompt("reviewer.md")


def review(code: str, result: dict) -> str:
    prompt = f"""
{REVIEWER_PROMPT}

代码：

{code}

运行结果：

{result}
"""

    return chat(prompt)