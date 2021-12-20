class Admin:
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
    
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
    
    def set_username(self, uname):
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights
    
    def __repr__(self):
        return f"{self.fname},{self.lname},{self.address[0]},{self.address[1]},{self.address[2]},{self.address[3]},{self.user_name},{self.password},{self.full_rights}"
    
    def print_admindetails(self):
        #STEP A.4.3
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("User name: %s" %self.user_name)
        print("Password: %s" %self.password)
        print("Address: %s" %self.address[0])
        print(" %s" %self.address[1])
        print(" %s" %self.address[2])
        print(" %s" %self.address[3])
        if self.full_admin_rights == 1:
                adminright = "Full"
        else:
                adminright = "Partial"
        print("Full Admin Rights: %s(%s)" %(self.full_admin_rights,adminright))
        print(" ")
    
    def admin_menu(self):
         print (" ")
         print ("Avilable options are:")
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Update name")
         print ("2) Update address")
         print ("3) Update login details")
         print ("4) Update Admin Rights")
         print ("5) Show Admin details")
         print ("6) Back")
         print (" ")
         option = int(input ("Choose your option: "))
         return option

    def run_admin_options(self):
            loop = 1
            while loop == 1:
                choice = self.admin_menu()
                if choice == 1:
                    try:
                        fname=input("\n Enter new admin first name: ")
                        self.update_first_name(fname)
                        sname = input("\nEnter new admin last name: ")
                        self.update_last_name(sname)
                    except:
                        print("Error occured!")
                        print("Please check the admin details you provided...")
                        self.admin_menu()
                        
                elif choice == 2:
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
                        self.admin_menu()
                        
                elif choice == 3:
                    try:
                        newlogin=input("\n Enter your new username: ")
                        self.set_username(newlogin)
                        newpassword = input("\n Enter your new password: ")
                        self.update_password(newpassword)
                    except:
                        print("Error occured!")
                        print("Please double check the details...")
                        self.admin_menu()
                        
                elif choice == 4:
                    try:
                        updateright=int(input("\n Enter 1 for full rights or 2 for partial rights: "))
                        self.set_full_admin_right(updateright)
                    except:
                        print("Error occured!")
                        print("Please follow the instructions provided...")
                        self.admin_menu()
                
                elif choice == 5:
                    try:
                        self.print_admindetails()
                    except:
                        print("Error occured!")
                        self.admin_menu()
                    
                elif choice == 6:
                    try:
                        loop = 0 
                    except:
                        print("Error occured!")
                        self.admin_menu()
            print ("\n Exit account operations")
            