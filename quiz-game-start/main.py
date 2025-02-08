import data
import question_model
import quiz_brain
print("Bienvenue dans le quiz !")

list_question = []
for element in data.question_data:
    question = question_model.question(element["text"],element["answer"])
    list_question.append(question)

partie = quiz_brain.quiz(list_question)

partie.lancer_quiz()