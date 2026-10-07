# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose.** A Streamlit number-guessing game: pick a difficulty, guess the secret number within a limited number of attempts, and get Higher/Lower hints and a score.

**Bugs found** (full table in [reflection.md](reflection.md)):
- Fresh game started with 7 attempts instead of 8 (`attempts` initialized to 1).
- Higher/Lower hints were reversed in `check_guess`.
- On even-numbered attempts the secret was compared as a string, so hints were wrong every other guess.
- "Attempts left" did not update until a later rerun (it was drawn before the guess was processed).
- "New Game" kept the old score and ignored the difficulty range.

**Fixes applied:**
- Initialize `attempts` to 0 and redraw the attempts-left text after each guess.
- Return the correct hint for each outcome and always compare int to int.
- Reset score, status and history on New Game and pick the secret from the selected difficulty's range.
- Move the game logic into `logic_utils.py` and add pytest regression tests in `tests/test_game_logic.py`.

## 🧪 Test Output

Run `pytest`. Result: 7 passed (full output in [test_results.txt](test_results.txt)).

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
