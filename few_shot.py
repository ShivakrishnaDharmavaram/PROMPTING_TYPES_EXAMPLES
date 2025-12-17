import ollama


prompt = ''' Translate the following english words to telugu:
English: mango
Telugu: మామిడిపండు
English: banana
Telugu: అరటిపండు
English: apple
Telugu:
'''

response = ollama.chat(
    model="llama3", #LLM model 
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response['message']['content'])