
#user class
class user():
    def __init__(self, username, password, valid_user, valid_password):
        username = username
        password = password
        valid_user = valid_user
        valid_password = valid_password

        if (username == valid_user and password==valid_password):
            print("You username and password has been succefully validated")
        else:
            print("Invalid login Credentials")

print ("*************Enter Credentials To Register ***************")
username = input("UserName: ")
password = input("Password: ")
#access = {username : password}
print ("*************Enter Credentials To Login ***************")
valid_user = input("UserName: ")
valid_password = input("Password: ")
#access.update({valid_user: valid_password})
user(username, password, valid_user, valid_password)
