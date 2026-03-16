import string
from getpass import getpass

# Hello Testing 

def letter_limit(num_players: int) -> str:
    if num_players == 2:
        return "J"
    if num_players == 3:
        return "O"
    if num_players == 4:
        return "R"
    raise ValueError("Number of players must be 2, 3, or 4.")


def build_letters(last_letter: str) -> dict:
    all_letters = list(string.ascii_uppercase)
    end = all_letters.index(last_letter) + 1
    selected = all_letters[:end]

    letters = {}
    for i, ch in enumerate(selected, start=1):
        letters[ch] = {"need": i, "filled": 0}
    return letters


def all_completed(letters: dict) -> bool:
    return all(v["filled"] >= v["need"] for v in letters.values())


def print_status(players: list, letters: dict) -> None:
    print("\n" + "=" * 60)
    print("SCORES")
    for p in players:
        print(f"  {p['name']}: {p['score']}")

    print("\nLETTERS (filled/need)")
    row = []
    for ch in letters.keys():
        row.append(f"{ch}:{letters[ch]['filled']}/{letters[ch]['need']}")
        if len(row) == 8:
            print("  " + "   ".join(row))
            row = []
    if row:
        print("  " + "   ".join(row))
    print("=" * 60)


def get_secret_letter_input(letters: dict, prompt: str) -> str:
    valid = set(letters.keys())
    while True:
        # getpass hides what the player types
        choice = getpass(prompt).strip().upper()

        if len(choice) != 1 or choice not in valid:
            print("Invalid letter. Choose from the available letters shown.")
            continue

        if letters[choice]["filled"] >= letters[choice]["need"]:
            print("That letter is already completed. Pick another.")
            continue

        return choice


def get_guess_input(letters: dict, guesser_name: str) -> str:
    valid = set(letters.keys())
    while True:
        guess = input(f"{guesser_name}, guess the letter played: ").strip().upper()

        if len(guess) != 1 or guess not in valid:
            print("Invalid guess. Guess one of the available letters.")
            continue

        return guess


def apply_fill_and_score(player: dict, letters: dict, letter: str) -> None:
    letters[letter]["filled"] += 1
    filled = letters[letter]["filled"]
    need = letters[letter]["need"]

    if filled == need:
        player["score"] += 1
        print(f"{player['name']} completed {letter} and earned +1 point.")
    else:
        print(f"{player['name']} filled one box of {letter}. Now {letter} is {filled}/{need}.")


def main():
    print("LETTER BOXES GAME (CONTINUE UNTIL GUESSED RIGHT)\n")

    while True:
        try:
            num_players = int(input("How many players (2-4)? ").strip())
            if num_players not in (2, 3, 4):
                print("Enter 2, 3, or 4.")
                continue
            break
        except ValueError:
            print("Enter a number (2, 3, or 4).")

    players = []
    for i in range(1, num_players + 1):
        name = input(f"Enter name for Player {i}: ").strip()
        if not name:
            name = f"Player {i}"
        players.append({"name": name, "score": 0})

    last = letter_limit(num_players)
    letters = build_letters(last)

    current = 0
    while not all_completed(letters):
        print_status(players, letters)

        current_player = players[current]
        guesser = players[(current + 1) % num_players]

        print(f"\n{current_player['name']}'s TURN (you keep playing until {guesser['name']} guesses right).")

        # Player keeps playing until guesser guesses correctly
        while True:
            played = get_secret_letter_input(
                letters,
                f"{current_player['name']}, secretly type a letter to play: "
            )

            # Give guesser one chance to guess BEFORE fill happens
            print("\n" * 30)  # crude screen wipe so the letter isn't visible above
            guess = get_guess_input(letters, guesser["name"])

            if guess == played:
                print(f"Correct! {current_player['name']} loses the turn. No fill happens.")
                break  # end current player's turn immediately

            print("Wrong guess. Fill happens, and current player continues.")
            apply_fill_and_score(current_player, letters, played)

            if all_completed(letters):
                break

        current = (current + 1) % num_players

    print_status(players, letters)
    print("\nGAME OVER! All letters are completed.\n")

    max_score = max(p["score"] for p in players)
    winners = [p["name"] for p in players if p["score"] == max_score]

    if len(winners) == 1:
        print(f"Winner: {winners[0]} with {max_score} point(s)!")
    else:
        print(f"Tie between: {', '.join(winners)} with {max_score} point(s) each!")


if __name__ == "__main__":
    main()