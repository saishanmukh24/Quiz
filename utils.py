def ask_question(question_data, number):
    print(f"\nQuestion {number}: {question_data['question']}")
    options = question_data['options']
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    correct_option = question_data['answer']
    if options[answer - 1] == correct_option:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong. The correct answer was: {correct_option}")
        return False

def show_final_score(score, total):
    print("\n🎉 Quiz Completed!")
    print(f"Your Score: {score} / {total}")
    percentage = (score / total) * 100
    print(f"Accuracy: {percentage:.2f}%")
