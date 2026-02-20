
print("Welcome to the Simple CBT Program")

questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "answer": "b"
    },
    {
        "question": "What color is the sky on a clear day?",
        "options": ["a) Red", "b) Blue", "c) Green", "d) Yellow"],
        "answer": "b"
    },
    {
        "question": "How many legs does a spider have?",
        "options": ["a) 6", "b) 7", "c) 8", "d) 9"],
        "answer": "c"
    },
    {
        "question": "What sound does a cow make?",
        "options": ["a) Meow", "b) Bark", "c) Moo", "d) Quack"],
        "answer": "c"
    },
    {
        "question": "What is the opposite of 'hot'?",
        "options": ["a) Warm", "b) Cold", "c) Cool", "d) Boiling"],
        "answer": "b"
    },
    {
        "question":"What is my name?",
        "options":["a) Samuel", "b) Dayo", "c) Fola", "d) Dotun"],
        "answer": "a"
    }
]
score = 0

for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    for option in q['options']:
        print(option)

    user_answer = input("Enter an option from a to d: ").lower().strip()

    if user_answer == q['answer']:
        score += 1
print(f"At the end of the CBT exam, you scored {score} points.")
