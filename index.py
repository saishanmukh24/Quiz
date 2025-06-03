import json
import random
from utils import ask_question, show_final_score

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def start_quiz():
    questions = load_questions('src/questions.json')
    random.shuffle(questions)

    score = 0
    for idx, q in enumerate(questions, start=1):
        correct = ask_question(q, idx)
        if correct:
            score += 1

    show_final_score(score, len(questions))

if __name__ == '__main__':
    start_quiz()
