
from itertools import count


def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name,salary, *_ = line.strip().split(',')
                    salary = int(salary)
                    total += salary
                    count += 1
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        return 0, 0
    
    average = total / count if count else 0
    
    return total, average
            
salary = total_salary('salaries_people.txt')
print(f'Total Salary: {salary[0]}')
print(f'Average Salary: {salary[1]:g}')