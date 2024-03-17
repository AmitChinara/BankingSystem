import ExceptionClass as exp


class Main:

    def __init__(self):
        pass

    def main(self):
        running = True
        while running:
            try:
                self.displayMenu()
                choice = input("Enter your choice: ")
                if choice == '1':
                    pass
                elif choice == '2':
                    pass
                elif choice == '3':
                    pass
                elif choice == '4':
                    pass
                elif choice == '5':
                    pass
                elif choice == '6':
                    running = False
                    print("Thank you for using the banking application")
                else:
                    raise exp.InvalidChoiceException(choice)
            except exp.InvalidChoiceException as e:
                print(f"No action performed due to exception: {e}")


if __name__ == '__main__':
    main = Main()
    print("The application has started")
    try:
        main.main()
        print("Application has been stopped")
    except Exception as e:
        print(f'The application has been terminated with error: {e}')
