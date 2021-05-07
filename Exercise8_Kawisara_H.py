usernameInput = input("username :")
passwordInput = input("password :")
if usernameInput == "abcd" and passwordInput == "3456":
    print("Done!!")
    print("---MyShop---")
    print("1. Coke  10 THB")
    print("2. Pepsi 15 THB")
    print("3. water 10 THB")
    userSelected = int(input("Product >>>"))
    if userSelected == 1:
        amount = int(input("Amount: "))
        price = 10
        result1 = price*amount
        print(("Coke"), price,("*"), amount,("=") , result1 , ("THB"))
    elif userSelected == 2:
        amount = int(input("Amount: "))
        price = 15
        result2 = price*amount
        print(("Pepsi"), price,("*"), amount,("=") , result2, ("THB"))
    elif userSelected == 3:
        amount = int(input("Amount: "))
        price = 10
        result3 = price*amount
        print(("Water"), price,("*"), amount,("=") , result3, ("THB"))