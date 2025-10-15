# class Account:
#     def __init__(self,ac_holder,bal):
#         self.ac_holder=ac_holder
#         self.bal=bal

#     def deposit(self, amount):
#            self.bal+=amount
#            print('Balance afer deposit',self.bal)

#     def withdraw(self,amount):
#          if(self.bal>=amount):
#               self.bal-=amount
#               print('Balance after Withdraw: ',self.bal) 
#          else:
#               print('Insufficient amount in account')
#               print ('Transcation Failed!!!')
#     def show(self):
#          print(f'Account Holder Name: {self.ac_holder} Account Balance {self.bal}')

# # ac1=Account('sameer',50000)
# # ac2=Account('Chang',14000) 
# # ac1.show()
# # ac2.show() 
# ac1=Account('sameer',50000)

# ac1.show()
# wamount=float(input('Enter amount to withdraw'))
# ac1.withdraw(wamount)

# class Account:
#     def __init__(self, balance,ac_holder):
#         self.balance = balance
#         self.ac_holder=ac_holder

#     def get_balance(self):
#         return self.balance
    
    

# acc = Account(1000,'Sam')
# acc.balance=34000
# print(acc._balance)


class Account:
    def __init__(self,ac_holder,bal):
        self.ac_holder=ac_holder
        self.bal=bal

    def deposit(self, amount):
           self.bal+=amount
           print('Balance afer deposit',self.bal)

    def withdraw(self,amount):
         if(self.bal>=amount):
              self.bal-=amount
              print('Balance after Withdraw: ',self.bal) 
         else:
              print('Insufficient amount in account')
              print ('Transcation Failed!!!')
    def show(self):
         print(f'Account Holder Name: {self.ac_holder} Account Balance {self.bal}')

ac=Account('Sam',15000)
ac.show()
print('Please choose\n 1.Deposit 2.Withdraw 3.Balance Info')
op=int(input())

if(op==1):
    damount=float(input('Enter amount to deposit: '))
    ac.deposit(damount)
elif(op==2):
     damount=float(input('Enter amount to withdraw: '))
     ac.withdraw(damount) 
elif(op==3):
     ac.show()     
else:
     print('Wrong Choice')       
