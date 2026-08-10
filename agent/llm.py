from openai import OpenAI
from config import DASHSCOPE_API_KEY


client = OpenAI(
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def chat(message):

    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {
                "role": "system",
                "content": "你是MiniCursor，一个AI编程助手"
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content