global balance
global name
global account_no
global contact_no
global address_field

balance=0.0
name=""
account_no=-1
contact_no=0
adress_field=0

def deposit():
  global balance
  amount = float(input("Enter amount to be deposited: "))
  balance = amount + balance
  print("Amount Deposited:",amount)

def computeinterest():
  global balance
  roi = int(input("Enter rate of interest: "))
  balance += (balance * roi / 100)
  print("New Balance:",balance)

def withdraw():
  global balance
  amount = float(input("Enter amount to be withdrawn: "))
  if balance >= amount:
    balance -= amount
    print("Withdrew Amount:", amount)
  else:
    print("Insufficient balance ")

def display():
  print("Net Available Balance:",balance) 

while True:
  print("1. Create Account")
  print("2. Deposit Amount")
  print("3. Withdraw Amount")
  print("4. Rate of Interest")
  print("5. Display Amount")
  print("6. Exit")
  choice = input("Enter choice(1/2/3/4/5/6): ")
  if choice in ('1', '2', '3', '4', '5', '6'):
    if choice == '1':
      name = input("Enter your name: ")
      account_no = int(input("Enter your account number: "))
      contact_no = int(input("Enter your phone number: "))
      address_field = input("Enter your address: ")
    elif choice == '2':
      if account_no == -1:
        print("Please create account first")
      else:
        deposit()
    elif choice == '3':
      if account_no == -1:
        print("Please create account first")
      else:
        withdraw()
    elif choice == '4':
      if account_no == -1:
        print("Please create account first")
      else:
        computeinterest()
    elif choice == '5':
      if account_no == -1:
        print("Please create account first")
      else:
        display()
    else:
      exit()