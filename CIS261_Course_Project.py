#Dominick Orlando 
#CIS261 Course Project

FILENAME = "employee_info.txt"
USER_FILE = "user_login.txt"

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization


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

def valid_date(date_str):
    if len(date_str) != 10:
        return False
    if date_str[2] != "/" or date_str[5] != "/":
        return False
    m = date_str[0:2]
    d = date_str[3:5]
    y = date_str[6:10]
    if not (m.isdigit() and d.isdigit() and y.isdigit()):
        return False
    return True

def get_from_date():
    while True:
        from_date = input("Enter 'From' Date (mm/dd/yyyy) or 'All': ")
        if from_date == "All":
            return "All"
        if valid_date(from_date):
            return from_date
        print("Invalid date. Try again.")

def run_report(login_obj):
    print("Logged in User:", login_obj.user_id)
    print("Authorization:", login_obj.authorization) 
    print()

    from_date = get_from_date()

        
    totals = {
        "total_employees": 0,
        "total_hours": 0.0,
        "total_gross": 0.0,
        "total_tax": 0.0,
        "total_net": 0.0
    }

    try:
        file = open(FILENAME, "r")
    except:
        print("No data file found.")
        return
    for line in file:
        line = line.strip()
        if line == "":
            continue

        parts = line.split("|")

        start = parts [0]

        if from_date != "All" and start != from_date:
            continue
        end = parts[1]
        name = parts[2]
        hours = float(parts[3])
        rate = float(parts[4])
        tax_rate = float(parts[5])

        gross, tax, net = calculate_pay(hours, rate, tax_rate)
        show_employee_info(start, end, name, hours, rate, gross, tax_rate, tax, net)

        totals["total_employees"] += 1 
        totals["total_hours"] += hours 
        totals["total_gross"] += gross
        totals["total_tax"] += tax
        totals["total_net"] += net 

    file.close()
    show_totals(totals)

def login():
    user_ids = []
    passwords = []
    auths = []

    try:
        file = open(USER_FILE, "r")
    except:
        print("User's login data not detected.")
        return None
    
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split("|")
        user_ids.append(parts[0])
        passwords.append(parts[1])
        auths.append(parts[2])

    file.close()
    
    user_id = input("Enter User ID: ")

    if user_id not in user_ids:
        print("User ID not detected.")
        return None
    
    password = input("Enter password: ")

    index = user_ids.index(user_id)

    if password != passwords[index]:
        print("Password is incorrect.")
        return None
    
    return Login(user_id, password, auths[index])

def enter_employee_data():
    file = open(FILENAME, "a")

    while True:
        employee_name = get_employee_name()
        if employee_name.lower() == "end":
            break
        start_date, end_date = get_dates()
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        record = start_date + "|" + end_date + "|" + employee_name + "|" + str(hours) + "|" + str(rate) + "|" + str(tax_rate)
        file.write(record + "\n")

    file.close()


login_obj = login()

if login_obj != None:

    if login_obj.authorization == "Admin":
        enter_employee_data()
        run_report(login_obj)

    else:
        run_report(login_obj)

