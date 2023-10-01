grades_digit = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
Grades_word = {
    "F": "Unsatisfactorily",
    "FX": "Unsatisfactorily",
    "E": "Enough",
    "D": "Satisfactorily",
    "C": "Good",
    "B": "Very good",
    "A": "Perfectly",
}


def get_grade(key):
    a = grades_digit.get(key, None)
    return a


def get_description(key):
    b = Grades_word.get(key, None)
    return b


print(get_grade("FX"))

print(get_description("A"))
