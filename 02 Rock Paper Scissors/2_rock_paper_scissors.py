

with open('02 Rock Paper Scissors\input.txt', 'r') as f:
    strat_guide = f.readlines()
    strat_guide = list(map(str.strip, strat_guide))       # remove \n for each element and convert it into the list
    # strat_guide = ['A Y', 'B X', 'C Z']

""" Part I """
def draw_game(strat_guide):
    total_score_draw = 0
    for round in strat_guide:
        if round[0] == 'A' and round[2] == 'X':       # rock
            total_score_draw += 4
        elif round[0] == 'B' and round[2] == 'Y':      # paper
            total_score_draw += 5
        elif round[0] == 'C' and round[2] == 'Z':      # scissors
            total_score_draw += 6

    return total_score_draw


def win_game(strat_guide):
    total_score_win = 0
    for round in strat_guide:
        if round[0] == 'A' and round[2] == 'Y':    # rock / paper
            total_score_win += 8
        elif round[0] == 'B' and round[2] == 'Z':  # paper / scissors
            total_score_win += 9
        elif round[0] == 'C' and round[2] == 'X':  # scissors / rock
            total_score_win += 7

    return total_score_win


def loss_game(strat_guide):
    total_score_loss = 0
    for round in strat_guide:
        if round[0] == 'A' and round[2] == 'Z':    # rock / scissors
            total_score_loss += 3
        elif round[0] == 'B' and round[2] == 'X':  # paper / rock
            total_score_loss += 1
        elif round[0] == 'C' and round[2] == 'Y':  # scissors / paper
            total_score_loss += 2

    return total_score_loss


# total_score = loss_game(strat_guide) + win_game(strat_guide) + draw_game(strat_guide)
# print(total_score)

""" Part II """

def loss(strat_guide):
    total_score_loss = 0
    for round in strat_guide:
        if round[2] == 'X' and round[0] == 'A':     # scissors / rock
            total_score_loss += 3
        elif round[2] == 'X' and round[0] == 'B':   # rock / paper
            total_score_loss += 1
        elif round[2] == 'X' and round[0] == 'C':   # paper / scissors
            total_score_loss += 2
    return total_score_loss


def draw(strat_guide):
    total_score_draw = 0
    for round in strat_guide:
        if round[2] == 'Y' and round[0] == 'A':     # rock / rock
            total_score_draw += 4
        elif round[2] == 'Y' and round[0] == 'B':   # paper / paper
            total_score_draw += 5
        elif round[2] == 'Y' and round[0] == 'C':   # scissors / scissors
            total_score_draw += 6
    return total_score_draw

def win(strat_guide):
    total_score_win = 0
    for round in strat_guide:
        if round[2] == 'Z' and round[0] == 'A':     # paper / rock
            total_score_win += 8
        elif round[2] == 'Z' and round[0] == 'B':   # scissors / paper
            total_score_win += 9
        elif round[2] == 'Z' and round[0] == 'C':   # rock / scissors
            total_score_win += 7
    return total_score_win

total_score = draw(strat_guide) + win(strat_guide) + loss(strat_guide)
print(total_score)