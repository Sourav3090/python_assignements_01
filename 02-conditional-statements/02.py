# 2. Task: Cricket Stats Analyzer
# ● Objective: Write a script to analyze cricket stats for a team.
# ● Hints:
# ○ Prompt the user to input the runs scored by each of the five players in a
# cricket match.
# ○ For each player (Player 1 to Player 5) ask the user to input the runs they
# scored.
# ○ Calculate the total runs scored by all players and the average runs.
# ○ Display the total runs and average runs to the user.

player1=int(input("enter player 1 runs : "))
player2=int(input("enter player 2 runs : "))
player3=int(input("enter player 3 runs : "))
player4=int(input("enter player 4 runs : "))
player5=int(input("enter player 5 runs : "))

total_runs=player1+player2+player3+player4+player5
print(f"TOTAL RUNS SCORE BY ALL PLAYERS : {total_runs}")

avg_runs= total_runs/5
print(f"THE AVERAGE OF RUNS SCORED BY ALL PLAYERS : {avg_runs}")
