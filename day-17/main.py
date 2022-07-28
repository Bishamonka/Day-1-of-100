from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    question = Question(key['question'], key['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
quiz.game_over()