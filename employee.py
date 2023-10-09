"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractPay, contractType, hoursWorked = 0, contractsLanded = "", commissionPay = 0, commissionType = ""):
        self.name = name
        self.hoursWorked = hoursWorked
        self.contractPay = contractPay
        self.contractType = contractType
        self.commissionType = commissionType
        self.contractsLanded = contractsLanded
        self.commissionPay = commissionPay

    def get_pay(self):
        totalPay = self.contractPay
        if self.contractType == "hourly":
            totalPay = self.hoursWorked * self.contractPay
        
        if self.commissionType == "bonus":
            totalPay = totalPay + self.commissionPay
        
        if self.commissionType == "contract":
            totalPay = totalPay + self.commissionPay * self.contractsLanded

        return totalPay

    def __str__(self):
        strn = self.name
        if self.contractType == "hourly":
            strn = strn + f' works on a contract of {self.hoursWorked} hours at {self.contractPay}/hour'
        else:
            strn = strn + f' works on a monthly salary of {self.contractPay}'

        if self.commissionType == "bonus":
            strn = strn + f' and receives a bonus commission of {self.commissionPay}'
        elif self.commissionType == "contract":
            strn = strn + f' and receives a commission for {self.contractsLanded} contract(s) at {self.commissionPay}/contract'
        else:
            strn = strn
        return strn + f'. Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, "monthly")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, "hourly", 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, "monthly", 0, 4, 200, "contract")

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, "hourly", 150, 3, 220, "contract")

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, "monthly", 0, 0, 1500, "bonus")

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, "hourly", 120, 0, 600, "bonus")
