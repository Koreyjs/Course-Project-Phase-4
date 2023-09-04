from datetime import datetime

def CreateUsers():
    print("Create users, passwords, and roles")
    UserFile = open("Users.txt", "+a")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        UserPassword = GetUserPassword()
        UserRole = GetUserRole()
        
        UserDetail = username + "|" + UserPassword + "|" + UserRole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    PrintUserInformation()
    
def GetUserName():
    username = input("Enter a username or 'End' to quit: ")
    return username

def GetUserPassword():
    password = input("Enter password: ")
    return password

def GetUserRole():
    UserRole = input("Enter a role (Admin or User): ")
    while True:
        if (UserRole.upper() == "ADMIN" or UserRole.upper() == "USER"):
            return UserRole
        else:
            UserRole = input("Enter a role (Admin or User): ")
            
def PrintUserInformation():
    UserFile = open("Users.txt" , "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        UserPassword = UserList[1]
        UserRole = UserList[2]
        print("User Name: ", username, "Password: ", UserPassword, "Role:", UserRole)
        
def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    username = input("Enter a username: ")
    UserPassword = input("Enter Password: ")
    UserRole = "NONE"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, username, UserPassword
        UserDetail = UserDetail.replace("\n", "")
        
        UserList = UserDetail.split("|")
        if username == UserList[0] and UserPassword == UserList[1]:
            UserRole = UserList[2]
            return UserRole, username
        
    return UserRole, username

def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY:   ")
    endDate = input("Please enter end date in the following format MM/DD/YYY:   ")
    return fromDate, endDate
 
def getEmpname():
    empname = input("Enter Employee Name (Enter 'END' to start report): ")
    return empname

def getHoursWorked():
    hours = float(input("Enter Hours:   "))
    return hours


def getHourlyRate():
    hourlyrate = float(input("Enter Hourly Rate:    ")) 
    return hourlyrate

def getTaxRate():
    taxrate = float(input("Enter Tax Rate:  "))
    taxrate = taxrate / 100
    return taxrate

def CalcTaxAndNetPay(hours,hourlyrate,taxrate):
    gpay = hours * hourlyrate
    incometax = gpay * taxrate
    netpay = gpay - incometax
    return gpay, incometax, netpay
                                     
def printinfo(DetailList):
    totalemployee = 0
    totalhours = 0.00
    totalgrosspay = 0.00
    totaltax = 0.00
    totalnetpay = 0.00
    EmpFile = open("Employees.txt", "r")
    while True:
        rundate = input("Enter a start date for report (MM/DD/YYYY) or 'ALL' for all data: ")
        if (rundate.upper() == "ALL"):
            break                 
        try:
            rundate = datetime.striptime (rundate, "%m/%d/%y")
        except ValueError:
            print("Invalid date forrmat. Try again. ")
            print()
            continue
        
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "")
        EmpList = EmpDetail.split("|")
        fromDate = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate =  datetime.striptime(fromDate, "m/%d/%y")
            if (checkdate < rundate):
                continue
        endDate  = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate = float(EmpList[4])
        taxrate = float(EmpList[5])
        gpay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromDate, endDate, empname,f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{gpay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        totalemployee += 1
        totalhours += hours
        totalgrosspay += gpay
        totaltax += incometax
        totalnetpay += netpay
        empTotals["totEmp"] = totalemployee
        empTotals["totHours"] = totalhours
        empTotals["totGross"] = totalgrosspay
        empTotals["totTax"] = totaltax
        empTotals["totNet"] = totalnetpay
        DetailsPrinted = True
        
    if (DetailsPrinted):
        PrintTotals(empTotals)
    else:
        print("NO detailed information to print")
        
def PrintTotals(empTotals):
    print()
    print(f"Total Number Of Employees:  {empTotals['totEmp']}")
    print(f"Total Hours of Employees:   {empTotals['totHours']:,.2f}")
    print(f"Total Gross Pay of Employees: {empTotals['totGross']:,.2f}")
    print(f"Total Tax of Employees: {empTotals['totTax']:,.1%}")
    print(f"Total Net Pay of Employees: {empTotals['totNet']:,.2f}")

if __name__ == "__main__":
    CreateUsers()
    print()
    print("Data Entry")
    UserRole, username = Login()
    DetailsPrinted = False
    empTotals = {}
    if (UserRole.upper() == "NONE"):
        print(username, " is invalid.")
        
    else:
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("Employees.txt", "a+")
            while True:
                empname = getEmpname()
                if (empname.upper() == "END"):
                    break
                fromDate, endDate = getDatesWorked()
                hours = getHoursWorked()
                hourlyrate = getHourlyRate()
                taxrate = getTaxRate()
                EmpDetail = fromDate + "|" + endDate + "|" +  empname + "|" + str(hours) + "|" +str(hourlyrate) + "|" + str(taxrate) + "\n"
                EmpFile.write(EmpDetail)
                
            EmpFile.close()
            
        printinfo(DetailsPrinted)
                
                
        
