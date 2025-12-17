import ollama

response = ollama.chat(
    model="llama3", #LLM model 
    messages=[
        {
            "role": "user",
            "content": "Translate the following: \nEnglish: mango\nHindi:आम \n\nEnglish: apple"
        }
    ]
)

print(response['message']['content'])