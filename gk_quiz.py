questions=[
    {"question":"What is the capital of India?",
    "options":["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
    "answer":"B"
    }, 
    {"question":"Which planet is known as the Red Planet?",
        "options":["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer":"C"
    },
    {"question":"Who developed python?",
        "options":["A. Guido van Rossum", "B. James Gosling", "C. Dennis Ritchie", "D. Brendan Eich"],
        "answer":"A"
    },
    {"question":"Which is the largest ocean?",
        "options":["A. Atlantic Ocean", "B. Pacific Ocean", "C. Indian Ocean", "D. Arctic Ocean"],
        "answer":"B"
    },
    {"question":"How many days are there in a leap year?",
        "options":["A. 365", "B. 366", "C. 364", "D. 367"],
        "answer":"B"
    },
]
score=0
for q in questions:
    print("\n"+q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").upper()
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("correct answer is: " + q["answer"])
print("\n Quiz completed!")
print(f"\nYour final score is: {score}/{len(questions)}")
percentage = (score / len(questions)) * 100
print(f"Your percentage is: {percentage}%")