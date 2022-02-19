from question_model import Question
from data_1 import question_data
from quiz_brain import QuizBrain

question_bank = []

for q_data in question_data:
	question_text = q_data["question"]  # ["text"]
	question_answer = q_data["correct_answer"]  # ["answer"]
	question_bank.append(Question(question_text, question_answer))
	# question_bank.append(Question(q_data["text"], q_data["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# have_questions = True
# while have_questions:
# 	quiz.next_question()
# 	if not quiz.still_has_questions():
# 		print(f"You've completed the quiz.\nYour final score was: {quiz.score}")
# 		have_questions = False