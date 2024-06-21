def get_test_score(answer_sheet, student_answers):
    student_name = student_answers.pop(0)
    answers_right = 0

    for i in range(0, len(answer_sheet)):
        if (student_answers[i] == answer_sheet[i]):
            answers_right = answers_right + 1

    percentage = answers_right / len(answer_sheet) * 100

    return student_name, percentage
