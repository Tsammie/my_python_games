def evaluate(answer, keywords):
    score = 0
    ans = answer.lower()
    for word,weight in keywords.items():
        if word.lower() in ans:
            score += weight
    return score

Questions = [
       
       { "question":"What is photosynthesis",
        "keywords": {
            "photosynthesis":2,
            "Light energy":1,
            "Chemical energy":1,
            "Chloroplasts":2,
            "Chlorophyll":1,
            "Carbon dioxide": 1,
            "Water":1,
            "Glucose":1,
            "Oxygen":1,
            "ATP":1,
        }
       },
       {
           "question":"What is SQI",
           "keywords":{
               "Tech":2,
               "ogbomosho":2,
               "success":1,
               "data science":1,
               "branches":1,
               "professionals":1,
               "Good staffs":3
           }
       }
]

total_score = 0
max_score = sum(sum(q["keywords"].values()) for q in Questions)

for q in Questions:
    print(q["question"])
    user_answer = input("Your answer: ")
    score = evaluate(user_answer, q["keywords"])
    total_score += score



print(f"Total Score: {total_score} out of {max_score} points.")