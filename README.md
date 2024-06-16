Certainly! Here’s how your GitHub README would look with the actual Python code snippets included:

---

## Python Scripts Collection

Welcome to my Python scripts repository! This collection showcases several scripts demonstrating different functionalities.

### 1. Double Dice Rolls (`double_dice_rolls.py`)

This script simulates rolling two six-sided dice multiple times and calculates the mean of the sums.

```python
import random

n = int(input('Number of double rolls: '))
ats = []
for i in range(n):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sumn = dice1 + dice2
    ats.append(sumn)

mean = sum(ats) / n
print(mean)
print('*' * 80)
```

#### Definition:
- **Functionality:** Generates random dice rolls, computes their sums, and calculates the mean.
- **Usage:** 
  1. Run the script.
  2. Enter the number of double rolls when prompted.
  3. The script will output the mean of the sums of dice rolls.

### 2. Rock-Paper-Scissors Game (`rock_paper_scissors.py`)

This script allows you to play a simple rock-paper-scissors game against a bot.

```python
import random

ALLOWED = ['R', 'P', 'S']

while True:
    name = input('> Player name: ')
    pandm = {}
    player = input('> Your move: ')
    if player not in ALLOWED:
        print('> Please enter valid move')
        continue

    pandm[player] = name

    bot = 'bot'
    num = random.randint(0, 2)
    if num == 0:
        ia = 'R'
    elif num == 1:
        ia = 'P'
    else:
        ia = 'S'
    bandm = {}
    bandm[ia] = bot

    players = player, ia

    if player == ia:
        print(f'It\'s a tie')
    elif player == 'R' and ia == 'S':
        print(f'{pandm[player]} wins.')
    elif player == 'S' and ia == 'P':
        print(f'{pandm[player]} wins.')
    elif player == 'P' and ia == 'R':
        print(f'{pandm[player]} wins.')
    else:
        print(f'{bandm[ia]} wins.')

    print('*' * 80)

    keepPlaying = input('Keep playing? (y/n): ')
    if keepPlaying == 'n':
        quit()
```

#### Definition:
- **Functionality:** Implements a classic rock-paper-scissors game with a random bot opponent.
- **Usage:** 
  1. Run the script.
  2. Enter your name and your move (R for Rock, P for Paper, S for Scissors).
  3. The bot randomly selects its move.
  4. The script determines the winner and prints the result.
  5. You can choose to keep playing or quit.

### Instructions:

- **Setup:**
  - Ensure Python is installed on your system.
  - Clone the repository:
    ```
    git clone https://github.com/your_username/your_repository.git
    ```
  - Navigate into the repository:
    ```
    cd your_repository
    ```

- **Running Scripts:**
  - Execute any script using Python:
    ```
    python script_name.py
    ```

Feel free to explore and modify these scripts as needed! If you have any questions or suggestions, please let me know.

---

Replace `your_username` and `your_repository` with your actual GitHub username and repository name. This version includes the actual Python code snippets, providing users with both the code and its explanations in a structured and informative manner.
