#dice simulator

import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}


class Die:
    def __init__(self):
        self._value = None  # Encapsulation: internal state

    def roll(self):
        """Abstraction: User doesn't know how the value is generated"""
        self._value = random.randint(1, 6)

    def display(self):
        """Abstraction: Hides internal logic of ASCII rendering"""
        if self._value is None:
            print("Roll the die first.")
            return
        for line in DICE_ART[self._value]:
            print(line)


class DiceGame:
    def __init__(self):
        self.die = Die()

    def play(self):
        print("Welcome to the Dice Rolling Simulator!")
        while True:
            user_input = input("Press Enter to roll the dice or 'q' to quit: ").strip()
            if user_input == 'q':
                print("Goodbye!")
                break
            elif user_input == '':
                self.die.roll()
                self.die.display()
            else:
                print("Invalid input. Press Enter to roll or 'q' to quit.")


if __name__ == "__main__":
    game = DiceGame()
    game.play()