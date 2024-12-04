#Exercise 8 : Star Wars Quiz

def ask_questions(data):
    correct = 0
    incorrect = 0
    wrong_answers = []

    print("Welcome to the Star Wars Quiz!")
    for item in data:
        user_answer = input(f"{item['question']}").strip()
        if user_answer.lower() == item["answer"].lower():
            correct += 1
            print("correct!\n")
        else:
            incorrect += 1
            wrong_answers.append({
             "question": item["question"],
             "your_answer": user_answer,
             "correct_answer": item["answer"]   
            })
            print(f"Incorrect, the correct is {item['answer']}.\n")

    return correct, incorrect, wrong_answers

def display_results(correct, incorrect, wrong_answers):
    print("\nQuiz Results:")
    print(f"Correct Answers: {correct}")
    print(f"incorrect Answers: {incorrect}\n")

    if wrong_answers:
        print("Here are the questions you answered incorrectly:")
        for item in wrong_answers:
            print(f"Question: {item['question']}")
            print(f"your answer: {item['your answer']}")
            print(f"Correct Answer: {item['correct_answer']}\n")
    else:
        print("Perfect score!")

    if incorrect > 3:
        print("You got more than 3 answers wrong. Would you like to try again? (yes/no)")
        retry = input().strip().lower()
        if retry == 'yes':
            main()

def main():
    data = [
       {
            "question": "What is Baby Yoda's real name?",
            "answer": "Grogu"
        },
        {
            "question": "Where did Obi-Wan take Luke after his birth?",
            "answer": "Tatooine"
        },
        {
            "question": "What year did the first Star Wars movie come out?",
            "answer": "1977"
        },
        {
            "question": "Who built C-3PO?",
            "answer": "Anakin Skywalker"
        },
        {
            "question": "Anakin Skywalker grew up to be who?",
            "answer": "Darth Vader"
        },
        {
            "question": "What species is Chewbacca?",
            "answer": "Wookiee"} 
    ]

    correct, incorrect, worng_answers = ask_questions(data)
    display_results(correct, incorrect, wrong_answers)

if __name__ == "__main__":
    main()