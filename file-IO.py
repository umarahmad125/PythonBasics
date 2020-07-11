with open('salary.txt', 'r') as rf:
    with open('outputsalary.txt', 'a') as af:
        for line in rf.readlines():
            name, salary = line.split(',')
            af.write(f"{name}\'s salary is {salary}")