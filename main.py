from operation import DBHelper


def main():
    db=DBHelper()
    while True:
        print("----------welcome-----------")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("press 3 to delete user")
        print("press 4 to update user")
        print("press 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid=int(input("Enter user id: "))
                username=input("Enter username: ")
                userno=input("enter phone number: ")
                db.insert_user(uid,username,userno) 
                pass
            elif choice==2: 
                #display
                db.fetch_all()
                pass
            elif choice==3:
                #delete
                id=int(input("enter id to delete: "))
                db.delete_user(id)
                pass
            elif choice==4:
                #update user\
                id=int(input("Enter id to update: "))
                newname=input("Enter new name: ")
                newno=input("enter new no: ")
                db.update_user(id,newname,newno)
                pass
            elif choice==5:
                break
            else:
                print("invalid input..")
        except Exception as e:
            print(e)
            print("Invalid details..")
if __name__=="__main__":
    main()           
        