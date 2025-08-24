a={128:{"Name":"Rahul","Balance":20000,"PIN":1245}}  # saving data of the users in the form of the nested dictionary

print("Banking Management System")

def home_page(): 
    print("press 1 for exisitng users")
    print("press 2 for new users")

    choice=int(input("enter a number"))
    if choice==1:
        existing_user()
    elif choice==2:
        new_user()
    else:
        print("Please enter  valid key")

def existing_user():
    f=int(input("enter your account number"))
    print("Your account number is:",f)
    for i in a:
        if i==f:
            print(i,a[i])
            main_page()

    
def new_user():
    g=input("Please enter your name")
    b=int(input("Please enter the PIN you want to create"))
    print("Your PIN has been successful generated:",b)
    import random
    x = random.randint(100,200)  # Random 3 digit account number
    print("Your account number has been generated successfully:",x)
    print("Please remember your account number for future use.")
    balance= 0
    a[x]={"name":g,"Balance":balance,"PIN":b}
    for i in a:
        if i==x:
            print(i,a[i])
            main_page()
                

def  main_page():
    print("press 1 for credit amount")
    print("press 2 for debit amoount")
    print("press 3 for check balance")
    print("press 4 for delete account")
    print("press 5 to go to home page")
    z=int(input("Please enter the key of your choice"))

    if(z==1):
            g=int(input("enter your account number"))
            if g in a:
                print("Balance:",a[g]["Balance"])
                credit=int(input("Enter the amount"))
                a[g]["Balance"]+=credit
                print('Your amount has been credited successfully')
                print("Your current account balance is :",a[g]["Balance"])
                main_page() 

            else:
                print("Incorrrect Account number . Please mention right account number")
                main_page() 
            
    elif(z==2):
        g=int(input("enter your account number"))
        if g in a :
            print("Balance:",a[g]["Balance"])
                
            Debit=int(input("Enter the amount"))
            if a[g]["Balance"]<Debit:
                print("Insufficient Balance")
            else:
                a[g]["Balance"]=a[g]["Balance"]-Debit
                print("Your amount has been debited successfully:",a[g]["Balance"])
                print("Your account balance is :",a[g]["Balance"])
            main_page()

        else:
            print("Incorrect account number. Please mention correct account number")
            main_page()

    elif(z==3):
        g=int(input("enter your account number"))
        if g in a:
                print("Your current account balance is:",a[g]["Balance"])
                main_page()
        else:
            print("Incorerect account number. Please mention correct account number")
            main_page()
    

    elif(z==4):
        g=int(input("enter your account number"))
        if g in a :
                a.pop(g)
                print("Your account has been deleted successfully")
                main_page()

        else:
            print("Incorrect account number. Please mention correct account number")
            main_page()
        

    elif(z==5):
        home_page()
        main_page()

    else:
        print("Please enter the valid key from 1 to 5")
        main_page()

home_page()   # Start the program



        
