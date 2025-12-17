import ollama
# Chain of Thought Prompting Example

#Question 1: How many maximum runs a batting team can score in an over with 2 no balls? Let's think step by step. /// we got wrong answer
#Question 2: How many maximum runs a batting team can score in an over with 2 no balls? think step by step, consider max runs per legal and no ball as 6 and consider extra run per no ball. /// we got wrong answer
#Question 3: How many maximum runs a batting team can score in an over with 2 no balls? think step by step, consider max runs per legal and for no ball also as 6 and consider extra run per no ball. /// 
#Question 4: How many maximum runs a batting team can score in an over with 2 no balls? think step by step, consider max runs per legal ball is 6 and for each no ball as 6 and consider 1 extra run per no ball.
#Question 5: How many maximum runs a batting team and a batter individually - can score in an over with 2 no balls. Think step by step, consider max runs per legal and no ball as 6 and consider 1 extra run per no ball.
#Question 6: How many maximum runs a batting team and a batter individually - can score in an over with 2 no balls. Think step by step, consider max runs per legal and no ball as 6 and consider 1 extra run per no ball. Consider extras runs only for teams total, those shall not be added in batters score.


prompt = ''' Question: 

How many maximum runs a batting team and a batter individually - can score in an over with 2 no balls. Think step by step, consider max runs per legal and no ball as 6 and consider 1 extra run per no ball. Consider extras runs only for teams total, those shall not be added in batters score.
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