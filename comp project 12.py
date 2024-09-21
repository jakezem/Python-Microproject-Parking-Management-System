#DONE BY JACOB SAM JOSE 
#ADMIN USERNAME: admin
#ADMIN PASSWORD: 123

import mysql.connector as mysql
import time
import random
mydb=mysql.connect(host='localhost',user='root',passwd='Isalain',database='parking_system')
mycursor=mydb.cursor()

print("\t\t\t\t\t\t WELCOME TO MEGAPARK DIGITAL AIRPORT PARKING MANAGAMENT  SYSTEM\t\t\t\t\t\t ")

for i in range(130):
    print("_",end="")
    time.sleep(0.00001)
    
First_List = []
Bus_List = []
Eco_List = []
Fcollection = 0
Bcollection = 0
Ecollection = 0
for i in range (1,101):
    First_List.append('A'+str(i))
for j in range (1,101):
    Bus_List.append('B'+str(j))
for k in range (1,101):
    Eco_List.append('C'+str(k))
    

def account():
    print()
    print('CREATE AN ACCOUNT AND BECOME A PART OF OUR FAMILY !')
    print()
    Username=input(str('Enter Username: '))
    Password=input(str('Enter Password: '))
    Type=input(str('Enter Type of Car:'))
    emid=input(str('Enter your EM ID:'))
    query_vals=(Username,Password,Type,emid)
    mycursor.execute("INSERT INTO users (Username,Password,Type,emid) VALUES (%s,%s,%s,%s)",query_vals)
    mydb.commit()
    print('YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY')
            
    
def customer_act():
    while True:
        print()
        print('1.Display Profile')
        print('2.Edit Profile')
        print('3.Book a Parking Reservation')
        print('4.Give Feedback')
        print('5.Log Out')
        user_option=input(str('OPTION :'))
        if user_option=='1':
            print()
            print('DISPLAY PROFILE')
            mycursor.execute('SELECT * FROM users WHERE Username=%s AND Password=%s',vals)
            records=mycursor.fetchall()
            print(records)
        elif user_option=='2':
            print()
            print('EDIT PROFILE')
            mycursor.execute('SELECT * FROM users WHERE Username=%s AND Password=%s',vals)
            records=mycursor.fetchall()
            print(records)
            while True:
                print('Select the Field you want to Edit', '\n1.Username','\n2.Password','\n3.Car Type','\n4.EMID','\n5.Go Back')
                c=input(str(''))
                if c=='1':
                    mycursor.execute('SELECT * FROM users WHERE Username=%s AND Password=%s',vals)
                    z=mycursor.fetchone()
                    print(z)
                    us,ps,tp,i=z
                    new_user=input(str("Enter your New Username: "))
                    v=(new_user,ps)
                    mycursor.execute('UPDATE users SET Username = %s WHERE Password = %s',v)
                    mydb.commit()
                    print('Your Username has been changed to',new_user)    
                elif c=='2':
                    mycursor.execute('SELECT * FROM users WHERE Username=%s AND Password=%s',vals)
                    z=mycursor.fetchone()
                    print(z)
                    us,ps,tp,i=z
                    new_pass=input(str("Enter your New Password: "))
                    v=(new_pass,us)
                    mycursor.execute('UPDATE users SET Password = %s WHERE Username = %s',v)
                    mydb.commit()
                    print('Your Password has been changed to',new_pass)    
                    
                elif c=='3':
                    mycursor.execute('SELECT * FROM users WHERE Username=%s AND Password=%s',vals)
                    z=mycursor.fetchone()
                    print(z)
                    us,ps,tp,i=z
                    new_type=input(str("Enter your New Car Type: "))
                    v=(new_type,us)
                    mycursor.execute('UPDATE users SET Type = %s WHERE Username = %s',v)
                    mydb.commit()
                    print('Your Car Type has been changed to',new_type)   
                    
                elif c=='4':
                    mycursor.execute('SELECT * FROM users WHERE Username=%s AND Password=%s',vals)
                    z=mycursor.fetchone()
                    print(z)
                    us,ps,tp,i=z
                    new_emid=input(str("Enter your New ID : "))
                    v=(new_emid,us)
                    mycursor.execute('UPDATE users SET emid = %s WHERE Username = %s',v)
                    mydb.commit()
                    print('Your New EM ID has been changed to',new_emid)
                elif user_option=='5':
                    break
                    
                else:
                    print('INVALID OPTION')
            
        elif user_option=='3':
            print('BOOK A PARKING RESERVATION')
            place=input(str('Place :'))
            print('Finding slots, Please Wait............')
            for i in range(130):
                print(".",end="")
                time.sleep(0.00001)
            print(' Press 1 for FIRST CLASS:100 DHS')
            print('Press 2 for BUSINESS CLASS:50 DHS')
            print('Press 3 for ECONOMY CLASS:25 DHS')
            while True:
                key = int(input('Which Parking Would You Like To Choose: '))
                if key == 1:
                    print("Your parking is at",random.choice(First_List))
                    
                    global Fcollection
                
                    Fcollection += 100
                    break
                elif key == 2:
                    print("Your parking is at",random.choice(Bus_List))
                    
                    global Bcollection
                    
                    Bcollection += 50
                    break
                elif key == 3:
                    print("Your parking is at",random.choice(Eco_List))
                    global Ecollection
                    
                    Ecollection += 25
                    break
                
            for i in range(130):                
                print(".",end="")
                time.sleep(0.00001)
        
        elif user_option=='4':
            print("GIVE YOUR HONEST FEEDBACK OF OUR SERVICE")
            fd=input(str())
            print('\t\t\t\t THANK YOU!!\t\t\t\t')
        elif user_option=='5':
            break            

