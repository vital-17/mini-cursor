from agent.llm import chat
from agent.prompt_loader import load_prompt


PLANNER_PROMPT = load_prompt("planner.md")


def create_plan(requirement: str) -> str:
    prompt = f"""
{PLANNER_PROMPT}

用户需求：

{requirement}
"""

    return chat(prompt)