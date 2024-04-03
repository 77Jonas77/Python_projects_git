import data
import question_model
import quizbrain

question_bank = []

if __name__ == "__main__":
    # dodawanie pytan do bazy
    for one_data in data.question_data:
        question_bank.append(
            question_model.Question(one_data["text"], one_data["answer"]))

    quiz_bank = quizbrain.QuizBrain(question_bank)
    score = 0

    # false to wszystko tylko nie true!
    while len(quiz_bank.question_list) - 1 != quiz_bank.question_nr:
        answer = quiz_bank.next_question()
        score += (1 if answer is True else 0)

    print(f"The final score: {score}")
