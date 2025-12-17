import ollama

messages = [
    {"role": "user", "content" : "You are a helpful assistant."},
    {"role": "user", "content": "What is machine learning?"},
    {"role": "assistant", "content": "Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computers to perform specific tasks without explicit instructions. It involves training models on data to recognize patterns and make predictions or decisions based on new input data."},
    {"role": "user", "content": "Explain supervised and unsupervised learning."}
    ]

response = ollama.chat(
    model="llama3", #LLM model 
    messages= messages
)

print(response['message']['content'])