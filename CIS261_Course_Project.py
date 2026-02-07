#Dominick Orlando 
#CIS261 Course Project

def get_employee_name():
    name = input("Enter employee name, or type 'End' to quit: ")
    return name 
def get_dates():
    start_date = input("Enter a start date (mm/dd/yyyy): ")
    end_date = input("Enter an end date (mm/dd/yyyy): ")
    return start_date, end_date
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


def show_employee_info(start_date, end_date, name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    print("Start Date:", start_date)
    print("End Date:", end_date)
    print("Employee Name:", name)
    print("Total Hours:", hours)
    print("Hourly Rate: $", rate)
    print("Gross Pay: $", gross_pay)
    print("Tax Rate:", tax_rate)
    print("Income Tax : $", income_tax)
    print("Net Pay: $", net_pay)

def show_totals(totals_dict):
    print("Total Employees:", totals_dict["total_employees"])
    print("Total Hours:", totals_dict["total_hours"])
    print("Total Gross Pay: $", totals_dict["total_gross"])
    print("Total Tax: $", totals_dict["total_tax"])
    print("Total Net Pay: $", totals_dict["total_net"])



def process_employees(employee_list):
    totals_dict = {
        "total_employees": 0,
        "total_hours": 0.0,
        "total_gross": 0.0,
        "total_tax": 0.0,
        "total_net": 0.0
    }

    for emp in employee_list:
        start_date = emp[0]
        end_date = emp[1]
        name = emp[2]
        hours = emp[3]
        rate = emp[4]
        tax_rate = emp[5]

        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

        show_employee_info(
            start_date,
            end_date,
            name,
            hours,
            rate,
            gross_pay,
            tax_rate,
            income_tax,
            net_pay
        )

        totals_dict["total_employees"] += 1 
        totals_dict["total_hours"] += hours
        totals_dict["total_gross"] += gross_pay
        totals_dict["total_tax"] += income_tax
        totals_dict["total_net"] += net_pay
    return totals_dict 

employee_list = []
while True:
    employee_name = get_employee_name()
    if employee_name.lower() == "end":
        break 

    start_date, end_date = get_dates()
    hours = get_total_hours()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()

    employee_list.append([start_date, end_date, employee_name, hours, rate, tax_rate])

totals = process_employees(employee_list)
show_totals(totals)

