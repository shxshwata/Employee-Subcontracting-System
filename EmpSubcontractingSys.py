import random
import mysql.connector as mys
import os
d_uid="Admin"  #default userID
d_pw="1234"    #default password
db=mys.connect(host='localhost', user='root',passwd='Isgx#007',database='EmpSubcontractingSys')
p=db.cursor()
def login():
    print("------------------------------------------------------------")
    print("Please enter User ID and Password to login as Administrator.")
    uid=input("User ID: ")
    pw=input("PASSWORD: ")
    print("------------------------------------------------------------")
    print()
    print()
    if uid==d_uid and pw==d_pw:
        print("Welcome!")
        menu()
    else:
        print("Data entered is wrong.")
        c=input("Do you want to enter password again?(y/n): ")
        if c=='y':
            login()
        else:
            print("Program Execution Finished.")
            print("Thank you.")
def menu():
    _=os.system('clear')
    print()
    print()
    print("-------------------------MENU------------------------------")
    print("1. VIEW FULL RECORDS")
    print("2. VIEW CURRENT STATUS OF EMPLOYEES")
    print("3. VIEW AND ACCEPT JOB APPLICANTS")
    print("4. EDIT RECORDS")
    print("5. EDIT STATUS OF EMPLOYEES")
    print("------------------------------------------------------------")
    i=int(input("Enter your choice: "))
    if i>5:
        print("Invalid Choice Entered.")
        requestmenu()
    else:
        choice(i)
        
def choice(i):
    if i==1:
        viewfullrec()
    elif i==2:
        viewempstatus()
    elif i==3:
        jobapplicants()
    elif i==4:
        editfullrec()
    elif i==5:
        editempstatus()
    else:
        print("Invalid Choice Entered")
        requestmenu()

def requestmenu(): #for a new menu
    print()
    print()
    ch=input("Do you want to view the menu and select another choice? (y/n): ")
    if ch=='y':
        os.system('clear')
        menu()
    else:
        print()
        print()
        print("Program Execution Finished.")
        print("Thank You.")
    
def viewfullrec():
    command="select * from MainTable"
    p.execute(command)
    data=p.fetchall()
    for i in data:
        print(i[0],":",i[1],":",i[2],":",i[3],":",i[4],":",i[5]) #subject to change depending on the number of columns
    requestmenu()
    
def viewempstatus():
    command="select * from Status"
    p.execute(command)
    data=p.fetchall()
    for i in data:
        print(i[0],":",i[1]) #subject to change
    requestmenu()
    
def jobapplicants(): #view and accept applicants
    command="select * from Applicants"
    p.execute(command)
    data=p.fetchall()
    for i in data:
        print(i[0],":",i[1],":",i[2],":",i[3],":",i[4]) #subject to change depending on number of columns 
    ac=input("Enter the serial numbers of those whose application should be accepted in the form of a list: ")
    print()
    print("Data of accepted job applications are as follows:")
    for i in data:
        if i[0]==ac:
            print(i[1],":",i[2],":",i[3],":",i[4]) #subject to change depending on number of columns
    requestmenu()
    
def editfullrec(): #to edit records
    n1=input("Enter name of the employee: ")
    print()
    print("--------------------------------------------------------")
    print("1. Change Salary of ",n1)
    print("2. Change Post of ",n1)
    print("3. Change Location of ",n1)
    print("--------------------------------------------------------")
    ch=int(input("Enter number corresponding to the change you want to make to the record of: "))
    if ch==1:
        salary1=int(input("Enter new salary: "))
        command="UPDATE MainTable SET EmpSalary='{}' WHERE EmpName='{}'".format(salary1,n1)
    elif ch==2:
        post1=input("Enter new position: ")
        command="UPDATE MainTable SET EmpPost='{}' WHERE EmpName='{}'".format(post1,n1)
    elif ch==3:
        location1=input("Enter new location: ")
        command="UPDATE MainTable SET EmpLocation='{}' WHERE EmpName='{}'".format(location1,n1)
    else:
        print("Choice does not exist.")
        requestmenu()
    p.execute(command)
    db.commit()
    print("Records Updated.")
    requestmenu()    

def editempstatus(): # to edit emp status
    n1=input("Enter name of the employee: ")
    c1=input("If you want to change his status from unemployed to employed, please enter 1, and for vice-versa, please enter 2.")
    if c1==1:
        command="UPDATE Status s, MainTable m SET EmpStatus='Employed' WHERE s.UID=m.UID and EmpName='{}'".format(n1)
    else:
        command="UPDATE Status s, MainTable m SET EmpStatus='Unemployed' WHERE s.UID=m.UID and EmpName='{}'".format(n1)
    p.execute(command)
    db.commit()
    print("Records Updated.")
    requestmenu()

login()
db.close()
