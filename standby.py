


import openai

import OPEN_API_KEY # we need the API key and its hidden in a seperate local file

openai.api_key = OPEN_API_KEY.mykey



def query(content, maximum_tokens = 150, temp = 0):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": content}],
    max_tokens= maximum_tokens,
    temperature = temp
    )

    return(completion['choices'][0]['message']['content'])


