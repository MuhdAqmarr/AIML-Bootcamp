# class Emp:
#     def display(self):
#         print('Display of Employee Class')

# obj = Emp()
# obj.display()

class Emp:
    def reg(self, eid, ename):
        self.eid=eid
        self.ename=ename
    
    def display(self):
        # print('Employee Details:')
        print(f'Employee ID: {self.eid}, Employee Name: {self.ename}')

e1 = Emp()
e2 = Emp()
e3 = Emp()
e1.reg(101,'Sam')
e2.reg(102,'Neha')
e3.reg(103,'Jai')
print('First Employee Details')
e1.display()
print('Second Employee Details')
e2.display()
print('Third Employee Details')
e3.display()

# for i in range(3):
#     e1 = Emp()
#     eid=int(input('Enter Employee ID: \t'))
#     ename=input('Enter Employee Name: \t')
#     e1.reg(eid, ename)
#     e1.display()