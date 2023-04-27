import openai
openai.api_key = ""
#openai.organization = "org-XXX"

def generate_response(userprompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userprompt}
        ]
    )
    message = completion.choices[0].message.content
    return message


    prompt = "explain why there is no -0 in math for 7 years child"
    
    response = generate_response(prompt)

    print(response)
