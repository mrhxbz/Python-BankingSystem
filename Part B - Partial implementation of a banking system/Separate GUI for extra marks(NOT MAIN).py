from tkinter import *

window = Tk()
varKeep = IntVar()
def cmdLogin():
    print(f"{enterUserID.get()}, {enterpassword.get()}, {varKeep.get()}")
window.title("BCU Banking")
window.geometry("470x300")
window.configure(bg="black")

lblTitle = Label(window,
                 text= "Welcome to BCU Bank",
                 font=("Times New Roman", 24, "bold"),
                 bg= "black",
                 fg= "white")
lblTitle.grid(row=0, column=0, columnspan=2)

#UserID
lblUserID = Label(window,
                 text= "UserID",
                 font=("Times New Roman", 12, "bold"),
                 bg= "black",
                 fg= "white")
lblUserID.grid(row=1, column=0, sticky=W)

enterUserID = Entry()
enterUserID.grid(row=1, column=1)
#pasword
lblpassword = Label(window,
                 text= "Password",
                 font=("Times New Roman", 12, "bold"),
                 bg= "black",
                 fg= "white")
lblpassword.grid(row=2, column=0, sticky=W)
enterpassword = Entry()
enterpassword.grid(row=2, column=1, pady=(1,1))

chkKeep = Checkbutton(text= 'Keep me Logged in',
                  variable=varKeep,
                  bg='black',
                  fg='red')
chkKeep.grid(row=3, column=0)
#button
btnLogin = Button(window, text='Login',
                  width=10, 
                  height=2,
                  command = cmdLogin)
btnLogin.grid(row=3, column=1, sticky=W)
window.mainloop()
