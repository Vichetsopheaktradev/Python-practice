import random
def automated_decision_maker(question):
    responses = [
        "Yes", "No", "Maybe", "Ask again later", "Definitely", "I don't think so"
    ]
    print(f"Question: {question}")
    decision = random.choice(responses)
    return decision

question = input("What is your question? ")
decision = automated_decision_maker(question)
print("Decision:", decision)
