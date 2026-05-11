import os

from dotenv import load_dotenv

from openai import OpenAI


load_dotenv()


client = OpenAI(

    api_key=os.environ["sk-6v2xnpTjHvbnk3R6Bg6eQmMMJJ0ivBwec8de6yohAOG28TSI"],

    base_url=os.environ["https://api.chatanywhere.tech/v1"],

)


resp = client.chat.completions.create(

    model=os.environ["MODEL"],

    messages=[

        {"role": "system", "content": "You are a helpful tutor."},

        {"role": "user",   "content": "Explain recursion in 2 lines."},

    ],

)

print(resp.choices[0].message.content)
