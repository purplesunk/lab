def filter_messages(messages):
    filtered_messages = []
    dang_count_per_message = []

    for message in messages:
        word_array = message.split()
        filtered_message = []
        dang_count = 0

        for word in word_array:
            if (word == "dang"):
                dang_count = dang_count + 1
            else:
                filtered_message.append(word)

        filtered_messages.append(" ".join(filtered_message))
        dang_count_per_message.append(dang_count)

    return filtered_messages, dang_count_per_message
