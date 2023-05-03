


import openai

import OPEN_API_KEY # we need the API key and its hidden in a seperate local file

openai.api_key = OPEN_API_KEY.mykey



def query(content):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": content}],
    max_tokens=150,
    temperature = 0
    )

    return(completion['choices'][0]['message']['content'])