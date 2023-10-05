from pathlib import Path


def total_salary(path):
    tot = 0.0
    fh = open(path, "r")
    line = fh.readline()
    while line:
        i, salary = line.strip().split(",")
        tot += float(salary)
        line = fh.readline()
    fh.close()
    return tot


s = Path("1.txt")
print(total_salary(s))

