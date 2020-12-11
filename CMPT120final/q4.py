# def count_numeric_chars_rec(input_string):
#     if len(input_string) == 0:
#         return 0
#     if input_string[-1] in digits:
#         return 1 + count_numeric_chars_rec(input_string[:-1])
#     return count_numeric_chars_rec(input_string[:-1])


def count_numeric_chars_rec(input_string):
    if len(input_string) == 1:
        if input_string[0] in digits:
            return 1
        else:
            return 0
    else:
        if input_string[-1] in digits:
            return 1 + count_numeric_chars_rec(input_string[:-1])
        else:
            return count_numeric_chars_rec(input_string[:-1])


digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(count_numeric_chars_rec("Hello world"))
print(count_numeric_chars_rec("Hello w1rld2"))
print(count_numeric_chars_rec("100377"))
