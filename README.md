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

- [✔] Describe the game's purpose.
  The game's purpose was to not only test the user's ability to use context and hints as best as possible to figure out the right answer, but most importantly for the developer to see how a user may interact with the game that would cause edge cases to appear.
- [✔] Detail which bugs you found.
  - the range of guessing in between 1 - 100 seems to be broken. i guessed for the number 0 and it told me to "go lower". The same applies for guessing with 100.
  - the game allows me to go to a negative number of guesses. for example: "Attempts left: -2"
  - whenever you change the difficulty of the game, the expected behavior is for the range of guessing numbers to get smaller, but that is not reflected on the page.
- [✔] Explain what fixes you applied.
- 1. I swapped the "Too High" and "Too Low" messages to match the correct direction since they were flipped, and also made sure to always compare the secret to an integer rather than a string.
  2. I moved the incrementation logic inside the ELSE block having to do with this logic, so that it only runs when parse_guess succeeded. Now the "Attempts left" will never be able to go below 0. Invalid inputs are not rejected with a message to let the user know.
  3. I added a check to check IF the stored difficulty is different than the one selected, then the code needs to grab a new secrete and update the stored difficulty. I also changed the hardcoded range being "1 to 100" to "between {low} and {high}" I also changed the button's logic (which was also hardcoded) from randint(1, 100) to randint(low, high) which is grabbing from the stored difficulty as correctly expected.

## 📸 Demo

- [✔] [Insert a screenshot of your fixed, winning game here]

<img width="1890" height="930" alt="Screenshot 2026-03-08 at 10 57 29 PM" src="https://github.com/user-attachments/assets/af6566b7-042a-4847-8c25-ccaeb8988e9a" />



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
