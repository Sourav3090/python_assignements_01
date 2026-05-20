name = input("Enter your name:  ")
start = input(f"Welcome to the KBC MR.{name} Quiz Game! Type start to begin or not to quit: ").lower()
score = 0
correct_answers = 0
skipped_questions = 0
wrong_answers = 0

if start == "start":
    q1 = input("Question 1: What is the capital of France?\nA) Berlin\nB) Madrid\nC) Paris\nD) Rome\n(Type skip to skip this question): ").lower()

    if q1 == "c" or q1 == "paris":
        print("Correct! You earned 1000 points.")
        score += 1000
        correct_answers += 1

    elif q1 == "skip":
        print("Question skipped.")
        skipped_questions += 1

    else:
        print("Wrong answer.")
        wrong_answers += 1
    q2 = input("Question 2: What is the capital of India?\nA) Mumbai\nB) New Delhi\nC) Kolkata\nD) Chennai\n(Type skip to skip this question): ").lower()

    if q2 == "b" or q2 == "new delhi":
        print("Correct! You earned 1000 more points.")
        score += 1000
        correct_answers += 1

    elif q2 == "skip":
        print("Question skipped.")
        skipped_questions += 1

    else:
        print("Wrong answer.")
        wrong_answers += 1
    q3 = input("Question 3: Which is the longest river in India?\nA) Yamuna\nB) Brahmaputra\nC) Ganga\nD) Godavari\n(Type skip to skip this question): ").lower()

    if q3 == "c" or q3 == "ganga":
        print("Correct! You earned 3000 points.")
        score += 1000
        correct_answers += 1

    elif q3 == "skip":
        print("Question skipped.")
        skipped_questions += 1

    else:
        print("Wrong answer.")
        wrong_answers += 1
    q4 = input("\nQuestion 4: Who was the first Prime Minister of India?\nA) Mahatma Gandhi\nB) Indira Gandhi\nC) Jawaharlal Nehru\nD) Sardar Vallabhbhai Patel\n(Type skip to skip this question): ").lower()

    if q4 == "c" or q4 == "jawaharlal nehru":
        print("Correct! You earned 5000 points.")
        score += 5000
        correct_answers += 1

    elif q4 == "skip":
        print("Question skipped.") 
        skipped_questions += 1

    else:
        print("Wrong answer.")
        wrong_answers += 1
    q5 = input("\nQuestion 5: What is the lower house of the Indian Parliament called?\nA) Rajya Sabha\nB) Vidhan Sabha\nC) Lok Sabha\nD) Supreme Court\n(Type skip to skip this question): ").lower()

    if q5 == "c" or q5 == "lok sabha":
        print("Correct! You earned 10000 points.")
        score += 10000
        correct_answers += 1

    elif q5 == "skip":
        print("Question skipped.")
        skipped_questions += 1

    else:
        print("Wrong answer.")
        wrong_answers += 1
    print(f"========== GAME OVER ========== \n Congo MR.{name}\n you have successfully completd the name \n and your scores are \n Total Score: {score}\n Correct Answers: {correct_answers} \nWrong Answers: {wrong_answers} \n Skipped Questions: {skipped_questions}")

elif start == "not":
    print("Thank you for visiting. Goodbye!")

else:
    print("Invalid input. Please type 'start' or 'not'.")