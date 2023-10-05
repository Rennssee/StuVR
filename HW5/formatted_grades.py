grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    fina_form = []
    step = 1
    for name, grade in students.items():
        line = f"{step:>4}|{name:<10}|{grade:^5}|{grades[grade]:^5}"
        fina_form.append(line)
        step += 1
    return fina_form


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
for el in formatted_grades(students):
    print(el)
