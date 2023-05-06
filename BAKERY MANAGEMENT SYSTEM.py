#                    BAKERY MANAGEMENT SYSTEM
import mysql.connector
con = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Adikar')

cur = con.cursor()
cur.execute('create database if not exists items')
cur.execute('use items')
cur.execute('create table if not exists cs(sno int,products varchar(20),cost int)')
cur.execute('select * from cs')
res = cur.fetchall()
if res == []:
    cur.execute('insert into cs values(1,"Cake",50)')
    cur.execute('insert into cs values(2,"Pastry",20)')
    cur.execute('insert into cs values(3,"Milk",60)')
    cur.execute('insert into cs values(4,"Butter",20)')
    cur.execute('insert into cs values(5,"Cheese",30)')
    con.commit()

cur.execute('create table if not exists flavours(sno int,varieties varchar(20))')
cur.execute('select * from flavours')
res = cur.fetchall()
if res == []:
    cur.execute('insert into flavours values(1,"Vanilla")')
    cur.execute('insert into flavours values(2,"Chocolate")')
    cur.execute('insert into flavours values(3,"Strawberry")')
    cur.execute('insert into flavours values(4,"Butter_Scoth")')
    cur.execute('insert into flavours values(5,"Mango")')
    con.commit()

cur.execute('create table if not exists worker(Sno int,Name varchar(20),Salary int)')
cur.execute('select * from worker')
res= cur.fetchall()
if res == []:
    cur.execute('insert into worker values(1,"Biju",5000)')
    cur.execute('insert into worker values(2,"Preeti",20000)')
    cur.execute('insert into worker values(3,"Ram",6000)')
    cur.execute('insert into worker values(4,"Raj",10000)')
    con.commit()

from datetime import datetime

print("____________________________________________________________________")
print("|__________________________WELCOME_________________________________|")
print("|____________________________TO____________________________________|")
print("|__________________BAKERY MANAGEMENT SYSTEM________________________|")
print("|__________________________________________________________________|")

