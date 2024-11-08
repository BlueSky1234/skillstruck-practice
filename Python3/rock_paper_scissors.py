player_a, player_b = input().split('@')
player_a = player_a.split()
player_b = player_b.split()

player_one_score = 0
player_two_score = 0

for rounds in range(len(player_a)):
    if player_a[rounds] == "rock" and player_b[rounds] == "scissors":
        player_one_score += 1
    elif player_a[rounds] == "paper" and player_b[rounds] == "rock":
        player_one_score += 1
    elif player_a[rounds] == "scissors" and player_b[rounds] == "paper":
        player_one_score += 1
    elif player_b[rounds] == "rock" and player_a[rounds] == "scissors":
        player_two_score += 1
    elif player_b[rounds] == "paper" and player_a[rounds] == "rock":
        player_two_score += 1
    elif player_b[rounds] == "scissors" and player_a[rounds] == "paper":
        player_two_score += 1
    else:
        pass

if player_one_score > player_two_score:
    print(f"Score of player a: {player_one_score} Score of player b: {player_two_score} Player a won!")
elif player_two_score > player_one_score:
    print(f"Score of player a: {player_one_score} Score of player b: {player_two_score} Player b won!")
else:
    print(f"Score of player a: {player_one_score} Score of player b: {player_two_score} Tie!")