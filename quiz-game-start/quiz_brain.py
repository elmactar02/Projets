import question_model

class quiz:
    def __init__(self, list_questions):
        self.questions = list_questions
        self.score = 0

    def lancer_quiz(self):
        for elem in self.questions :
            print("Votre score est de "+ str(self.score))
            reponse = input(elem.text + " : ")
            if reponse == elem.answer.lower():
                self.score +=1
            else:
                print("Dommage vôtre score final est "+ str(self.score))
                break 
        if self.score == len(self.questions):
            print("Vous avez reussi le quiz ! ")
            print("Votre score final est de "+str(self.score))
