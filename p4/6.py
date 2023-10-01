def split_list(grade):
    if not grade:
        return ([], [])

    average = sum(grade) / len(grade)

    less = [x for x in grade if x <= average]
    more = [x for x in grade if x > average]
    return (less, more)


grade = [10, 20, 30, 40, 50]

print(split_list(grade))