ch = ''
while ch != 'N' or ch != 'n':
    print("\n\nPLEASE CHOOSE \n1 FOR ADMIN\n2 FOR CUSTOMER\n3 TO EXIT: \n")
    choice= int(input("Enter your choice: "))
    if choice == 3:
        break
    if choice == 1:
        admin = input("ENTER USERNAME: ")
        password = int(input("ENTER PASSWORD: "))
        if password == 1234:
            print('*******************HELLO ADMIN,LOGIN SUCCESSFULL**********')
            print('__________________________________________________________')
            print('Press 1 To Add Item in the shop....')
            print('Press 2 To See Items in the shop....')
            print('Print 3 to update cost of any item....')
            print('Press 4 to add varities of cake in the shop....')
            print('Press 5 To Add Worker in the shop..')
            print('Press 6 to see workers..')
            print('Press 7 to update salary of any worker..')

            c = int(input("Enter your choice: "))
            if c == 1:
                def add():
                    sno = int(input("Enter serial number: "))
                    product = input("Enter product name: ")
                    cost = int(input("Enter cost of product: "))
                    d1 = (sno,product1,cost)
                    s1 = 'insert into cs values(%s,%s,%s)'
                    cur.execute(s1,d1)
                    con.commit()
                    print('_______________________////////ITEM ADDED SUCCCESSFULLY//////_______________________')
                add()
            elif c== 2:
                def items():
                    print('Items in the shop:')
                    cur.execute('select * from cs')
                    res = cur.fetchall()
                    t = (['serial_no','products','cost'])
                    for serial_no,products,cost in res:
                        print(serial_no,":","\t",products,":\t\t",'Cost',cost)
                items()
            elif c == 3:
                def money():
                    sno = input("Enter serail number of the product: ")
                    n_cost = input("Enter the new cost of the product: ")
                    cur.execute('update cs set cost = cost+'+n_cost+'where sno='+sno+';')
                    con.commit()
                    print("DETAILS AFTER UPDATION")
                    cur.execute('select * from cs')
                    res = cur.fetchall()
                    t = (['sno','products','cost'])
                    for sno,products,cost in res:
                        print(sno,":","\t",products,":","\t",'Cost',cost)
                money()
            elif c == 4:
                def variety():
                    sno = input("Enter serial number: ")
                    varities = input("Enter variety: ")
                    d2 = (sno,varieties)
                    s2 = 'insert into flavour values(%s,%s)'
                    cur.execute(s2,d2)
                    con.commit()
                variety()
            elif c == 5:
                def adw():
                    sno = int(input("Enter serial number: "))
                    emp = input("Enter name: ")
                    salary = int(input("Enter the salary: "))
                    dx = (sno,emp,salary)
                    sy = 'insert into worker values(%s,%s,%s)'
                    cur.execute(sy,dx)
                    con.commit()
                    print('_______________________////////WORKER ADDED SUCCCESSFULLY//////_______________________')
                adw()
            elif c == 6:
                def workers():
                    print("Workers in the shop: ")
                    cur.execute('select * from worker')
                    res = cur.fetchall()
                    t = (['serial_no','name','salary'])
                    for serial_no,name,salary in res:
                        print(serial_no,":","\t",name,":","\t",salary)
                workers()
            elif c == 7:
                def up():
                    print("Choose 1 to increase the salary:")
                    print("Choose 2 to decrease: ")
                    n_salary = int("Enter the salary: ")
                    name = input("Enter name of the employee: ")
                    sig = int(input("Enter choice(1/2): "))
                    if sig == 1:
                        cur.execute('update worker set salary = salary+'+n_salary+'where name='+name+';')
                        con.commit()
                        print("DETAILS AFTER UPDATION")
                        cur.execute('select * from worker')
                        res = cur.fetchall()
                        t = (['sno','name','salary'])
                        for sno,name,salary in res:
                            print(sno,":","\t",name,":","\t",salary)
                    if sig == 2:
                        cur.execute('update worker set salary = salary-'+n_salary+'where name='+name+';')
                        con.commit()
                        print("DETAILS AFTER UPDATION")
                        cur.execute('select * from worker')
                        res = cur.fetchall()
                        t = (['sno','name','salary'])
                        for sno,name,salary in res:
                            print(sno,":","\t",name,":","\t",salary)
                up()
            else:
                print("SORRY...WRONG INPUT PLEASE ENTER A VALUE BETWEEN (1-7)")
        else:
            print("\t\t\t\t\t\t\t*********************WRONG PASSWORD************\t\t\t\t\t\t\t")
    elif choice == 2:
        name = input("Enter your name: ")
        phone = int(input("Enter yout phone number: "))
        print("Press 1 to see the MENU",sep = '.....')
        print("Press 2 to order an item")
        c = int(input("Enter your choice:"))
        if c == 1:
            def items():
                print("Items in the shop:")
                cur.execute('select * from cs')
                res = cur.fetchall()
                t = (['serial_no','products','cost'])
                for serial_no,products,cost in res:
                    print(serial_no,":","\t",products,":","\t",'Cost',cost)
            items()
        elif c == 2:
            print("What do you want to order?")
            cur.execute('select * from cs')
            res = cur.fetchall()
            t = (['serial_no','products','cost'])
            for serial_no,products,cost in res:
                print(serial_no,":","\t",products,":","\t",'Cost',cost)


            cur.execute('select sno from cs')
            res = cur.fetchall()
            print(res)
            l = []
            for i in range(len(res)):
                l.append(res[i][0])
            print(l)

            d = int(input("Enter your serial no of the item you want to buy:"))
            if d == 1:
                def items():
                    print("Which cake do you want?")
                    cur.execute('select * from flavours')
                    srh = cur.fetchall()
                    f = (['sno','varities'])
                    for sno,varities in srh:
                        print(sno,":","\t\t",varities)
                    print("Choose which cake do you want?")
                    ck = int(input("Enter choice:"))
                    if ck == 1:
                        print("How much Quantity of vanila cake do you want?")
                        Qty = int(input("Enter Quantity."))
                        print("You have successfully ordered your cake!!!\t:")
                        cur.execute('select * from cs where products = "cake"')
                        for i in cur:
                            c = i[2]
                            con.commit()
                        print("Total amount",Qty*c)
                        print("\n")
                        print("________________________________________________")
                        print("_________________YOUR BILL______________________")
                        print("________________________________________________")
                        print("Customer's Name:",name)
                        print("Contact no:",phone)
                        print("Cake type:Vanilla")
                        print("No of Cakes:",Qty)
                        print("Total amount",Qty*c)
                        print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                        print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
                    if ck == 2:
                        print("How much Quantity of Chocolate cake do you want?")
                        Qty = int(input("Enter Quantity."))
                        print("You have successfully ordered your cake!!!\t:")
                        cur.execute('select * from cs where products = "cake"')
                        for i in cur:
                            L =i[2]
                        print("Total amount",Qty*L)
                        print("\n")
                        print("________________________________________________")
                        print("_________________YOUR BILL______________________")
                        print("________________________________________________")
                        print("Customer's Name:",name)
                        print("Contact no:",phone)
                        print("Cake type:Chocolate")
                        print("No of Cakes:",Qty)
                        print("Total amount",Qty*L)
                        print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                        print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
                    if ck == 3:
                        print("How much Quantity of Strawberry cake do you want?")
                        Qty = int(input("Enter Quantity."))
                        print("You have successfully ordered your cake!!!\t:")
                        cur.execute('select * from cs where products = "cake"')
                        for i in cur:
                            N =i[2]
                        print("Total amount",Qty*N)
                        print("\n")
                        print("________________________________________________")
                        print("_________________YOUR BILL______________________")
                        print("________________________________________________")
                        print("Customer's Name:",name)
                        print("Contact no:",phone)
                        print("Cake type:Strawberry")
                        print("No of Cakes:",Qty)
                        print("Total amount",Qty*N)
                        print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                        print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
                    if ck == 4:
                        print("How much Quantity of Butter_scotch cake do you want?")
                        Qty = int(input("Enter Quantity."))
                        print("You have successfully ordered your cake!!!\t:")
                        cur.execute('select * from cs where products = "cake"')
                        for i in cur:
                            M =i[2]
                        print("Total amount",Qty*M)
                        print("\n")
                        print("________________________________________________")
                        print("_________________YOUR BILL______________________")
                        print("________________________________________________")
                        print("Customer's Name:",name)
                        print("Contact no:",phone)
                        print("Cake type:Butter_scotch")
                        print("No of Cakes:",Qty)
                        print("Total amount",Qty*M)
                        print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                        print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
                    if ck == 5:
                        print("How much Quantity of Mango cake do you want?")
                        Qty = int(input("Enter Quantity."))
                        print("You have successfully ordered your cake!!!\t:")
                        cur.execute('select * from cs where products = "cake"')
                        for i in cur:
                            Z =i[2]
                        print("Total amount",Qty*Z)
                        print("\n")
                        print("________________________________________________")
                        print("_________________YOUR BILL______________________")
                        print("________________________________________________")
                        print("Customer's Name:",name)
                        print("Contact no:",phone)
                        print("Cake type:Mango")
                        print("No of Cakes:",Qty)
                        print("Total amount",Qty*Z)
                        print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                        print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
                items()
            elif d == 2:
                print("How much pastry do you want")
                past = int(input("Enter your choice:"))
                print("You have successfully orderd",past,"pastry")
                cur.execute("select * from cs where products = 'pastry'")
                for i in cur:
                    c = i[2]
                print("Total amount",past*c)
                print("\n")
                print("________________________________________________")
                print("_________________YOUR BILL______________________")
                print("________________________________________________")
                print("Customer's Name:",name)
                print("Contact no:",phone)
                print("No of pastry:",past)
                print("Total amount",past*c)
                print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
            elif d == 3:
                print("How much lites of milk do you want?")
                milk = int(input("Enter your choice:"))
                print("You have successfully orderd",milk,"L of milk:")
                cur.execute("select * from cs where products = 'milk'")
                for i in cur:
                    c = i[2]
                print("Total amount",milk*c)
                print("\n")
                print("________________________________________________")
                print("_________________YOUR BILL______________________")
                print("________________________________________________")
                print("Customer's Name:",name)
                print("Contact no:",phone)
                print("Quantity of milk:,",milk)
                print("Total amount",milk*c)
                print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
            elif d == 4:
                print("How much packets(20gm) of butter do you want?")
                but = int(input("Enter your choice:"))
                print("You have successfully orderd",but,"packets of butter:")
                cur.execute("select * from cs where products = 'butter'")
                for i in cur:
                    c = i[2]
                print("Total amount",but*c)
                print("\n")
                print("________________________________________________")
                print("_________________YOUR BILL______________________")
                print("________________________________________________")
                print("Customer's Name:",name)
                print("Contact no:",phone)
                print("Quantity of butter:",but)
                print("Total amount",but*c)
                print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
            elif d == 5:
                print("How much cheese(in Kg) of cheese do you want?")
                chs = int(input("Enter your choice:"))
                print("You have successfully orderd",chs,"Kg of cheese.")
                cur.execute("select * from cs where products = 'cheese'")
                for i in cur:
                    c = i[2]
                print("Total amount",chs*c)
                print("\n")
                print("________________________________________________")
                print("_________________YOUR BILL______________________")
                print("________________________________________________")
                print("Customer's Name:",name)
                print("Contact no:",phone)
                print("Quantity of cheese:",chs)
                print("Total amount",chs*c)
                print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
            elif d in l:
                Qty = int(input("Enter Quantity: "))
                print("You have successfully orderd your selected item!!!\t:")
                cur.execute("select * from cs where sno="+str(d))
                for i in cur:
                    L = i[2]
                print("Total amount",Qty*L)
                print("\n")
                print("________________________________________________")
                print("_________________YOUR BILL______________________")
                print("________________________________________________")
                print("Customer's Name:",name)
                print("Contact no:",phone)
                print("Quantity",Qty)
                print("Total amount",Qty*L)
                print("!!!!!!!!!!!!!!!!!THANK YOU FOR ORDERING THE ITEM!!!!!!")
                print("\t\t\t\t\t\t\t\t\tDate:",datetime.now())
            else:
                print("Wrong Input")
        else:
            print("\t\t\t\t\t\t\t****************Wrong Password*********\t\t\t\t\t\t\t")
    ch = input("Do you want to continue(Y/N):")
    if ch == 'N' or ch == 'n':
        exit()




