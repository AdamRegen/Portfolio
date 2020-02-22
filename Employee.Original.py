class Employee:
    empNo = 0
    payIncrease = 1.04

    def __init__(self,fname,lname,pay):
        self.fname = fname

        self.lname = lname

        self.pay = pay

        self.empNo = Employee.empNo

        Employee.empNo += 1

    def email(self):
        return(self.first + self.second +"@company.com")

    def increasePay(self):
        self.pay = self.pay * Employee.payIncrease

    def fullname(self):
        return('{}{}'.format(self.fname,self.lname))

emp1 = Employee('Lester','Square',40000)

print(emp1.fname)

print(emp1.__dict__)

print(Employee.__dict__)

print(emp1.email())

print(emp1.pay)

emp1.increasePay()

print(emp1.pay)
