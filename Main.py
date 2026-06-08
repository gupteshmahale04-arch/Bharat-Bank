## Bank Project1

import json 
import random 
import string
from pathlib import Path

class Bank:
    database = "bharatbank_db.json"
    data = []

    if Path(database).exists():
        with open(database) as fs: 
            data = json.loads(fs.read())
    

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))

    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 8)
        num = random.choices(string.digits, k =4)

        acc = alpha + num
        random.shuffle(acc)
        return "".join(acc)
    
    def create_user(self):
        info = {
            "name":input("Enter user name :- "),
            "age": int(input("Enter user Age :- ")),
            "email":input("Enter  user Email :- "),
            "AccountNo.": Bank.__accountgenerate(),
            "pin": int(input("Enter user pin :- ")),
            "balance": 0
        }

        if info['age'] < 12 or len(str(info["pin"])) != 4:
            print("sorry cannot create account")
        
        else:
            Bank.data.append(info)
            Bank.__update()

            
    
    def deposite_money(self):
        accno = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))

        userdata = [i for i in Bank.data if 
                    i['AccountNo.'] == accno 
                    and i['pin']== pin]
        if userdata == False:
            print("sorry no such user exist")
        else:
            amount = int(input("Money :- "))
            userdata[0]['balance'] += amount
            bank.__update()
            print("balance added successfully")

    def withdraw_money(self):
        accno = input("Ener your account number :- ")
        pin = int(input("Enter  your pin :- "))

        userdata = [i for i in Bank.data if 
                    i['AccountNo.'] == accno and 
                    i['pin']== pin]
        if userdata == False:
            print("sorry no such user exist")
        else:
            amount = int(input("Money :- "))
            if amount > userdata[0]['balance']:
                print("insufficient balance")
            else:
                userdata[0]['balance'] -= amount
                bank.__update()
                print("balance added successfully")
            
    def show_details(self):
        accno = input("Enter your account number :- ")
        pin = int(input("Enter your pin :- "))

        userdata = [
            i for i in Bank.data
            if i['AccountNo.'] == accno and i['pin'] == pin
         ]

        if not userdata:
            print("No data found!")
        else:
            for key, value in userdata[0].items():
                print(f"{key} : {value}")#print(f"{i} - {userdata[0][i]}") by akarsh bhiya

   

    def update_details(self):
        
        accno = input("Ener your account number :- ")
        pin = int(input("Enter  your pin :- "))
        # userdata = [i for i in Bank.data if i['AccountNo.'] == accno and 
        #             i['pin']== pin]# by me
        userdata = [i for i in Bank.data if str(i.get('AccountNo.')) == accno and i.get('pin') == pin]# by ai
       # userdata = [i for i in Bank.data if (i ["AccountNO."])== accno and i["pin"]== pin] #by bhaiya
        if  not userdata:
                print("no data found !")
        else:
            print("You can not change bankbalance, account number and age")
            newdata={
                 "name" : input("Enter your New name  or press enter to skip")    ,      
                 "E mail" : input("Enter your New E mmail  or press enter to skip")  ,
                 "pin":input("Enter your New pin  or press enter to skip")  }
            if newdata["name"]=="":
                 newdata["name"]=(userdata[0]["name"])

            if newdata["E mail"]=="":
                 newdata["E mail"]=(userdata[0]["E mail"])

            if newdata['pin']=="":
                 newdata['pin']=str(userdata[0]['pin'])

            for i in userdata[0]:
                if i in newdata:
                    userdata[0][i] = newdata[i]

                if i == "pin":
                     userdata[0][i] = int(newdata[i])
            bank.update_details()
            print("Details updated successfully")
    
    
    def delete_account(self):
        accno = input("Ener your account number :- ")
        pin = int(input("Enter  your pin :- "))
        userdata = [i for i in Bank.data if 
                    i['AccountNo.'] == accno and 
                    i['pin']== pin]
        if   userdata==False:
             print("no such user")
        
        else:
             print("are you sure you want to delete :")
             ckeck =input("press y for yes or n ofr no :- ")
             
             if ckeck.lower() == "y":
                    Bank.data.remove(userdata[0])
                    bank.__update()
                    print("account deleted successfully")
        


bank = Bank()
while True:
    print("============================================================================================================================================================== " )
    print("                                                  ----------------- welcome to Bharat Bank-----------------                                                     ")
    print("============================================================================================================================================================== " )
     
    print("Press 1 for Creating account :")
    print("Press 2 for Depositing Money :")
    print("Press 3 for Withdrawing Money :")
    print("Press 4 for Details of a user :")
    print("Press 5 for Updatinng User Details :")
    print("Press 6 for Deleting User  :")
    print("Press 0 for Exit  :")

    res = int(input("Enter  your response :- "))

    print("============================================================================================================================================================== " )

    if res > 0:
    

            if res == 1:
                bank.create_user()
            elif res == 2:
                bank.deposite_money()

            elif res == 3:
                bank.withdraw_money()

            elif res == 4:
                bank.show_details()

            elif res == 5:
                bank.update_details()

            elif res == 6:
                bank.delete_account()
        

            elif res>6:
                break

    elif res == 0:
         print("Thank you for using our services")



