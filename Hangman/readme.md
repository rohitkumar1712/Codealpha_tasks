# 🎮 Hangman Game (Python)

A simple command-line Hangman game built using Python. The player has to guess a randomly selected word one letter at a time before running out of attempts.

---

## 📌 Features

- Random word selection
- Input validation
- Tracks guessed letters
- Prevents duplicate guesses
- 6 incorrect attempts allowed
- Win and lose messages
- Beginner-friendly Python project

---

## 🛠️ Technologies Used

- Python 3
- Random module

---

## 📂 Project Structure

```
Hangman-Game/
│
├── hangman.py
└── README.md
```

---

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.

```bash
git clone https://github.com/your-username/Hangman-Game.git
```

3. Navigate to the project folder.

```bash
cd Hangman-Game
```

4. Run the program.

```bash
python hangman.py
```

---

## 🎯 How to Play

1. A random word is selected.
2. The word is displayed as underscores (_).
3. Enter one letter at a time.
4. If the letter exists, it is revealed.
5. If the letter is incorrect, one attempt is deducted.
6. You have **6 incorrect attempts**.
7. Guess the entire word before your attempts reach zero.

---

## 🖥️ Sample Output

```
===== HANGMAN GAME =====
Guess the word one letter at a time.

Word: _ _ _ _ _ _

Enter a letter: p
✅ Correct!

Word: p _ _ _ _ _

Enter a letter: x
❌ Wrong guess!
Remaining attempts: 5
```

---

## 📜 Rules

- Enter only one alphabet at a time.
- Repeated guesses are not allowed.
- Invalid inputs are rejected.
- Game ends when:
  - The word is guessed correctly.
  - All attempts are used.

---

## 📚 Concepts Used

- Variables
- Lists
- Loops
- Conditional Statements
- User Input
- Random Module
- String Manipulation

---

## 🚀 Future Improvements

- Add difficulty levels
- Larger word database
- ASCII Hangman graphics
- Hint system
- Scoreboard
- Play Again option
- Categories (Animals, Fruits, Programming, etc.)

---

## 👨‍💻 Author

Developed as a beginner Python project to practice programming fundamentals.

---

## 📄 License

This project is open-source and free to use for learning and educational purposes.