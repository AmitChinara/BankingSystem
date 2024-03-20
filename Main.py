import ExceptionClass as exp
from HelperClass import Helper
from Bank import Bank


class Main:

    def __init__(self):
        pass

    def main(self):
        running = True
        helper = Helper()
        bank_obj = Bank()
        bank_obj.loadData()

        while running:
            try:
                choice = input("Enter your choice: ('0' to display options) ")
                if choice == '0':
                    helper.displayMenu()
                elif choice == '1':
                    account_number = bank_obj.accountCreation()
                    if account_number is not None:
                        print(f"Successfully created the account. Account Number: {account_number}")
                elif choice == '2':
                    account_number = bank_obj.deposit()
                    if account_number is not None:
                        print(f"Successfully updated the balance. Account Number: {account_number}")
                elif choice == '3':
                    pass
                elif choice == '4':
                    bank_obj.balanceInquiry()
                elif choice == '5':
                    pass
                elif choice == '6':
                    running = False
                    print("Thank you for using the banking application")
                else:
                    raise exp.InvalidChoiceException(choice)
            except exp.InvalidChoiceException as e:
                print(f"No action performed due to exception: {e}")
            except ValueError as e:
                print(f"Invalid number provided: {e}")
            except exp.AccountNumberNotFoundException as e:
                print(f"ERROR: {e}")
            except exp.InvalidAmountException as e:
                print(f"ERROR: {e}")


if __name__ == '__main__':
    main = Main()
    print("The application has started")
    try:
        main.main()
        print("Application has been stopped")
    except Exception as e:
        print(f'The application has been terminated with error: {e}')
