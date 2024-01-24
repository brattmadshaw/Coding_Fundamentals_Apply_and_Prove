print("Welcome to the ISMS system. Unauthorised access is strictly prohibited and can result in sever penalties. Please ensure you have permission to access this system")

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == 'matt' and password == 'pass':
    print("Login correct")
    print("Welcome to the ISMS Dashboard")
else:
    ("Invalid username or password.")