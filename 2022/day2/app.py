player_conversion = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
outcome_conversion = {"X": "lose", "Y": "draw", "Z": "win"}
scoring = {"rock": 1, "paper": 2, "scissors": 3, "lose": 0, "draw": 3, "win": 6}


def game_result(playerA, playerB):
    if playerA == "rock":
        if playerB == "rock":
            return "draw"
        elif playerB == "paper":
            return "win"
        else:  # scissors
            return "lose"
    elif playerA == "paper":
        if playerB == "rock":
            return "lose"
        elif playerB == "paper":
            return "draw"
        else:  # scissors
            return "win"
    else:  # scissors
        if playerB == "rock":
            return "win"
        elif playerB == "paper":
            return "lose"
        else:  # scissors
            return "draw"


def round_part1(playerA, playerB) -> int:
    win_score = scoring[game_result(playerA, playerB)]
    choice_score = scoring[playerB]
    total = win_score + choice_score
    return total


def play_for_outcome(playerA, outcome):
    if outcome == "lose":
        if playerA == "rock":
            return "scissors"
        elif playerA == "paper":
            return "rock"
        else:  # scissors
            return "paper"
    elif outcome == "draw":
        if playerA == "rock":
            return "rock"
        elif playerA == "paper":
            return "paper"
        else:  # scissors
            return "scissors"
    else:  # win
        if playerA == "rock":
            return "paper"
        elif playerA == "paper":
            return "scissors"
        else:  # scissors
            return "rock"


def round_part2(playerA, outcome) -> int:
    playerB = play_for_outcome(playerA, outcome)
    win_score = scoring[game_result(playerA, playerB)]
    choice_score = scoring[playerB]
    total = win_score + choice_score
    return total


def convert_symbols_to_plays_part1(line):
    a, b = line.strip().split(" ")
    return player_conversion[a], player_conversion[b]


def convert_symbols_to_plays_part2(line):
    a, outcome = line.strip().split(" ")
    return player_conversion[a], player_conversion[outcome]


def part1():
    with open("input.txt", "r") as file_in:
        scores = [
            round_part1(*convert_symbols_to_plays_part1(line)) for line in file_in
        ]
    return sum(scores)


def part2():
    with open("input.txt", "r") as file_in:
        scores = [
            round_part2(*convert_symbols_to_plays_part2(line)) for line in file_in
        ]
    return sum(scores)


if __name__ == "__main__":
    print(f"p1 = 10994, p2 = 12526")
    print(part1())
    print(part2())
