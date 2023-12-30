from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from joker import Joker

if __name__ == '__main__':
    joker = Joker()
    joke = joker.joke()
    print(joke)

    puns = joker.puns(5)
    for pun in puns:
        print(pun)
    employees = get_employees()
    salary = calculate_salary()
    print(employees, salary, datetime.now())
