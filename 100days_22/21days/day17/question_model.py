"""Pytanie wraz z opdowiedzia"""


class Question:
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

    def check_answer(self, answer):
        """Checking if answer is correct"""
        return answer == self.answer
