# 🚦 CCTV Rush Hour Game (Python)

A simple terminal-based traffic control betting game built with Python.
In this game, you act as a traffic signal controller and bet money on whether traffic will move smoothly or result in a crash.

---

## 🎮 Gameplay Overview

* You start with **₹100**.
* Each round:

  * Random traffic is generated in four directions: **North, South, East, West**.
  * You place a bet.
  * You choose which signal to turn green:

    * **North-South**
    * **East-West**
* If conflicting traffic exists → 💥 **Crash** → You lose money
* If traffic flows safely → ✅ **Win** → You earn money

The game continues until:

* You run out of money 💸
* Or you choose to quit ❌

---

## 🧠 Game Logic

* Traffic is randomly generated (0–5 vehicles per direction)
* Only opposite directions are safe together:

  * North ↔ South
  * East ↔ West
* If vehicles exist in crossing directions → crash occurs

---

## 📦 Requirements

* Python 3.x

No external libraries required (uses only built-in modules).

---

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/cctv-rush-hour-game.git
   ```

2. Navigate to the project folder:

   ```bash
   cd cctv-rush-hour-game
   ```

3. Run the game:

   ```bash
   python game.py
   ```

---

## 🖥️ Sample Output

```
🎮 CCTV Rush Hour Game Started!

💰 Your Balance: 100
Enter your bet amount: 20

🚦 Current Traffic स्थिति:
North: 🚗🚗 (2)
South: 🚗 (1)
East: 🚗🚗🚗 (3)
West:  (0)

Choose signal:
1. North-South Green
2. East-West Green
Enter choice (1/2): 1

⏳ Processing traffic...

💥 CRASH! You lost the bet.
💰 Updated Balance: 80
```

---

## 📁 Project Structure

```
cctv-rush-hour-game/
│
├── game.py        # Main game file
└── README.md      # Project documentation
```

---

## 🚀 Future Improvements

* Add difficulty levels
* Introduce traffic patterns (rush hour logic)
* GUI version using Tkinter or Pygame
* Sound effects and animations
* Scoreboard system

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

Created as a fun Python project to practice:

* Functions
* Loops
* Conditionals
* User input handling

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐** on GitHub!

---
