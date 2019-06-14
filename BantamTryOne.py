# Coding Project
# The programs purpose: A user must enter the correct username and password and then verify the users certifications
# The correct username is bantamTech
# The correct password is 12345
# The correct certifi is 2019.3.9
# The correct chardet is 3.0.4
# The correct idna is 2.8
# The correct requests is 2.220
# The correct urllib3 is 1.25.3

userName = input("Enter your username and password \nUsername: ")
passWord = input("\nPassword: ")
certifi = input("Enter your certification code \nCertification Code: ")
chardet = input("Enter your detection ID \nDetection ID: ")
idna = input("Enter your \nI-Domain Name: ")
requests = input("Enter your \nRequest Code: ")
urllib3 = input("Enter your URL: \n")

while userName == userName and password == password:
    if userName == 'bantamTech' and password == '12345':
        print("Now let's verify your certifications!")
        break
    elif userName != 'bantamTech' and password != '12345':
        print(
            "Your Username and Password are wrong!")
        userName = input(
            "\n\nUsername: ")
        password = input("Password: ")
        continue
    elif userName == 'bantamTech' and password != '12345':
        print("Your Password is wrong!")
        userName = input(
            "\n\nUsername: ")
        password = input("Password: ")
        continue
    elif userName != 'bantamTech' and password == '12345':
        print("Your Username is wrong!")
        userName = input(
            "\n\nUsername: ")
        password = input("Password: ")
        continue

while certifi == certifi and chardet == chardet:
    if certifi == '2019.3.9' and chardet == '3.0.4':
        print("Just a few more certifications to go!")
        break
    elif certifi != '2019.3.9' and chardet != '3.0.4':
        print(
            "Your certification code and detection ID are wrong!")
        certifi = input(
            "\n\nCertification Code: ")
        chardet = input("Detection ID: ")
        continue
    elif certifi == '2019.3.9' and chardet != '3.0.4':
        print("Your detection ID is wrong!")
        certifi = input(
            "\n\nCertification Code: ")
        chardet = input("Detection ID: ")
        continue
    elif certifi != '2019.3.9' and chardet == '3.0.4':
        print("Your certification code is wrong!")
        certifi = input(
            "\n\nCertification Code: ")
        chardet = input("Detection ID: ")
        continue

while idna == idna and requests == requests:
    if idna == '2.8' and requests == '2.220':
        print("Just a few more certifications to go!")
        break
    elif idna != '2.8' and requests != '2.220':
        print(
            "Your i-domain name and request code are wrong!")
        idna = input(
            "\n\nI-Domain Name: ")
        requests = input("Request Code: ")
        continue
    elif idna == '2.8' and requests != '2.220':
        print("Your request code is wrong!")
        idna = input(
            "\n\nI-Domain Name: ")
        requests = input("Request Code: ")
        continue
    elif idna != '2.8' and requests == '2.220':
        print("Your i-domain is wrong!")
        idna = input(
            "\n\nI-Domain Name: ")
        idna = input("Request Code: ")
        continue

while urllib3 == urllib3:
    if urllib3 == '1.25.3':
        print("Verification complete. You will now be transferred to our top secret site.")
        break
    elif urllib3 != '1.25.3':
        print(
            "Your URL is wrong!")
        urllib3 = input(
            "\n\nurllib3: ")
        continue
while userName == userName and password == password and certifi == certifi and chardet == chardet and idna == idna and requests == requests and urllib3 == urllib3:
    print("JSON Web Token being created")
    print(" (copy and send to user)")