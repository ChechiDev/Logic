# Connect-4: The Ultimate Game

## Description
Connect-4 is a Python-based implementation of the classic board game. The project includes a menu system, game logic, and utilities to manage the terminal and text formatting.

---

## Features
- **Menu System**:
  - Landing Menu with options like Register, Play Game, Game Rules, Statistics, Settings, and Exit.
  - Exit Menu for gracefully exiting the game.

- **Utilities**:
  - Terminal clearing functionality.
  - Text centering for better visual presentation.

- **Game Board**:
  - Basic setup for the game board.

---

## Project Structure
```
├── lib
│   ├── utils.py       # Utility functions for terminal and text formatting
│   ├── validation.py  # Validation logic for user inputs
│   └── __init__.py    # Initialization file for the lib module
├── board.py           # Game board setup and logic
├── game.py            # Main entry point for the game
├── logging.py         # Logging system for tracking events
├── menu.py            # Menu system for user interaction
├── user.py            # User management and profiles
├── README.md          # Project documentation
└── __pycache__        # Compiled Python files
```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Connect-4
   ```

2. Run the main game file:
   ```bash
   python game.py
   ```

---

## Requirements
- Python 3.13 or higher

---

## Future Improvements
- Implement the game logic for Connect-4.
- Add user authentication for Register and Sign In options.
- Enhance the board visualization.
- Add statistics tracking and settings customization.

---

## Author
This project was developed as part of a training exercise in Python logic and programming.

---

Feel free to suggest improvements or contribute to the project!