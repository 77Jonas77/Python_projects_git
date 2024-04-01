class QuizBrain:
    def __init__(self, question_list):
        self.question_nr = 0
        self.question_list = question_list

    def next_question(self):
        """Zwraca nast pytanie i czy poprawna odp"""
        curr_question = self.question_list[self.question_nr]
        answer = input(
            f"Q{self.question_nr}: {curr_question.question_text} (True / False): ")

        # tak naprawde to nie jest potrzebne (mozna bylo w ifie lower)
        answer = "True" if answer.lower() == "true" else "False"

        self.question_nr += 1
        if answer == curr_question.answer:
            print("Good answer!")
            return True
        else:
            print("Wrong answer!")
            return False
