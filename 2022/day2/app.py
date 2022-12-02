rock = "rock"
paper = "paper"
scissors = "scissors"
win = "win"
draw = "draw"
lose = "lose"

player_conversion = {  # decodes the input to the expected plays
    "X": rock,
    "Y": paper,
    "Z": scissors,
    "A": rock,
    "B": paper,
    "C": scissors,
}
scoring = {rock: 1, paper: 2, scissors: 3, lose: 0, draw: 3, win: 6}

# all outcomes are written from the perspective of playerB
game_result = {  # accessed with outcome[a][b], so outcome[rock][paper] == win
    rock: {rock: draw, paper: win, scissors: lose},
    paper: {rock: lose, paper: draw, scissors: win},
    scissors: {rock: win, paper: lose, scissors: draw},
}
outcome_conversion = {
    "X": lose,
    "Y": draw,
    "Z": win,
}  # decodes the input to the expected outcome
play_for_outcome = (
    {  # accessed with play_for_outcome[o][a], so play_for_outcome[win][rock] == paper
        win: {rock: paper, paper: scissors, scissors: rock},
        draw: {rock: rock, paper: paper, scissors: scissors},
        lose: {rock: scissors, paper: rock, scissors: paper},
    }
)


def round_part1(playerA, playerB) -> int:
    win_score = scoring[game_result[playerA][playerB]]
    choice_score = scoring[playerB]
    total = win_score + choice_score
    return total


def round_part2(playerA, outcome) -> int:
    playerB = play_for_outcome[outcome][playerA]
    return round_part1(playerA, playerB)


def convert_symbols_part1(line):
    a, b = line.strip().split(" ")
    return player_conversion[a], player_conversion[b]


def convert_symbols_part2(line):
    a, outcome = line.strip().split(" ")
    return player_conversion[a], outcome_conversion[outcome]


def part1():
    with open("input.txt", "r") as file_in:
        scores = [round_part1(*convert_symbols_part1(line)) for line in file_in]
    return sum(scores)


def part2():
    with open("input.txt", "r") as file_in:
        scores = [round_part2(*convert_symbols_part2(line)) for line in file_in]
    return sum(scores)


if __name__ == "__main__":
    print("expected: p1 = 10994, p2 = 12526")
    print(f"result:   p1 = {part1()}, p2 = {part2()}")
