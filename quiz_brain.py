import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.current_question.text = html.unescape(self.current_question.text)
        # print("Q#",self.question_number,"Current Q is: ",self.current_question.text, "Ans= ",
        # self.current_question.answer)
        return f"Q.{self.question_number}: {self.current_question.text} (True/False): "

    def check_answer(self, user_answer):
        print("\n\nQ# ", self.question_number,
              "Correct Ans=", self.current_question.answer,
              "to: ", self.current_question.text,
              "You gave=", user_answer
              )
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            return True
        else:
            print("That's wrong.")
            return False