"""               RESTAURANT MANAGEMENT SYSYTEM


#Connecting database
import mysql.connector as a
passwd=str(input("Enter Database Password: "))
con=a.connect(host='localhost',user='root',password=passwd)
#Selecting or Creating Database
c=con.cursor()
c.execute("Show Database")
dl=c.fetchall()
dl2=[]
for i in dl:
    dl2.append(i[0])
if 'rest1' in dl2:
    sql='use rest1'
    c.execute(sql)
    con.commit()
else:
    sql1='create database rest1'
    c.execute(sql1)
    sql2='use rest1'
    c.execute(sql2)
    sql3="""#create table Dish(DishID varchar(20) Dish varchar(20),Price integer, Cook varchar(50))""""""
    #c.execute(sql3)"""
    #sql4="""create table Orders(DishIDs varchar(100), Price integer,Date varchar(20), Customer varchar(50), Aadhar varchar(20))"""
    #c.execute(sql4)
    #sql5="""create table Cook(Name varchar(50),Aadhar varchar(20), Dishes varchar(100), Salary integer, DOJ varchar(20))"""
    #c.execute(sql5)
    #sql6="""create table Salary(Name varchar(50), Aadhar varchar(20), Bank varchar(20),Month varchar(20),Salary integer, Days integer,Net integer)"""
    #c.execute(sql6)
    #sql7="""create table Expenditure(Type varhcar(50), Cost integer, Date varchar(20))"""
    #c.execute(sql7)
    #con.commit()
