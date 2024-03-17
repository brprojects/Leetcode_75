from collections import deque

# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The voting for this change is a round-based procedure. In each round, each 
# senator can exercise one of the two rights:

# Ban one senator's right: 
#     A senator can make another senator lose all his rights in this and all the following rounds.
#     Announce the victory: If this senator found the senators who still have rights to vote are 
#     all from the same party, he can announce the victory and decide on the change in the game.

# Given a string senate representing each senator's party belonging. The character 'R' and 'D' 
# represent the Radiant party and the Dire party.

# The round-based procedure starts from the first senator to the last senator in the given order. 
# This procedure will last until the end of voting. All the senators who have lost their rights 
# will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. 
# Predict which party will finally announce the victory and change the Dota2 game. The output 
# should be "Radiant" or "Dire".

# Solution: Implement a queue for Radiant and Dire positions from the senate list. Pop element from each queue and the 
# smaller one gets re-appended to its queue. Whichever queue runs out first loses
def predictPartyVictory(senate: str) -> str:
    rad = deque()
    dire = deque()
    for i in range(len(senate)):
        if senate[i] == 'R':
            rad.append(i)
        else:
            dire.append(i)
    counter = i + 1
    while rad and dire:
        if rad.popleft() < dire.popleft():
            rad.append(counter)
            counter += 1
        else:
            dire.append(counter)
            counter += 1
    if not rad:
        return 'Dire'
    else:
        return 'Radiant'

print(predictPartyVictory('RRDDDRD'))