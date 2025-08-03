signals = [3, 7, 2, 8, 4]  # List of alien signals

alerts = []  # Empty list for decoded ones

for signal in signals:  # Loop through each
    if signal > 5:  # Conditional check
        alerts.append(signal)
        print("Alert! Strong signal detected 👾")

while len(alerts) < 3:  # While loop for more scans
    new_signal = int(input("Scan next? Enter number: "))
    if new_signal > 5:
        alerts.append(new_signal)
