from random import randint
class bank:
    def __init__(self):
            self.account_number = randint(10000000, 99999999)
            self.full_name =input("Enter your full name: ")
            self.phone_number = int(input("Enter your phone number: "))
            self.balance = 0
    
    def show_details(self):
            print(f"Account Number: {self.account_number}")
            print(f"Full Name: {self.full_name}")
            print(f"Phone Number: {self.phone_number}")
            print(f"Balance: {self.balance}\n")
    
    def chack_balance(self):
            print(f"Current Balance: {self.balance}")
    

    def deposit(self):
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"Deposited: {amount}. New balance: {self.balance}")
            else:
                print("Deposit amount must be positive.")
    
    def withdraw(self):
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance or invalid amount.")


banks=[]
while True:
      print("1. Create Account")
      print("2. show All banks details")
      print("3. deposit amount")
      print("4. withdraw amount")
      print("5. amount transfer")
      print("6. exit")
      choice=int(input("Enter your choice: "))
       
      if choice==1:
           obj=bank()
           banks.append(obj)
           print(f"Account created successfully! Your account number is {obj.account_number}")
           print(banks)
      elif choice==2:
           if len(banks)==0:
              print("No accounts available.")
           else:
                for account in banks:
                     account.show_details()
                     
      elif choice==3:
            if len(banks)==0:
              print("No accounts available.")
            else:
                account_number = int(input("Enter your account number: "))
                for account in banks:
                        if account.account_number == account_number:
                            account.deposit()
                            break
                else:
                        print("Account not found.")
      elif choice==4:
           if len(banks)==0:
              print("No accounts available.")   
           else :
                account_number = int(input("Enter your account number: "))
                for account in banks:
                        if account.account_number == account_number:
                            account.withdraw()
                            break
                else:
                        print("Account not found.")
      elif choice==5:
                if len(banks)<2:
                  print("At least two accounts are required for transfer.")
                else:
                 from_account_number = int(input("Enter your account number: "))
                 to_account_number = int(input("Enter recipient's account number: "))
                 amount = float(input("Enter amount to transfer: "))
                
                 from_account = None
                 to_account = None
                
                 for account in banks:
                    if account.account_number == from_account_number:
                        from_account = account
                    if account.account_number == to_account_number:
                        to_account = account
                
                 if from_account and to_account:
                    if 0 < amount <= from_account.balance:
                        from_account.balance -= amount
                        to_account.balance += amount
                        print(f"Transferred {amount} from account {from_account_number} to account {to_account_number}.")
                    else:
                        print("Insufficient balance or invalid amount.")
                 else:
                    print("One or both account numbers not found.") 
      elif choice==6:
            print("Exiting the program.")
            break
           
     
      
      
           
      else:
        print("Invalid choice. Please try again.")
       

 