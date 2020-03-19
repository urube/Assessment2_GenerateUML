"""
classes with inheritance

"""
# from abstract_classes import Hospital


class Hospital(object):
    """
    Parent class
    """
    def __init__(self, employee_name, employee_id):
        self.name = employee_name
        self.id = employee_id

    def __str__(self):
        print(f"I am {self.name}. I am a {self.id}.")


class Doctor(Hospital):
    """
    child class 1
    """
    def __init__(self, employee_name, employee_id, a_salary):
        super().__init__(employee_name, employee_id)
        self.salary = a_salary
        # self.hour = work_hour

    def annual_pay(self):
        print(self.salary)

    def calculate_payroll(self):
        print(f'Calculating Payroll of {self.name}')
        print('===================================================================')
        print(f'Payroll for: {self.id}, {self.name}, is {self.salary} annually.')
        print('=================================================================== \n')


class Nurse(Hospital):
    """
    child class 2
    """
    def __init__(self,employee_name, employee_id, a_salary):
        super().__init__(employee_name,employee_id)
        self.salary = a_salary

    def annual_pay(self):
        print(self.salary)

    def calculate_payroll(self):
        print(f'Calculating Payroll of {self.name}')
        print('===================================================================')
        print(f'Payroll for: {self.id}, {self.name}, is {self.salary} annually.')
        print('=================================================================== \n')


if __name__ == "__main__":
    import pickle
    with open('output.pickle', 'wb') as f:
        pickle.dump(Doctor, f)
    with open('output.pickle', 'rb') as f:
        data = pickle.load(f)

    d = Doctor("John Wick", "Doctor", 138000)
    d.__str__()
    d.calculate_payroll()
    n = Nurse("Zara Noor", "Nurse", 60000)
    n.__str__()
    n.calculate_payroll()


