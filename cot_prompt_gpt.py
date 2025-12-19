import ollama
# The model which I have selected her is not an onprimise model, it's a cloud model.
# 


prompt = ''' Question: 

How many maximum runs a batting team and a batter individually - 
can score in an over with 2 no balls. 
Think step by step, consider max runs per legal and no ball as 6 and consider 1 extra run per no ball. 
Consider extras runs only for teams total, 
those shall not be added in batters score.
'''

response = ollama.chat(
    model="gpt-4o", #GPT-4o model
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response['message']['content'])