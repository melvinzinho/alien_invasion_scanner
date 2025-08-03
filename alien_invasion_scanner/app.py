import random

alerts = []  # Empty list for decoded ones


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


def scan_signals(number_new_signals):
    new_signals = []

    for signal in range(number_new_signals):
        signal = random.randint(0, 10)
        new_signals.append(signal)

    return new_signals


def check_signals(signals_to_check):
    found_signal = []
    for signal in range(len(signals_to_check)):
        print(f"Checking signal number: '{signal}'...")

        if signals_to_check[signal] > 5:
            found_signal.append(signals_to_check[signal])
            print("\nAlert! Strong signal detected 👾\n")

    return found_signal


signals = scan_signals(5)
print(signals)

strong_signals = check_signals(signals)

print(strong_signals)
