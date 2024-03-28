import random

game_count = int(input('input game count: '))
turn_number = int(input('input turn count: '))
coin_defect = float(input('input coin defect parameter: '))
first_stack_input = int(input('input first stack: '))
second_stack_input = int(input('input second stack: '))
first_wins = 0
second_wins = 0
turn_count = 0

for _ in range(game_count):
    first_stack = first_stack_input
    second_stack = second_stack_input
    for _ in range(turn_number):
        randomness = random.random()
        if randomness > coin_defect:
            first_stack -= 1
            second_stack += 1
            turn_count += 1
        else:
            first_stack += 1
            second_stack -= 1
            turn_count += 1

        if first_stack == 0 or second_stack == 0:
            break
            
    if first_stack > second_stack:
        first_wins += 1
    else:
        second_wins += 1
print(f'first won {first_wins} times | second won {second_wins} times')
print(f'first loss probability is {1 - (first_wins / game_count)}')
print(f'second loss probability is {1 - (second_wins / game_count)}')
print(f'turn count {turn_count} , average game length {turn_count / game_count}')
