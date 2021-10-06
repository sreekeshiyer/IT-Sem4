class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
    
    def computeinterest(self):
        roi = int(input("Enter rate of interest: "))
        self.balance += (self.balance * roi)
        print("New Balance:",self.balance)

    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance)

print("""
Welcome to Bank Management System:
1. Create Account
2. Deposit 
3. Withdraw
4. Rate of Interest
5. Display Amount
6. Exit
""")

while True:
    print("\n")
    choice = input("Enter choice(1/2/3/4/5/6) :  ")
    print("\n")
    if choice in ('1', '2', '3', '4', '5', '6'):
        if choice == '1':
            name = input("Enter your name: ")
            account_no = int(input("Enter your account number: "))
            contact_no = int(input("Enter your phone number: "))
            address_field = input("Enter your address: ")
            s = Bank_Account()
        elif choice == '2':
            s.deposit()
        elif choice == '3':
            s.withdraw()
        elif choice == '4':
            s.computeinterest()
        elif choice == '5':
            s.display()
        else:
            exit()
    else:
        print("Invalid Option")
