import ollama

response = ollama.chat(
    model="llama3", #LLM model 
    messages=[
        {
            "role": "user",
            # "content": "What is the capital of india?"
            # "content": "List five popular places to visit in New Delhi"
            "content": "Only lList five popular places to visit in New Delhi. Do not generate any other text. Only provide the list."
        },
        # {
        #     "role": "user",
        #     "content": "List five popular places to visit in New Delhi"
        # }
    ]
)

# print(response)
# print(response["message"])
print(response['message']['content'])