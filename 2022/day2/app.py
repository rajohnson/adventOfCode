# A, X is rock
# B, Y is paper
# C, Z is scissors
scoringA = {"A": 1, "B": 2, "C": 3}
scoringB = {"X": 1, "Y": 2, "Z": 3}
outcome_scores = {"W": 6, "D": 3, "L": 0}


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


def round(playerA, playerB) -> int:
    win_score = outcome_scores[game_result(playerA, playerB)]
    choice_score = scoringB[playerB]
    total = win_score + choice_score
    return total


def main():
    with open("input.txt", "r") as file_in:
        scores = [round(*line.strip().split(" ")) for line in file_in]
    print(scores)
    return sum(scores)


if __name__ == "__main__":
    print(main())
