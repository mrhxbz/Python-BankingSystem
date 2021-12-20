import time
class CustomerAccount:
    def __init__(self, fname, lname, address, current_account_no, current_account_balance, savings_account_no, savings_account_balance, overdraftlimit, start_interest, interest_amount):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.current_account_no = current_account_no
        self.current_account_balance = float(current_account_balance)
        self.savings_account_no = savings_account_no
        self.savings_account_balance = float(savings_account_balance)
        self.overdraftlimit=float(overdraftlimit)
        self.start_interest = float(start_interest)
        self.interest_amount = float(interest_amount)
        
        
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        
    def get_address(self):
        return self.address
       
    def deposit_current(self, amount):
        self.current_account_balance+=amount
        
    def withdraw_current(self, amount):
        self.current_account_balance-=amount
        
    def deposit_savings(self,amount):
        self.savings_account_balance+=amount

    def withdraw_savings(self,amount):
        self.savings_account_balance-=amount
        
    def print_balance(self):
        print("\n Your Current account balance is:£ %.2f" %self.current_account_balance)
        print("\n Your Savings account balance is:£ %.2f" %self.savings_account_balance)
        print("\n Current Account Overdraft Limit:£ %.2f"%self.overdraftlimit)
        print("\n Total Intrest:£ %.2f"%self.interest_amount)

        
    def get_current_balance(self):
        return self.current_account_balance

    def get_savings_balance(self):
        return self.savings_account_balance
    
    def get_current_account_no(self):
        return self.current_account_no

    def get_savings_account_no(self):
        return self.savings_account_no

    def overdraftlimit(self, overdraftlimit):
        self.overdraftlimit = overdraftlimit

    def Start_interest(self):
        self.start_interest = time.time()
        
    def Intrest_calc(self):
        if self.current_account_balance<0:
            import math
            acc = self.current_account_balance
            rate = 0.03
            actual_acc = float(acc)
            interest_rate = float(rate)
            actual_time =time.time()-self.start_interest
            x = math.pow((1 + interest_rate) , actual_time)
            self.intrest_amount = actual_acc*x
            return self.intrest_amount
        else:
            self.intrest_amount = 0
            return self.intrest_amount 
        
    def __repr__(self):
        return f"{self.fname},{self.lname},{self.address[0]},{self.address[1]},{self.address[2]},{self.address[3]},{self.current_account_no},{self.current_account_balance},{self.savings_account_no},{self.savings_account_balance},{self.overdraftlimit},{self.start_interest},{self.interest_amount}"
                 
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money to current account")
        print ("2) Withdraw money from current account")
        print ("3) Deposit to savings account")
        print ("4) Withdraw from savings account")
        print ("5) Check balance")
        print ("6) Update customer name")
        print ("7) Update customer address")
        print ("8) Show customer details")
        print ("9) Back")
        print (" ")
        try:
            option = int(input ("Choose your option: "))
            return option
        except ValueError as err :
            print(err)
            self.account_menu()
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("Current Account No: %s" %self.current_account_no)
        print("Current Account Balance:£ %.2f"%self.current_account_balance)
        print("Current Account Overdraft Limit:£ %.2f"%self.overdraftlimit)
        print("Savings Account No: %s" %self.savings_account_no)
        print("Savings Account Balance:£%.2f"%self.savings_account_balance)
        print("Total Intrest:£ %.2f"%self.interest_amount)
        print("Address: %s" %self.address[0])
        print(" %s" %self.address[1])
        print(" %s" %self.address[2])
        print(" %s" %self.address[3])
        print(" ")
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1:
                #STEP A.4.1
                try:
                    amount=float(input("\n Please enter amount to be deposited in to current account: "))
                    self.deposit_current(amount)
                    print(" %.2f have been deposited" %amount)
                except:
                    print("Error occured!")
                    print("Please input float or digits...")
                    self.account_menu()
            elif choice == 2:
                try:
                    amount=float(input("\n Please enter amount to be withdraw from current account: "))
                    self.withdraw_current(amount)
                    print(" %.2f have been withdrawn" %amount)
                except:
                    print("Error occured!")
                    print("Please input float or digits...")
                    self.account_menu()
            elif choice == 3:
                #STEP A.4.1
                try:
                    amount=float(input("\n Please enter amount to be deposited in to savings account: "))
                    self.deposit_savings(amount)
                    print(" %.2f have been deposited" %amount)
                except:
                    print("Error occured!")
                    print("Please input float or digits...")
            elif choice == 4:
                try:
                    amount=float(input("\n Please enter amount to be withdraw from savings account: "))
                    self.withdraw_savings(amount)
                    print(" %.2f have been withdrawn" %amount)
                except:
                    print("Error occured!")
                    print("Please input float or digits...")
                    self.account_menu()
            elif choice == 5:
                #STEP A.4.4
                try:
                    self.print_balance()
                except:
                    print("Error occured!")
                    self.account_menu()
            elif choice == 6:
                #STEP A.4.2s
                try:
                    fname=input("\n Enter new customer first name: ")
                    self.update_first_name(fname)
                    sname = input("\nEnter new customer last name: ")
                    self.update_last_name(sname)
                    print("Name updated to: %s %s" %(fname, sname))
                except:
                    print("Error occured!")
                    print("Please double check the details you provided...")
                    self.account_menu()
            elif choice == 7:
                try:
                    newdoor=input("\nEnter new door number:")
                    newstr=input("\nEnter new street name:")
                    newcit=input("\nEnter new city name:")
                    newpost=input("\nEnter new postcode:")
                    self.address[0]=newdoor
                    self.address[1]=newstr
                    self.address[2]=newcit
                    self.address[3]=newpost
                    print("Address have been updated!")   
                except:
                    print("Error occured!")
                    print("Please check the Address details you provided...")
                    self.account_menu()
            elif choice == 8:
                try:
                    self.print_details()
                except:
                    print("Error occured!")
                    print("Please check the Address details you provided...")
                    self.account_menu()
            elif choice == 9: 
                try:
                    loop = 0
                except:
                    print("Error occured!")
                    self.account_menu()
        print ("\n Exit account operations")
        
        
