while True:
    passwd = str(input("input:"))
    if len(passwd) < 6:
        print("Less than 6 characters.There must be 6-12 characters")
    elif 6 <= len(passwd) <= 12:
        if passwd.isalpha():
            print("Weak password!.Try using numbers and special characters.")
        elif passwd.isnumeric():
            print("Weak password!.Try using letters and special characters.")
        elif passwd.isalnum():
            print("Medium password!.Try special characters.")
        else:
            if passwd.isupper():
                print("Strong enough.But atleast one character should be lowercased.")
            elif passwd.islower():
                print("Strong enough.But atleast one character should be UPPERCASED.")
            elif passwd.istitle():
                print("Strong password! Great job!")
            else:
                print("Weak Password!.Try using numbers and letters.")
    else:
        print("More than 6 characters.There must be 6-12 characters")
