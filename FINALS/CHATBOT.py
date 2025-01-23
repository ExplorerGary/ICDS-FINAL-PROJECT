
from openai import OpenAI
def get_GPT_response(user_input):
    api_key = "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"  # 替换为你的 API 密钥

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )


    message_content = completion.choices[0].message.content
    return message_content


# print(get_GPT_response(input("输入一个指令")))



    