#LOGIN
"""
def signin():
    print("--->Welcome to name......<---")
    p=input("Enter system password: ")
    if p==passwd:
        options()
    else:
        signin()
#Displaying Program Menu

def options():
    print("Dishes - (1)\nCooks - (2)\nSalary - (3)\nOrder - (4)\nIncome - (5)\nBills - (6)")
    choice=input("Select your option: ")
    while True:
        if(choice=='1'):
            Dish()
        elif(choice=='2'):
            Cook()
        elif(choice=='3'):
            Paysalary()
        elif(choice=='4'):
            NewOrder()
        elif(choice=='5'):
            NetIncome()
        elif(choice=='6'):
            Expenditure()
        else:
            print("Invalid option....")
def Dish():
    choice=input("1.Add\n2.Remove\n3.Display\n4.Main menu\n : ")
    if choice=='1':
        dn=input("Dish name: ")
        dc=input("Dish price: ")
        Cname()
        cb=input("Cooked by: ")
        did=str(DishID())
        data=(dn,dc,cb,did)
        sql='insert into Dish values(%s,%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data sucessfully entered")
    elif choice=='2':
        did=input("Dish ID: ")
        data=(did,)
        sql='Delete from Dish where DishID=%s'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data sucessfully Updated")
    elif choice='3':
        sql='select * from Dish"
        c=con.cursor()
        c.execute(sql)
        d=c.fectchall()
        for i in d:
            print(i[0],'-',i[1],'-',i[2],'-',i[3])
        else:
            options()

def DishID():
    sql='select count(*), max(DishID) from Dish'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        if i[0]==0:
            return(1)
        else:
            return(int(i[1])+1)

def Cname():
    sql='select Name, Dishes from Cook'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    print("Available Cooks:-")
    for i in d:
        print(i[0],'---',i[1])
        return

def Cook():
    choice=input("1.Add cook\n2.Remove cook\n3.Display\n4.Main menu\n : ")
    if choice=='1':
        cn=input("Cook name: ")
        ca=input("Aadhar: ")
        d=input("Dishes: ")
        s=int(input("Salary: "))
        doj=input("Date of Join(Y/M/D): ")
        data=(cn,ca,d,s,doj)
        sql='insert into Cook values(%s,%s,%s,%s,%S)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data successfully altered")
    elif choice=='2':
        cn=input("Cook name: ")
        ca=input("Aadhar: ")
        data=(cn,ca)
        sql='delete from Cook where Name=%s and Aadhar=%s'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Updated Successfully")
    elif choice='3':
        sql='Select * from Cook'
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print(i[0],'-',i[1],'-',i[2],'-',i[3],'-',i[4])
    else:
        options()

                
                
                
                 
"""                     
                        
                        
                        
                    
                
            
                
                              
                    
                    
                
                
                    
                
            

            
            





    
