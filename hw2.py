def hierarchy(workers: list):
    """
    This function returns string containing information about the hierarchy in the company
    Arguments: workers {list} -- list of lists each of which refers to one worker
    """
    department = []
    for element in workers:
        department.append(element[1])
    department_unique = list(set(department))
    division = []
    for department in department_unique:
        for element in workers:
            if department == element[1]:
                division.append({department: element[2]})
    division_list = []
    for element in division:
        division_list.append(list(element.items()))
    for department in department_unique:
        command = []
        for div in division_list:
            if div[0][0] == department:
                command.append(div[0][1])
                command_unique = set(command)
        print(f'{department} : {command_unique}')


def salary_and_number_info(workers: list):
    """
    This function returns string containing information about min, max, and average salaries in each department
    as well as info about the number of workers in each department.
    Arguments: workers {list} -- list of lists each of which refers to one worker
    """
    number = dict()
    department = []
    for element in workers:
        department.append(element[1])
    department_unique = list(set(department))
    for department in department_unique:
        for worker in workers:
            if department == worker[1] and department not in number:
                number[department] = 1
            elif department == worker[1] and department in number:
                number[department] += 1
    for department in department_unique:
        list_of_all_salaries = []
        for element in workers:
            if element[1] == department:
                list_of_all_salaries.append(int(element[5]))
        print(
            f'{department} : number = {number[department]}, '
            f'max salary = {max(list_of_all_salaries)}, '
            f'min salary = {min(list_of_all_salaries)}, '
            f'avg salary = {sum(list_of_all_salaries) / len(list_of_all_salaries)}')


def to_csv():
    """
    This function provides csv file with information regarding min,max, avg salaries
    and number of workers in each department
    Arguments: no arguments
    """
    import csv
    with open('../Corp_Summary.csv', 'r', encoding='utf8') as file:
        workers = []
        lines = file.readlines()
        for line in lines:
            worker = line.split(';')
            workers.append(worker)
    workers.pop(0)
    number = dict()
    department = []
    for element in workers:
        department.append(element[1])
    department_unique = list(set(department))
    for department in department_unique:
        for worker in workers:
            if department == worker[1] and department not in number:
                number[department] = 1
            elif department == worker[1] and department in number:
                number[department] += 1
    for department in department_unique:
        list_of_all_salaries = []
        for element in workers:
            if element[1] == department:
                list_of_all_salaries.append(int(element[5]))
    with open('departments.csv', 'w', newline='') as csvfile:
        depwriter = csv.writer(csvfile, delimiter=' ',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        depwriter.writerows(
            f'{department} : number = {number[department]}, '
            f'max salary = {max(list_of_all_salaries)}, '
            f'min salary = {min(list_of_all_salaries)}, '
            f'avg salary = {sum(list_of_all_salaries) / len(list_of_all_salaries)}')


def choose_option():
    """
    This function offers to choose one from 3 possible printouts regarding the provided data on company's workers
    Arguments: no arguments
    """
    print('Choose one option: '
          '1 - company hierarchy, '
          '2 - department info, '
          '3 - csv file from 2 ')
    option = ''
    options = [1, 2, 3]
    while option not in options:
        print('Choose: {}/{}/{}'.format(*options))
        option = int(input())
    if option == 1:
        with open('../Corp_Summary.csv', 'r', encoding='utf8') as file:
            workers = []
            lines = file.readlines()
            for line in lines:
                worker = line.split(';')
                workers.append(worker)
        workers.pop(0)
        return hierarchy(workers)
    elif option == 2:
        with open('../Corp_Summary.csv', 'r', encoding='utf8') as file:
            workers = []
            lines = file.readlines()
            for line in lines:
                worker = line.split(';')
                workers.append(worker)
        workers.pop(0)
        return salary_and_number_info(workers)
    else:
        return to_csv()


if __name__ == '__main__':
    choose_option()
