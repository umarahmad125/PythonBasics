Algo = (('a','@'),('e','3'),('i','1'),('l','7'),('o','0'),('s','$'))

def EncryPass(Password):
    for a,b in Algo:
        Password = Password.replace(a, b)
    return Password


if __name__ == "__main__":
    Password = input("Enter Your Password: ")
    Password = EncryPass(Password)
    print(f"You Secure Password is: {Password}")