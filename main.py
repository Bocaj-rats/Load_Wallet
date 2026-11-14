"""Menu-driven program for the Cellphone Load Wallet."""

from load_wallet import LoadWallet


def ask_number(prompt):
    while True:
        number = input(prompt).strip()
        if number.isdigit() and len(number) == 11 and number.startswith("09"):
            return number
        print("Invalid number. Use 11 digits starting with 09.")


def ask_amount(prompt, allow_zero=False):
    while True:
        amount = input(prompt).strip()
        try:
            return LoadWallet._check_money(amount, allow_zero=allow_zero)
        except ValueError as error:
            print(f"Invalid amount: {error}")


def ask_network(prompt="Select network"):
    while True:
        print("\n1. Globe   2. Smart   3. DITO")
        choice = input(f"{prompt} (1-3): ").strip()
        networks = {"1": "Globe", "2": "Smart", "3": "DITO"}
        if choice in networks:
            return networks[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


def create_wallet():
    print("=" * 44)
    print("        CELLPHONE LOAD WALLET")
    print("=" * 44)

    while True:
        owner = input("Enter owner name: ").strip()
        if owner:
            break
        print("Owner name cannot be empty.")

    mobile = ask_number("Enter mobile number (09XXXXXXXXX): ")
    network = ask_network("Your network")
    balance = ask_amount("Enter starting balance (PHP): ", allow_zero=True)
    wallet = LoadWallet(owner, mobile, balance, network)
    print("\nWallet created successfully!")
    return wallet


def main():
    try:
        wallet = create_wallet()

        while True:
            print("\n" + "=" * 44)
            print("               MAIN MENU")
            print("=" * 44)
            print("1. Top Up Load")
            print("2. Send Load (Same Network)")
            print("3. Send with Fee (Different Network)")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                amount = ask_amount("Enter top-up amount (PHP): ")
                wallet.top_up(amount)
                print(f"Success! Added PHP {amount:.2f}.")
                print(f"Updated balance: PHP {wallet.balance:.2f}")

            elif choice in ("2", "3"):
                recipient = ask_number("Enter recipient number: ")
                network = ask_network("Recipient network")
                amount = ask_amount("Enter load amount (PHP): ")
                try:
                    if choice == "2":
                        wallet.send_load(recipient, amount, network)
                        print(f"Success! Sent PHP {amount:.2f} to {recipient}.")
                    else:
                        sent, fee, total = wallet.send_with_fee(recipient, amount, network)
                        print(f"Success! Sent PHP {sent:.2f} to {recipient}.")
                        print(f"Service fee: PHP {fee:.2f} | Total deducted: PHP {total:.2f}")
                    print(f"Remaining balance: PHP {wallet.balance:.2f}")
                except ValueError as error:
                    print(f"Transaction failed: {error}")

            elif choice == "4":
                print("\n--- WALLET DETAILS ---")
                print(wallet.show_balance())

            elif choice == "5":
                print("Thank you for using Cellphone Load Wallet!")
                break

            else:
                print("Invalid option. Please choose from 1 to 5.")

    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed.")


if __name__ == "__main__":
    main()
