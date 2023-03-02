''' payroll.py main function Illustrates the payroll module. '''
from payroll import *
import os, os.path, shutil


def main():
    load_employees()  # You will implement the first three of these functions
    process_timecards()
    process_receipts()
    run_payroll()  # This function is given to you in Part 2

    # Save copy of payroll file; delete old file
    shutil.copyfile('paylog.txt', 'paylog_old.txt')
    if os.path.exists('paylog.txt'):
        # os.remove('paylog.txt')  # You define PAY_LOGFILE = ‘paylog.txt’ globally
        pass

    # Change Issie Scholard to Salaried by changing the Employee object:
    emp = find_employee_by_id('51-4678119')
    emp.make_salaried(134386.51)
    emp.issue_payment()

    # Change Reynard,Lorenzin to Commissioned; add some receipts
    emp = find_employee_by_id('11-0469486')
    emp.make_commissioned(50005.50, 27)
    clas = emp.classification
    clas.add_receipt(1109.73)
    clas.add_receipt(746.10)
    emp.issue_payment()
    # Change Jed Netti to Hourly; add some hour entries
    emp = find_employee_by_id('68-9609244')
    emp.make_hourly(47)
    clas = emp.classification
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    emp.issue_payment()


if __name__ == '__main__':
    main()