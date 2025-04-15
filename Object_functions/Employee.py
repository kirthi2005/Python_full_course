class Employee:
    def __init__(self, name, dept, salary, performance,is_on_probation):
        self.name = name
        self.dept = dept
        self.salary = salary
        self.is_on_probation = is_on_probation
        self.performance = performance

    def on_honor_roll(self):
        if self.performance >= 6.0:
            return True
        else:
            return False
