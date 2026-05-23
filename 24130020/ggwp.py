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

def register(accounts,platform):
    print("Account Registration"+ platform)
    while True:
        username = input("nhap username: ")
        if not validate_username(username) :
            print("username phai co it nhat 6 ky tu")
            continue
        username_exists = False
        for account in accounts :
            if account["username"] == username and account["platform"] == platform :
                print("Username already exists! Try again.")
                username_exists = True
                break
        if username_exists:
            continue
        else:
            break
    while True :
        password = input("nhap password: ")
        if validate_password(password):
            accounts.append({
                        "username": username,
                        "password": password,
                        "platform": platform
                    })
            print("Account registered successfully for " + platform + "!")
        else: print("Password must meet security requirements.")

def login(accounts, platform):
    print("login to your"+platform+"account")
    while True:
        username = input("nhap username de login: ")
        password = input("nhap password de login: ")
        for account in accounts:
            if account.username == username and account.password == password and account.platform == platform:
                print("login successful")
                return
            else:
                print ("incorrect username or password! try again")

def main():
    accounts = []
    platforms = ["Facebook", "Instagram", "TikTok"]
    while True:
        print("Choose a platform:")
        for i in range (len(platforms)):
            print (f"{i+1}  .  {platforms[i-1]}")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3"]:
            platform = platforms[int(choice) - 1]
            print ("Choose an option for " + platform + ":")
            print("1. Register")
            print("2. Login")
            print("Enter your choice: ")
            sub_choice = input()
            if sub_choice == "1" :
                register(accounts,platform)
            elif sub_choice == "2" :
                if len(accounts) > 0 :
                    login(accounts,platform)
                else :
                    print("No registered accounts. Please register first.")
            else :
                print("invalid choice")
        elif choice == "4" :
                print("exit program")
                break
        else: print("Invalid choice. Please enter a valid option.")
main()