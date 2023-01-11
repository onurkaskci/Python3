import random

elements = ['🖖', '✊', '🤚']
print(elements)

player = int(input('Choose Your Element: '))
computer = int(random.randint(1,3))

if player == computer:
    print(f'You chose: {elements[player-1]}')
    print(f'Computer Chose: {elements[computer-1]}')
    print('Its a draw')
elif player > computer:
    print(f'You chose: {elements[player-1]}')
    print(f'Computer Chose: {elements[computer-1]}')
    print('You Win!')
elif computer > player:
    print(f'You chose: {elements[player-1]}')
    print(f'Computer chose: {elements[computer-1]}')
    print('Computer Wins!')