from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

#save password
# retrieves password
# main program loop
# The program will ask you for the name of the account you want to access. So, you type in "Instagram".
# The program searches for "Instagram" in its list of saved passwords, finds the encrypted password associated with that account, and decrypts it.
# The decrypted (original) password for your Instagram account is then displayed on the screen.

def save_password(account, password): 
    encrypted_password = cipher_suite.encrypt(password.encode())
    with open("passwords.txt", "a") as file:
        file.write(f"{account}:{encrypted_password.decode()}\n")
    print("Password saved!")

def get_password(account):
    with open("passwords.txt", "r") as file:
        for line in file:
            stored_account, encrypted_password = line.strip().split(":")
            if stored_account == account:
                decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode() # encodes converts string to bytes,decode does the opposite
                print(f"Password for {account}: {decrypted_password}")
                return
    print("Account not found. ")

master = input("set a master password: ")

def authenticate():
    password = input("enter your master password")
    return password == master_password

def main():
    if not authenticate():
        print("Authentication failed. ")
        return
    
    while True:
        action = input("Would you like to save or get a password? type either save or get or exit: ").lower()
        if action == "save":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            save_password(account, password)

        elif action == "get":
            account = input("Enter account name: ")
            get_password(account)
        elif action == "exit":
            break
        else:
            print("Invalid action. ")

if __name__ == "__main__":
    main()