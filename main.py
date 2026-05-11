import os

from dotenv import load_dotenv

from openai import OpenAI


load_dotenv()


client = OpenAI(

    api_key=os.environ["CHATANYWHERE_API_KEY"],

    base_url=os.environ["BASE_URL"],

)


resp = client.chat.completions.create(

    model=os.environ["MODEL"],

    messages=[

        {"role": "system", "content": "You are a helpful tutor."},

        {"role": "user",   "content": "Explain recursion in 2 lines."},

    ],

)

print(resp.choices[0].message.content)
