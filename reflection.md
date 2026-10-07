# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|---|---|---|---|---|
| No input (fresh page load) | Game starts with 8 attempts remaining | 7 attempts remaining; clicking "New Game" starts at 8 | none | `app.py`, initialization of `st.session_state.attempts` (started at 1 instead of 0) |
| Guess of 1 (secret was 47) | Hint says go HIGHER | Hint says go LOWER | none | `app.py`, `check_guess()` |
| Guess of 50 (secret was 46) | Hint says go LOWER | Hint says go HIGHER | none | `app.py`, `check_guess()` |
| Submitted a guess | "Attempts left" drops immediately after submitting | Displayed value did not decrease until a later rerun | none | `app.py`, attempts-left display rendered before the submit handler updates `attempts` |
| Clicked "New Game" after scoring 65 | Score resets to 0 | Attempts reset, but score stayed at 65 | none | `app.py`, `new_game` button handling (did not reset `score`, `status`, `history`) |
| Guesses on even-numbered attempts | Hints are always consistent with the secret | Hints were wrong on every other attempt | none | `app.py`, secret converted to `str` on even attempts before `check_guess()` (found while reading the code) |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used chatgpt and Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

11 computes attempt_limit - st.session_state.attempts. With a limit of 8, a fresh page load shows 8 − 1 = 7, while after "New Game" it shows 8 − 0 = 8.

Fix: change line 96 to initialize with 0:
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I refreshed the app and retested the previous inputs.

- Describe at least one test you ran (manual or using pytest)

Used a regression test for 50 vs 46 and 1 vs 47 which failed previously but passed now. The bug was in check_guess and not the UI.

  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

it traced each symptom to a code location, turned the two reported wrong-hint cases into regression tests, and showed that the tests failed before the fix.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire script from top to bottom whenever the user interacts with the page, so ordinary variables reset every time. st.session_state is a dictionary that persists across those reruns, so it holds anything the game needs to remember, like the secret number, attempts and score. Because the script runs in order, anything drawn before a state update shows stale values until the next rerun, which caused my attempts-left bug.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Create a tester to autamate the testing with inputs and expected outputs And feeding them to the ai to generate a pytest.

- What is one thing you would do differently next time you work with AI on a coding task?

Nothing much.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

It makes debugging much faster and easier.
