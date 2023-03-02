from abc import *
import os, os.path, shutil
employees = []
f = open('paylog.txt', 'w')

class Employee:
    def __init__(self, emp_id, first_name, last_name, \
                 address="", city="", state="", zipcode="", \
                 classification=None, salary=0, commission=0, hourly=0):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification
        self.hourly = hourly
        self.salary = salary
        self.commission = commission
        self.hourly = hourly

    def issue_payment(self):
        total = self.classification.issue_payment()
        f.write(f"Mailing {round(total, 2)} to {self.first_name} {self.last_name} at {self.address} {self.city} {self.state} {self.zipcode}\n")

    def make_hourly(self, value):
        self.classification = Hourly(value)

    def make_commissioned(self, salary, commission_rate):
        self.classification = Commissioned(commission_rate, salary)

    def make_salaried(self, value):
        self.classification = Salaried(value)

class Classification(ABC):

    @abstractmethod
    def issue_payment(self):
        pass

class Hourly(Classification):
    def __init__(self, hourly_rate):
        self._hourly_rate = hourly_rate
        self.hours_worked = []
    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        self._hourly_rate = value

    def add_timecard(self, value):
        self.hours_worked.append(value)

    def issue_payment(self):
        time_worked = 0.0
        for i in self.hours_worked:
            time_worked += i
        self.hours_worked = []
        return time_worked * self.hourly_rate



class Salaried(Classification):
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def issue_payment(self):
        return self.salary / 24

class Commissioned(Salaried, Classification):
    def __init__(self, commission_rate, salary):
        self._commission_rate = commission_rate
        self._salary = salary
        self.commissions = []

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        self._commission_rate = value

    def add_receipt(self, value):
        self.commissions.append(value)

    def issue_payment(self):
        total_commissions = 0
        for i in self.commissions:
            total_commissions += i
        self.commissions = []
        return (total_commissions * (self.commission_rate * .01)) + (self.salary / 24)



def load_employees():
    with open('employees.csv', 'r') as file:
        text = file.read()
    text = text[text.find('\n') + 1:]
    check = False
    while not check:
        for i in range(len(text)):
            if text[i].isdigit():
                break
        id = text[i:text.find(",")]
        text = text[text.find(",") + 1:]

        name = text[0:text.find(",")]
        text = text[text.find(",") + 1:]
        last_name = text[0:text.find(",")]
        text = text[text.find(",") + 1:]
        address = text[0:text.find(",")]
        text = text[text.find(",") + 1:]
        city = text[0:text.find(",")]
        text = text[text.find(",") + 1:]
        state = text[0:text.find(",")]
        text = text[text.find(",") + 1:]
        zip = text[0:text.find(",")]
        text = text[text.find(",") + 1:]
        classification = text[0:text.find(",")]
        text = text[text.find(",") + 1:]
        salary = float(text[0:text.find(",")])
        text = text[text.find(",") + 1:]
        commission = float(text[0:text.find(",")])
        text = text[text.find(",") + 1:]
        if text.find(' ') > 10:
            hourly = float(text[0:text.find('\n')])
            text = text[text.find('\n'):]
        elif text.find('...') < 10:
            hourly = float(text[0:text.find('\n')])
            text = ''
        else:
            hourly = float(text[0:text.find(" ")])
            text = text[text.find(" "):]
        employees.append(Employee(id, name, last_name, address, city, state, zip, classification, \
                              salary, commission, hourly))

        if classification == '1':
            employees[-1].classification = Salaried(salary)
        elif classification == '2':
            employees[-1].classification = Commissioned(commission, salary)
        elif classification == '3':
            employees[-1].classification = Hourly(hourly)

        if text == '':
            check = True

def process_timecards():
    with open('timecards.csv', 'r') as file:
        timecards = file.read()
    check = False
    while not check:
        temp_emp = find_employee_by_id(timecards[0:timecards.find(',')])

        timecards = timecards[timecards.find(',') + 1:]
        if temp_emp != None and isinstance(temp_emp.classification, Hourly):
            while timecards.find(',') < 5:
                if timecards.find('...') < 9:
                    temp_emp.classification.hours_worked.append(float(timecards[0:timecards.find('\n')]))
                    break
                else:
                    temp_emp.classification.hours_worked.append(float(timecards[0:timecards.find(',')]))
                    timecards = timecards[timecards.find(',') + 1:]
            temp_emp.classification.hours_worked.append(float(timecards[0:timecards.find('\n')]))
        timecards = timecards[timecards.find('\n') + 1:]

        if timecards.find('...') < 2:
            check = True

def process_receipts():
    with open('receipts.csv', 'r') as file:
        receipts = file.read()
    check = False
    while not check:
        temp_emp = find_employee_by_id(receipts[0:receipts.find(',')])

        receipts = receipts[receipts.find(',') + 1:]
        if temp_emp != None and isinstance(temp_emp.classification, Commissioned):
            while receipts.find(',') < 8:
                if receipts.find('...') < 9:
                    temp_emp.classification.commissions.append(float(receipts[0:receipts.find('\n')]))
                    break
                else:
                    temp_emp.classification.commissions.append(float(receipts[0:receipts.find(',')]))
                    receipts = receipts[receipts.find(',') + 1:]
            temp_emp.classification.commissions.append(float(receipts[0:receipts.find('\n')]))
        receipts = receipts[receipts.find('\n') + 1:]

        if receipts.find('...') < 2:
            check = True

def run_payroll():
    PAY_LOGFILE = 'payroll.txt'
    if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘payroll.txt’
        os.remove(PAY_LOGFILE)
    for emp in employees: # employees is the global list of Employee objects
        emp.issue_payment() # issue_payment calls a method in the classification
        # object to compute the pay


def find_employee_by_id(id):
    for i in employees:
        if i.emp_id == id:
            return i
    return None