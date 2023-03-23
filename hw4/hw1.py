"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are 
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""
import datetime
from collections import defaultdict


class DeadlineError(Exception):
    pass


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Person):
    def do_homework(self, homework, solution):
        if homework.is_active():
            return HomeworkResult(homework, solution, self)
        raise DeadlineError('You are late')


class Teacher(Person):
    homework_done = defaultdict()

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    def check_homework(self, hw_result):
        if len(hw_result.solution) > 5:
            self.homework_done[hw_result.homework] = hw_result.solution
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework:
            del cls.homework_done[homework]
        else:
            cls.homework_done = defaultdict()


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.today()

    def is_active(self):
        return datetime.datetime.today() - self.created < self.deadline


class HomeworkResult:
    def __init__(self, homework, solution, author):
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.today()