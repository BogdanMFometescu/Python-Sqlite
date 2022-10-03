from register_user import BankAccount


class Main:
    user_BF = BankAccount("", "", 10)

    def __int__(self):
        pass

    if __name__ == "__main__":

        while True:
            user_BF.show_menu()
            menu_choice = input(
                "Please choose an option from the menu :")  # TODO - implement exception(ValueError) if needed
            match menu_choice:
                case "1":
                    user_BF.register_user()
                case "2":
                    user_BF.deposit()
                case "3":
                    user_BF.withdraw()
                case "4":
                    user_BF.show_user_balance()
                case "0":
                    break

                case "5":
                    user_BF.remove_user()

                case "6":
                    user_BF.delete_db()

                case _:
                    print("Please choose a valid option:")
