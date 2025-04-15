from Question import Question

question_prompts = [
    "Is Python high level language?\n(a) True\n(b) False\n\n",
    "Is Python an interpreted language?\n(a) True\n(b) False\n\n",
    "Is Python a dynamically typed language?\n(a) True\n(b) False\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"a"),
    Question(question_prompts[2],"a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got "+ str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)
