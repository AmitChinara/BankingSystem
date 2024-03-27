import ExceptionClass as exp
from HelperClass import Helper
from Bank import Bank
from FileHandlingClass import FileHandle

def __init__(self):
    pass

class Main:
    bank_obj = Bank()
    def writeData(self):
        FileHandle().writeData(Main.bank_obj)
    def main(self):
        helper = Helper()
    
        while True:
            try:
                choice = input("Enter your choice: ('0' to display options) ")
                if choice == '0':
                    helper.displayMenu()
                elif choice == '1':
                    account_number = Main.bank_obj.accountCreation()
                    if account_number is not None:
                        print(f"Successfully created the account. Account Number: {account_number}")
                elif choice == '2':
                    account_number = Main.bank_obj.deposit()
                    if account_number is not None:
                        print(f"Successfully updated the balance in the Account Number: {account_number}")
                elif choice == '3':
                    balance = Main.bank_obj.withdrawal()
                    if balance is not None:
                        print(f"Your existing balance is: {balance}")
                elif choice == '4':
                    Main.bank_obj.balanceInquiry()
                elif choice == '5':
                    data = Main.bank_obj.closeAccount()
                    if data is not None:
                        print(f"Successfully closed the account for {data[0]} with a settlement of ${data[1]}")
                elif choice == '6':
                    raise KeyboardInterrupt
                else:
                    raise exp.InvalidChoiceException(choice)
            except exp.InvalidChoiceException as e:
                print(f"No action performed due to exception: {e}")
            except exp.InsufficientBalanceException as e:
                print(f'Withdrawal failed ({e})')
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
    except KeyboardInterrupt:
        print('\n++===============================================++'
              '\n||  Thank you for using the banking application  ||'
              '\n++===============================================++')
    finally:
        main.writeData()
        