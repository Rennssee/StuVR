def write_employees_to_file(employee_list, path):
    file = open(path, "w")
    for inr_list in employee_list:
        for employee in inr_list:
            file.write(employee + "\n")
    file.close()


lis = [["Robert Stivenson,28", "Alex Denver,30"], ["Drake Mikelsson,19"], ["VR,27"]]
pa = "test.txt"
write_employees_to_file(lis, pa)
