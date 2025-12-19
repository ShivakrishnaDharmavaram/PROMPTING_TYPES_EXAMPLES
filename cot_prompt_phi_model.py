import ollama
# Chain of Thought Prompting Example with phi model


prompt = ''' Question: 

How many maximum runs a batting team and a batter individually - 
can score in an over with 2 no balls. 
Think step by step, consider max runs per legal and no ball as 6 and consider 1 extra run per no ball. 
Consider extras runs only for teams total, 
those shall not be added in batters score.
'''

response = ollama.chat(
    model="phi", #SLM model which is not supported by python version above 3.10 and we haven't pulled it locally
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response['message']['content'])