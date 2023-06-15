"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 4 - Working With Lists - Working with Part of a List
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('A list:', players)
print('Its [0:3] slice:', players[0:3])
print('Its [1:4] slice:', players[1:4])
print('Its [:4] slice:', players[:4])
print('Its [2:] slice:', players[2:])
print('Its [-3:] slice:', players[-3:])

print("Loop on the first three players:")
for player in players[:3]:
    print(player.title())

# shallow copy
alt_players = players
print(players)
# change on shallow copy ...
alt_players[0] = 'tom'
# ... affect the actual source
print(players)

# deep copy
cp_players = players[:]
# change on deep copy ...
cp_players[0] = 'bob'
# ... do affect the actual source
print(cp_players, players)
