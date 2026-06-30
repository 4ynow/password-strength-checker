symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "_", ",", "."]
password = input("Password: \n>>>> ")

if len(password) < 8:
    print("Weak password.")
elif len(password) > 8 and any(item in symbols for item in password):
    print("Strong Password.")
elif len(password) > 8:
    print("Medium password.")
