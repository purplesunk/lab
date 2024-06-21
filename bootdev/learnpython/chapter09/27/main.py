def get_test_score(answer_sheet, student_answers):
    answers_right = 0

    for i in range (0, len(answer_sheet)):
        if (answer_sheet[i] == student_answers[i]):
            answers_right = answers_right + 1

    return (answers_right / len(answer_sheet)) * 100
