import Functions as fn
import getpass
print(" Welcome to SSAT Bank ATM ")
while True:
    print("\nMain Menu:")
    print("1. Login")
    print("2. Create Account")
    print("3. Settings")
    print("0. Exit")
    choice = input("Choose an option: ")
    if choice == "0":
        print("Thank you for using the ATM. Goodbye!")
        break
    elif choice == "1":
        print("\n Login:")
        acc_id = input("Enter your ID: ")
        password = getpass.getpass("Enter your Password: ")
        account = fn.find_account_by_id(acc_id)
        if account and account["pin"] == password:
            print(f"\n Welcome, {account['name']}!")
            while True:
                print("\n-- Account Menu --")
                print("1. Withdraw Money")
                print("2. Deposit Money")
                print("3. Balance Check")
                print("0. Logout")
                option = input("Choose an option: ")
                if option == "1":
                    amt = float(input("Enter amount to withdraw: ₹"))
                    print(fn.withdraw_money(account, amt))
                elif option == "2":
                    amt = float(input("Enter amount to deposit: ₹"))
                    print(fn.deposit_money(account, amt))
                elif option == "3":
                    print(f" Current Balance: ₹{account['balance']}")
                elif option == "0":
                    print("Logged out successfully.")
                    break
                else:
                    print(" Invalid option.")
        else:
            print(" Invalid ID or password!")
    elif choice == "2":
        print("\n  Create Account:")
        name = input("Full Name     : ")
        acc_id = input("Account ID    : ")
        email = input("E-mail ID     : ")
        password = getpass.getpass("Create PIN    : ")
        if fn.find_account_by_id(acc_id):
            print(" Account ID already exists!")
        else:
            fn.create_account(name, acc_id, email, password)
            print(" Account created successfully!")
    elif choice == "3":
        while True:
            print("\n  Settings Menu:")
            print("1. Forgot Password")
            print("2. Find ID")
            print("0. Back")
            setting_choice = input("Choose an option: ")
            if setting_choice == "0":
                break
            elif setting_choice == "1":
                acc_id = input("Enter your Account ID: ")
                account = fn.find_account_by_id(acc_id)
                if account:
                    new_password = getpass.getpass("Enter New Password: ")
                    fn.reset_password(account, new_password)
                    print(" Password reset successful!")
                else:
                    print(" Account not found!")
            elif setting_choice == "2":
                email = input("Enter your registered E-mail ID: ")
                ids = fn.find_ids_by_email(email)
                if ids:
                    print(" Account ID(s) linked to your email:", ", ".join(ids))
                else:
                    print(" No account found with that email.")
            else:
                print(" Invalid option.")
    else:
        print(" Invalid option. Try again.")
