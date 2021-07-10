class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        answer = input(f"Q{self.question_number+1} '{self.question_list[self.question_number].text}' [True/False]: ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
            print(f"Current score: {self.score}/{self.question_number}")

        else:
            print(f"Sorry, that's wrong, correct answer: {correct_answer}")
            print(f"Current score: {self.score}/{self.question_number}")
        print("\n")