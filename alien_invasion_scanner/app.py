import random

alerts = []  # Empty list for decoded ones

# IDEA: add a function to save when user found alien and register time of this and provide option of user to view log


def print_intro():
    print(
        f"""

           _ _              _____                     _                _____                                 
     /\   | (_)            |_   _|                   (_)              / ____|                                
    /  \  | |_  ___ _ __     | |  _ ____   ____ _ ___ _  ___  _ __   | (___   ___ __ _ _ __  _ __   ___ _ __ 
   / /\ \ | | |/ _ \ '_ \    | | | '_ \ \ / / _` / __| |/ _ \| '_ \   \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  / ____ \| | |  __/ | | |  _| |_| | | \ V / (_| \__ \ | (_) | | | |  ____) | (_| (_| | | | | | | |  __/ |   
 /_/    \_\_|_|\___|_| |_| |_____|_| |_|\_/ \__,_|___/_|\___/|_| |_| |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                                                             
                                                                                                             

"""
    )


def print_alien():
    print(
        f"""
     o            o
      \          /
       \        /
        :-'""'-:
     .-'  ____  `-.
    ( (  (_()_)  ) )
     `-.   ^^   .-'
        `._==_.'
         __)(___                                                                                                            
"""
    )


# TODO: Handle cases where the user enters non-numeric input
def ask_user_for_amount_of_signals():
    return int(input("2️⃣  How many signals would you like to scan: "))


def scan_signals(number_new_signals):
    new_signals = []

    for signal in range(number_new_signals):
        signal = random.randint(0, 10)
        new_signals.append(signal)

    return new_signals


def check_signals(signals_to_check):

    user_choice_2 = (
        input(
            "3️⃣  Would you like to scan signals now? Type 'Yes' to scan or 'No' to skip: "
        )
        .strip()
        .capitalize()
    )
    if user_choice_2 == "Yes":
        print("")

        for signal in range(len(signals_to_check)):
            print(f"🔍 Scanning signal {signal}... no alien activity detected.")

            if signals_to_check[signal] > 5:
                alerts.append(signals_to_check[signal])
                print("\n👽 Alert! Strong signal detected 👾\n")

            if len(alerts) > 3:
                print("************************")
                print("🚨🚨 ALIEN FOUND!!! 🚨🚨")
                print("************************")
                print_alien()
                break

    elif user_choice_2 == "No":
        print("⛔ Skipping signal scan for now.")

    else:
        print("❌ Invalid Input.")


print_intro()

while True:
    user_choice = (
        input("\n1️⃣  Would you like to play? Type: 'Yes' to play or 'No' to not play: ")
        .strip()
        .capitalize()
    )

    if user_choice == "Yes":
        number_of_signals_to_scan = ask_user_for_amount_of_signals()
        list_signal = scan_signals(number_of_signals_to_scan)
        check_signals(list_signal)

    elif user_choice == "No":
        print("👽 Transmission ended. Goodbye, Commander!")
        break

    else:
        print("❌  Invalid Input. \n")
        continue
