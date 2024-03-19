import sqlite3
import tkinter as tk

conn = sqlite3.connect('DBPRAC.db')#connects us to database
cursor = conn.cursor()#cursor executes queries one by one

cursor.execute("CREATE TABLE Users(Id INTEGER, Email TEXT, Password TEXT, Friends INTEGER)")#used to execute query you add query in paranthesis
cursor.execute("INSERT INTO Users VALUES(2,'spider@avengers.com','homeAway',112)")
cursor.execute("INSERT INTO Users VALUES(3,'iron@avengers.com','iDiedAgain',927)")
cursor.execute("INSERT INTO Users VALUES(3,'hulk@avengers.com','greenMan',27)")
cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

def Start():
    # user_email = input("Email: ")
    # user_pwd = input("Password: ")
    user_email = User_Entry.get()
    user_pwd = Pwd_Entry.get()
    cursor.execute("SELECT * FROM Users WHERE email = :email",{'email':user_email})
    user = cursor.fetchone() 

    if user is not None and user[2] == user_pwd:
        Action_Label["text"] = "Welcome home budday!"
        # print("Welcome home budday")
    else:
        # print("invalid userName o password")
        Action_Label["text"] = "invalid email or Password you better not be a hecker (⩺_⩹)"
    LogIn()


def LogIn():
    Start()

# for row in users:
#     if row[3] == 27:
#         row[3] += 1
# print(users)
# for row in users:
#     print(row)


root = tk.Tk()
root.title("Facebook Log-In Simulator")

main_frame = tk.Frame(root)
main_frame.pack()

sub_frame = tk.Frame(root)
sub_frame.pack()

log_frame = tk.Frame(root)
log_frame.pack()

feedback_frame = tk.Frame(root)
feedback_frame.pack()




title_label = tk.Label(main_frame, text="Facebook",font=("Serif", 60))
title_label.pack()

instruc_label = tk.Label(sub_frame, text="Please enter your email and password.")

email_label = tk.Label(log_frame, text="Email:")
email_label.grid(row=0, column=0)

User_Entry = tk.Entry(log_frame,width=20)
User_Entry.grid(row=0, column=1)


pwd_label = tk.Label(log_frame, text="Password:")
pwd_label.grid(row=1, column=0)

Pwd_Entry = tk.Entry(log_frame,width=20)
Pwd_Entry.grid(row=1, column=1)

LogIn_btn = tk.Button(feedback_frame, text="Log-In",command=LogIn)
LogIn_btn.pack()

Action_Label = tk.Label(feedback_frame, text=" ")
Action_Label.pack()



root.mainloop()

conn.commit()#save changes 
cursor.close()
conn.close()#close connection

Start()