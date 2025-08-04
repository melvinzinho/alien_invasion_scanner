# 👽 Alien Invasion Scanner

## 📖 Overview
This is a fun, console-based Python game where you act as a commander scanning signals for alien activity. Detect strong signals, uncover aliens, and log your findings. It's simple, text-based, and perfect for quick plays or learning basic Python concepts like loops, randomness, and file handling.

Inspired by sci-fi themes, the game features ASCII art for aliens and an intro screen. Your goal: Scan signals without letting too many alerts pile up—or face an invasion!

## 🛠️ Requirements
- Python 3.x (tested on 3.12, but should work on most versions)
- No external libraries needed—just standard `random` and `time` modules.
- A terminal or command prompt to run the script.

## 🚀 How to Run
1. Clone or download the project files (including `app.py` and the `alien_invasion_scanner` folder for logs).
2. Open a terminal in the project directory.
3. Run the script:
   ```
   python app.py
   ```
4. Follow the on-screen prompts to play!

## 🎮 Gameplay Guide
- **Start the Game**: Type "Yes" to begin scanning.
- **Choose Signals**: Enter how many signals to scan (e.g., 5).
- **Scan for Aliens**: Decide to scan now ("Yes") or skip ("No").
- **Alerts**: If signals are strong (>5), you'll get alerts. Too many? Alien invasion!
- **Log Findings**: View past alien detections with "Log".
- **Quit**: Type "No" to end the transmission.

Example session:
- Intro ASCII art appears.
- Scan 10 signals.
- Detect alerts and possibly an alien—logged automatically.

## 📁 Project Structure
- `app.py`: Main game script.
- `alien_invasion_scanner/log.txt`: Stores timestamps of alien findings (e.g., "Alien found at Sun Aug 3 19:39:22 2025").

## 🔍 Features
- **Random Signal Generation**: Simulates real-time scanning with random values.
- **ASCII Art**: Fun visuals for intro and aliens.
- **Logging System**: Saves detections to a file and views them on demand.
- **Input Validation**: Handles invalid entries gracefully.
- **Replayable**: Loop until you quit.

## 💡 Tips
> 🚨 *Pro Tip: Scan more signals for higher invasion chances—but don't overdo it!*

> 📝 *Note: Logs are appended, so they persist across runs. Clear `log.txt` if needed.*

## 🐛 Known Issues
- No error handling for file permissions (ensure write access to log folder).
- Purely random— no advanced AI or persistence beyond logs.

## 📈 Next Steps
- ⬜ Add multiplayer mode for competing scanners.
- ⬜ Include sound effects using a library like `playsound`.
- ⬜ Expand with levels or customizable signal thresholds.
- ⬜ Contribute: Fork and PR improvements!
