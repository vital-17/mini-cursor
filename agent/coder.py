import json

from agent.llm import chat
from agent.prompt_loader import load_prompt


CODER_PROMPT = load_prompt("coder.md")


def generate_code(plan: str) -> dict:
    prompt = f"""
{CODER_PROMPT}

项目规划：

{plan}
"""

    response = chat(prompt)

    try:
        return json.loads(response)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Coder returned invalid JSON:\n{response}"
        ) from exc