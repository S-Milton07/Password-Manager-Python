import random
import string
import json

class PasswordManager:
    def __init__(self):
        self.accounts=[]
        self.load_password()
      
    def add_Account(self):
        webname=input("Enter a Website:")
        user=input("Enter a user name:")
        choice1=input("Choose to auto generic password(Yes or No)").lower()
        if choice1=="yes":
            passwords=self.generate_password()
            print("The Generated Password is:",passwords)

        else:
            passwords=input("Enter a password:")
            if not self.password_strength(passwords):
                return "Weak Password"
        data={
        "website":(webname),
        "username":user,
        "password":(passwords)
        }
        self.accounts.append(data)
        self.save_password()
        return "Stored Successfully"
        
    def view_Account(self):
        if self.accounts:
            for i in self.accounts:
                print("The website is:",i["website"])
                print("The User_name is:",i["username"])
        else:
            print("No Accounts Found")
        

    def search_pass(self):
        name=input("Enter a Website_name to search its password:")
        for i in  self.accounts:
            if name==i["website"]:
                if i["website"]:
                    print(f"The User_Password is:{i["password"]}")
                    break
        else:
            print("Website not Found!")
                
    def delete_password(self):
       #Want to delete whole website details in dictionary
        del_acc=input("Enter the website to delete its Whole_account:")
        for i in self.accounts:
            if del_acc == i["website"]:
                self.accounts.remove(i)
                self.save_password()
                return "Account deleted successfully!"
        else:
            return "Enter valid Website_name to delete its Whole_account"

    #Update password
    def update_password(self):
        name=input("Enter a Website_name:")
        for i in self.accounts:
            if name==i["website"]:
                new_pass=input("Enter a new Password:")
                if self.password_strength(new_pass):
                    i["password"]=new_pass
                    self.save_password()
                    return "Password Updated successfully"
                else:
                    return "Weak password"
        else:
            return "Website not Found"
            
    #Password_strength
    def password_strength(self, passwords):
        if len(passwords) >=8 and any(i.isupper() for i in passwords) and any(i.islower() for i in passwords) and any(i.isdigit() for i in passwords) and any(i in "!@#$%^&*" for i in passwords):
            return True
        else:
            return False

    #Generate Password
    def generate_password(self):
        ch=string.ascii_letters + string.digits + string.punctuation
        characters=""
        for i in range(8):
            res=random.choice(ch)
            characters+=res
        return characters

    #Save password
    def save_password(self):
        with open("passwords.json","w") as file:
            #file.write(str(self.password)) :use json instead of this
            json.dump(self.accounts,file)

    #Load password
    def load_password(self):
        try:
            with open("passwords.json","r") as file:
                self.accounts=json.load(file)
        except FileNotFoundError:
            print("File Not Found!")

    def exits(self):
        return "User Exited!"
    def menu(self):
        while True:
            try:
                #loop the menu
                print("--------------------------")
                print("1.Add_Account")
                print("2.View_Account")
                print("3.Search_Account_Password")
                print("4.Delete_Account")
                print("5.update_password")
                print("6.Exit")
                print("--------------------------")
                Choice=int(input("Enter a Choice:"))
                
                if Choice==1:
                    print(self.add_Account())
                elif Choice==2:
                    self.view_Account()
                elif Choice==3:
                    self.search_pass()
                elif Choice==4:
                    print(self.delete_password())
                elif Choice==5:
                    print(self.update_password())
                elif Choice==6:
                    print(self.exits())
                    break
                else:
                    print("Enter valid choice")
            except ValueError:
                print("ValueError Occured!!")
            except KeyError:
                print("KeyError Occured!!")
p=PasswordManager()
p.menu()



        