def customer():
    print()
    print('CUSTOMER LOGIN')
    print()
    Username=input(str('Username :'))
    Password=input(str('Password :'))
    global vals
    vals=(Username,Password)
    mycursor.execute('SELECT * FROM users WHERE Username=%s AND Password=%s',vals)
    records=mycursor.fetchall()
    if records:
        for i in records:
            print('Welcome' +' '+ i[0])
            customer_act()
    else:
        print('User Not Detected')

def admin_act():
    while True:
        print('')
        print('ADMIN LOGIN')
        print('1.Register New Vehicle')
        print('2.Delete Existing Vehicle')
        print('3.Overall Income')
        print('4.Log Out')
        user_option=input(str('OPTION :'))
        if user_option=='1':
            print()
            print('REGISTER NEW VEHICLE')
            Username=input(str('Enter Username: '))
            Password=input(str('Enter Password: '))
            Type=input(str('Enter Type of Car:'))
            emid=input(str('Enter your EMIRATES ID:'))
            query_vals=(Username,Password,Type,emid)
            mycursor.execute("INSERT INTO users (Username,Password,Type,emid) VALUES (%s,%s,%s,%s)",query_vals)
            mydb.commit()
            print(Username + ' has been registered as a New Vehicle')
            
        elif user_option=='2':
            print()
            print('DELETE EXISTING VEHICLE')
            Username=input(str('Enter Username: '))
            emid=input(str('Enter  EM ID:'))
            query_vals=(Username,emid)
            mycursor.execute('DELETE FROM users WHERE Username= %s AND emid= %s',query_vals)
            mydb.commit()
            if mycursor.rowcount < 1:
                print('User Not Detected')
            else:
                print(Username , 'has been Deleted')
                
        elif user_option=='3':
            prmn = input("Do you Want to know the overall collection..?Yes/No-  ")
            if prmn == 'Yes' or 'yes':
                collection = Fcollection + Bcollection + Ecollection
                print(collection,'DHS')
            else:
                prmn == 'No' or 'no'
                print("Then why did you log in brooo?") 
            
        elif user_option=='4':
            break
        else:
            print('No Valid Option Selected')
            

        
def admin():
    print()
    print('ADMIN LOGIN')
    print()
    username=input(str('Username :'))
    password=input(str('Password :'))
    if username=='admin':
        if password=='123':
            admin_act()    
        else:
            print('Incorrect Password')
    else:
        print('Admin Log In Failed')
        
def main():
    while True:
        print('\n1. LOG IN AS CUSTOMER') 
        print('\n2. CREATE AN ACCOUNT')
        print('\n3. LOG IN AS ADMIN')
        user_option=input(str('OPTION : '))
        if user_option=='1':
            customer()
        elif user_option=='2':
            print('CREATE AN ACCOUNT ')
            account()
        elif user_option=='3':
            admin()
        else: 
            print('INVALID OPTION SELECTED')
    
main()