import ollama
# To run these on premise models, you need to have ollama server running locally.
# Commands to run ollama server:
# ollama pull llama3 ---> Once you pull the model, it will be available locally.
# ollama run llama3 ---> To run the server with llama3 model.
# ollama run gpt-oss ---> To run the server with gpt-oss model. Which is taking 13GB.


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