def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_lenght(doc):
            sequence_count = 0
            strings = doc.split("\n")
            for s in strings:
                if sequence in s:
                    sequence_count = sequence_count + 1
            return sequence_count
        return with_lenght

    return with_char
