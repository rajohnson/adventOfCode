# A, X is rock
# B, Y is paper
# C, Z is scissors
scoringB = {"X": 1, "Y": 2, "Z": 3}
outcome_scores = {"W": 6, "D": 3, "L": 0}
# X lost
# Y draw
# Z win


def game_result(playerA, playerB):
    if playerA == "A":  # rock
        if playerB == "X":  # rock
            return "D"
        elif playerB == "Y":  # paper
            return "W"
        else:  # scissors
            return "L"
    elif playerA == "B":  # paper
        if playerB == "X":  # rock
            return "L"
        elif playerB == "Y":  # paper
            return "D"
        else:  # scissors
            return "W"
    else:  # scissors
        if playerB == "X":  # rock
            return "W"
        elif playerB == "Y":  # paper
            return "L"
        else:  # scissors
            return "D"


def round_part1(playerA, playerB) -> int:
    win_score = outcome_scores[game_result(playerA, playerB)]
    choice_score = scoringB[playerB]
    total = win_score + choice_score
    return total


def play_for_outcome(playerA, outcome):
    if outcome == "X":  # lose
        if playerA == "A":  # rock
            return "Z"
        elif playerA == "B":  # paper
            return "X"
        else:  # scissors
            return "Y"
    elif outcome == "Y":  # draw
        if playerA == "A":  # rock
            return "X"
        elif playerA == "B":  # paper
            return "Y"
        else:  # scissors
            return "Z"
    else:  # win
        if playerA == "A":  # rock
            return "Y"
        elif playerA == "B":  # paper
            return "Z"
        else:  # scissors
            return "X"


def round_part2(playerA, outcome) -> int:
    playerB = play_for_outcome(playerA, outcome)
    win_score = outcome_scores[game_result(playerA, playerB)]
    choice_score = scoringB[playerB]
    total = win_score + choice_score
    return total


def main():
    with open("input.txt", "r") as file_in:
        scores = [round_part2(*line.strip().split(" ")) for line in file_in]
    print(scores)
    return sum(scores)


if __name__ == "__main__":
    print(main())
