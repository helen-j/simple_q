"""
Created on Tue Jan 9th 2018
@author: Helen Jeffrey
Code@ 

"""

# =========================
# Imports
# =========================

import numpy as np
import timeit
import random


# =========================
# Parameters
# =========================

GAMMA       = 0.7

numstates   = 4
numactions  = 4
numturns    = 100
actions     = [0,1,2,3]
action      = 0
solved      = False

initialState = [1,0,1,1]
finalState  = [1,1,1,1]
completedActions = []
state       = []

# Initialize Q-table with all zeros
# Q values will be calculated as state/action are tested
qtable = []


# ---------------------------------------------------------------------
start = timeit.timeit()

# ---------------------------------------------------------------------

def updateState(action):
    #change state vector
    #based on action
    if state[action] ==1:
        state[action]==0
    else:
        state[action]==1

# ---------------------------------------------------------------------
def checkSolved():
    if (state == finalState):
        solved=True
        return 1000
    else :
        return 0

# ---------------------------------------------------------------------
def initializeState():
    print("debug: initializeState()", initialState)
    state=initialState
    solved=False

# ---------------------------------------------------------------------
def initializeQTable():
    print("debug: initializeQTable()", numstates, numstates, numactions)
    qtable = []
    qtable = np.zeros((numstates, numstates, numactions))#array of zeros

# ---------------------------------------------------------------------
def explore(agent):
    print("debug: explore()")
    initializeState()

    counter=0
    while (not solved):
        currentAction = agent.randomAction()
        currentState = updateState(currentAction)
        checkSolved(currentState)

        counter=counter+1

        #agent.reward = (calculateQ())

#        Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)] http://mnemstudio.org/path-finding-q-learning-tutorial.htm
        ####Q learning formula Q(s,a) = Rimm + GAMMA*Q(s,a)-1
#       Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a]) #https://github.com/awjuliani/DeepRL-Agents/blob/master/Q-Table.ipynb
#

# ---------------------------------------------------------------------
def exploit(agent):
    print("debug: exploit()")
    initializeState()

    counter = 0
    while (not solved):
        # use BEST action (highest Q-value for this state from the qtable
        # ? Choose an action by greedily (with noise) picking from Q table
        #currentAction(qtable[s, :]
        currentAction = agent.bestAction(qtable)

        updateState(currentAction)
        currentState = updateState(currentAction)
        immreward = checkSolved(currentState)
        agent.reward = (calculateQ(immreward))

        counter = counter + 1
    pass


# ---------------------------------------------------------------------
def calculateQ(agent, state, action, immreward):
    print("debug: calculateQ() ", agent, state, action, immreward)
    # =========================
    # Calculates the value of Q and updates qtable
    # =========================

    # agent.reward = (calculateQ())
    #        Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)] http://mnemstudio.org/path-finding-q-learning-tutorial.htm
    ####Q learning formula Q(s,a) = Rimm + GAMMA*Q(s,a)-1
    #       Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a]) #https://github.com/awjuliani/DeepRL-Agents/blob/master/Q-Table.ipynb
    #

    pass

# ---------------------------------------------------------------------
def checkSolved(currentAction):
    print("debug: checkSolved() ", currentAction)
    if (currentAction == finalState):
        return True
    else:
        return False


# ---------------------------------------------------------------------
def printQTable():
    print("debug: printQTable()")
    for action in actions:
        qtable[0, 0, action] = action

    print(qtable)


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
#def main():
    # =========================
    # Settings
    # =========================
print("debug: main()")

initializeQTable()
initializeState()


for x in range(numturns):
    if x % 2 == 0:
        explore(agent)
    else:
        exploit(agent)




# ---------------------------------------------------------------------

print(qtable)

end = timeit.timeit()
print("time to execute: ", (end - start))

    #printQTable()
