import random

signals = []  # List of alien signals
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


def scan_signals(number_signal):
    for signal in range(number_signal):
        signal = random.randint(0, 10)
        signals.append(signal)


def check_signals():
    for signal in signals:  # Loop through each
        if signal > 5:  # Conditional check
            alerts.append(signal)
            print("Alert! Strong signal detected 👾")


while len(alerts) < 3:  # While loop for more scans
    new_signal = int(input("How many scans would you like? Enter number: "))
    scan_signals(int(new_signal))
    print("checking...")
    check_signals()
