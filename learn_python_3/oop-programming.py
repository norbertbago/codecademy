class User:
    is_admin = False

class Admin(User):
    is_admin = True


user_1 = User()
user_2 = Admin()

users = [user_1, user_2]


for user in users:
    if user.is_admin == True:
        print("Mas admin prava")
    else:
        print("Nemas admin prava")

print(issubclass(User, Admin))


