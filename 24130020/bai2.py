def validate_username(username):
    """

    :param username:
    :return: True or False
    """
    if len(username) >= 6:
        return True
    else:
        return False

def validate_password(password):
    if len(password) < 6:
        return False
    has_digit = False
    has_upper = False
    has_special = False
    special_characters = ("!@#$%^&*()_+-=[]{}|;':\",./<>?")
    for char in password:
        if char.isdigit(): has_digit = True
        if char.isupper(): has_upper = True
        if char in special_characters: has_special = True
    return has_digit and has_upper and has_special

def register():
    print("Facebook Account Registration")
    while True:
        username = input("nhap username: ")
        if validate_username(username) == False:
            print("username phai co it nhat 6 ky tu")
        else :
            break
    for account in accounts :
        if account[0] == username:
            print("Username already exists! Try again.")
            return
    while True :
        password = input("nhap password: ")
        if validate_password(password) is False:
            print("Password must have at least 6 characters, including 1 uppercase, 1 digit, 1 special character!")
        else:
            break
    accounts.append((username, password))
print("Registration successful!")

def login():
    print("Facebook login")
    while True:

        username = input("nhap username de login: ")
        password = input("nhap password de login: ")
        if (username,password) in accounts:
            print("login successful")
            return
        else:
            print ("incorrect username or password! try again")

accounts = []
register()
login()