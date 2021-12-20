from customer_account import CustomerAccount
from admin import Admin

accounts_list = []
admins_list = []
    
class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
        
    def loadCustomerData():
        customerdata = open("Customerdata.csv","r")
        line = customerdata.readline()
        while line != "":
            fname, lname, address, current_account_no, current_account_balance, savings_account_no, savings_account_balance, overdraftlimit, interest = line.split(",")
            customer = CustomerAccount(fname, lname, address, current_account_no, current_account_balance, savings_account_no, savings_account_balance, overdraftlimit, interest)
            accounts_list.appened(customer)
            line = customerdata.readline()
            
        admindata = open("Admindata.csv","r")
        line = admindata.readline()
        while line != "":
            fname, lname, address, user_name, password, full_rights = line.split(",")
            admin = Admin(fname, lname, address, user_name, password, full_rights)
            admins_list.appened(admin)
            line = admindata.readline()
            
    def load_bank_data(self):
        # create customers
        currentaccount_no = 1234
        savingsaccount_no = 1000
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], currentaccount_no, 5000.00,savingsaccount_no,80000.00, -1000.00, 1000.00, 1100.00)
        self.accounts_list.append(customer_1)
        
        currentaccount_no+=1
        savingsaccount_no+=1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], currentaccount_no, 3200.00, savingsaccount_no, 20000.00, 0.00, 0.00, 1110.00)    
        self.accounts_list.append(customer_2)

        currentaccount_no+=1
        savingsaccount_no+=1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], currentaccount_no, 18000.00, savingsaccount_no, 10000.00,-100.00, 0.00, 100)
        self.accounts_list.append(customer_3)

        currentaccount_no+=1
        savingsaccount_no+=1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], currentaccount_no, 40.00, savingsaccount_no, 30000.00,-10.00, 0.00, 200)
        self.accounts_list.append(customer_4)
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)
        
    def search_admins_by_name(self, admin_username):
        #STEP A.2
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break
        if found_admin == None:
                print("\n The Admin %s does not exist! Try again...\n" %admin_username)
        return found_admin
  
        
    def search_customers_by_name(self, customer_lname):
        #STEP A.3
        found_customer = None
        for s in self.accounts_list:
            username = s.get_last_name()
            if username == customer_lname:
                found_customer = s
                break
        if found_customer == None:
                print("\n The Customer %s does not exist! Try again...\n" %customer_lname)
        return found_customer
    
    def search_customers_by_account_no(self,customer_account_no):
        #STEP A.3
        found_customer = None
        for c in self.accounts_list:
            account_no = c.get_current_account_no()
            if account_no == customer_account_no:
                found_customer = c
                print("\n Customer %s found!\n" %found_customer.print_details)
                break
            if found_customer == None:
                print("\n Customer with account number: %s does not exist! Try again...\n" %customer_account_no)
        return found_customer  
    
    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        try:
            option = int(input("Choose your option: "))
            return option
        except ValueError as err:
            print(err)
            self.main_menu()
            
    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\n Thank-You for stopping by the bank!")


    def transferMoneyCurrent(self, sender_lname, receiver_lname, amount):
        sender = self.search_customers_by_name(sender_lname)
        receiver = self.search_customers_by_name(receiver_lname)
        sender.withdraw_current(amount)
        receiver.deposit_current(amount)
        print("Money has been transferred")
        
    def transferMoneySavings(self, sender_lname, receiver_lname, amount):
        sender = self.search_customers_by_name(sender_lname)
        receiver = self.search_customers_by_name(receiver_lname)
        sender.withdraw_savings(amount)
        receiver.deposit_savings(amount)
        print("Money has been transferred")
        
    def admin_login(self, username, password):
		#STEP A.1
        found_admin = self.search_admins_by_name(username)
        msg = "\n Login failed"
        if found_admin != None:
            if found_admin.get_password() == password:
                msg = "\n Login successful"
        return msg, found_admin
            
    def management_report(self):
            # list related operation - move to main.py
            i = 0
            total_overdraft = 0
            total_in_currents =0
            total_in_savings =0
            total_in_interests =0
            for x in self.accounts_list:
                i+=1
                total_overdraft += x.overdraftlimit
                total_in_currents += x.current_account_balance
                total_in_savings += x.savings_account_balance
                total_in_interests += x.interest_amount
        
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Management Report")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"Total number of customers in the system: {i}")
            print(f"Sum of all Current account balances: £{total_in_currents}")
            print(f"Sum of all Savings account balances: £{total_in_savings}")
            print(f"Sum of all Account balances: £{total_in_savings + total_in_currents}")
            print(f"Sum of all overdraft limits: £{-total_overdraft}")
            print(f"Sum of all interests: £{-total_in_interests}")
            

    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money to current account")
         print ("2) Transfer money to savings account")  
         print ("3) Customer account operations & profile settings")
         print ("4) Delete customer")
         print ("5) Print all customers detail")
         print ("6) Advanced Admin Options")
         print ("7) Management Report")
         print ("8) Sign out")
         print (" ")
         try:
             option = int(input ("Choose your option: "))
             return option
         except ValueError as err :
             print(err)
             self.admin_menu(admin_obj)
             
    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                try:
                    sender_lname = input("\n Please input sender surname: ")
                    amount = float(input("\n Please input the amount to be transferred: "))
                    receiver_lname = input("\n Please input receiver surname: ")
                    self.transferMoneyCurrent(sender_lname, receiver_lname, amount)
                except:
                    print("Error occured!")
                    self.run_admin_options(admin_obj)

            elif choice == 2:
                try:
                    sender_lname = input("\n Please input sender surname: ")
                    amount = float(input("\n Please input the amount to be transferred: "))
                    receiver_lname = input("\n Please input receiver surname: ")
                    self.transferMoneySavings(sender_lname, receiver_lname, amount)  
                except:
                    print("Error occured!")
                    print("Please double check the details you provided...")
                    self.run_admin_options(admin_obj)
                
            elif choice == 3:
                try:
                    #STEP A.4
                    customer_name = input("\n Please input customer surname :\n")
                    customer_account = self.search_customers_by_name(customer_name)
                    if customer_account != None:
                            customer_account.run_account_options()
                except:
                    print("Error occured!")
                    print("Please double check the details you provided...")
                    self.run_admin_options(admin_obj)

            elif choice == 4:
                try:
                   #STEP A.5
                   customer_name = input("\n input the customer's lastname you want to delete: ")
                   customer_account = self.search_customers_by_name(customer_name)
                   if customer_account != None:
                       self.accounts_list.remove(customer_account)
                       print("%s have been deleted successfully!" %customer_name)
                except:
                    print("Error occured!")
                    print("Please double check the details you provided...")
                    self.run_admin_options(admin_obj)
            
            elif choice == 5:
                try:
                    #STEP A.6
                    self.print_all_accounts_details()
                except:
                    print("Error occured!")
                    self.run_admin_options(admin_obj)
                
            elif choice == 6:#Admin Options
                try:
                    right=Admin.has_full_admin_right(admin_obj)
                    if right==True:
                        admin_name = input("\n Please input admin username to view options :\n")
                        admin_account = self.search_admins_by_name(admin_name)
                        if admin_account != None:
                            admin_account.run_admin_options()
                    else:
                        print("You do not have full admin rights!")
                except:
                    print("Error occured!")
                    self.run_admin_options(admin_obj)
                
            elif choice == 7:#Management Report
                try:
                    self.management_report()
                except:
                    print("Error occured!")
                    self.run_admin_options(admin_obj)
            
            elif choice == 8:
                try:
                    loop = 0
                except:
                    print("Error occured!")
                    self.run_admin_options(admin_obj)
        print ("\n Exit account operations")


    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.accounts_list:
                i+=1
                print('\n %d. ' %i, end = ' ')
                c.print_details()
                print("------------------------")
                
     


app = BankSystem()
app.run_main_options()
print("\n#####Data Being Saved#####\n")
print("\n#######Customers Data#######")
for x in range(len(app.accounts_list)): 
    print (app.accounts_list[x],)
print("\n#######Admins Data#######")
for x in range(len(app.admins_list)): 
    print (app.admins_list[x],)
    ####loading data to CSV files#####
    ###loading customer data###
with open('CustomerdataW.csv','w') as f:
    for Customers in app.accounts_list:
            f.write(str(Customers))
            f.write('\n')

with open('AdmindataW.csv','w') as f:
    for Admins in app.admins_list:
            f.write(str(Admins))
            f.write('\n')

