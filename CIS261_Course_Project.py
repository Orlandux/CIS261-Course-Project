#Dominick Orlando 
#CIS261 Course Project

def get_employee_name():
    name = input("Enter employee name, or type 'End' to quit: ")
    return name 
def get_total_hours(): 
    hours = float(input("Enter total hours worked: ")) 
    return hours 
def get_hourly_rate():
    rate = float(input("Enter hourly rate: "))
    return rate 
def get_tax_rate():
    tax_rate = float(input("Enter income tax rate: "))
    return tax_rate

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate 
    income_tax = gross_pay * tax_rate 
    net_pay = gross_pay - income_tax 
    return gross_pay, income_tax, net_pay


def show_employee_info(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    print("Employee Name:", name)
    print("Total Hours:", hours)
    print("Hourly Rate: $", rate)
    print("Gross Pay: $", gross_pay)
    print("Tax Rate:", tax_rate)
    print("Income Tax : $", income_tax)
    print("Net Pay: $", net_pay)

def show_totals(total_employees, total_hours, total_gross, total_tax, total_net):
    print("Total Employees:", total_employees)
    print("Total Hours:", total_hours)
    print("Total Gross Pay: $:", total_gross)
    print("Total Tax: $", total_tax)
    print("Total Net Pay: $", total_net)

total_employees = 0
total_hours_all = 0.0
total_gross_all = 0.0
total_tax_all = 0.0
total_net_all = 0.0 

while True:
    employee_name = get_employee_name()
    if employee_name.lower() == "end":
        break 

    hours = get_total_hours()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()

    gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
    show_employee_info(employee_name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)

    total_employees += 1 
    total_hours_all += hours 
    total_gross_all += gross_pay
    total_tax_all += income_tax
    total_net_all += net_pay

show_totals(total_employees, total_hours_all, total_gross_all, total_tax_all, total_net_all)


