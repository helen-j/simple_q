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
numtrials   = 1000
actions     = [0,1,2,3]
action      = 0
solved      = False

initialState = [1,0,1,1]
finalState  = [0,1,0,0]
completedActions = []
state       = []

# Initialize Q-table with all zeros
# Q values will be calculated as state/action are tested
qtable = []
qtable = np.zeros((numstates, numstates, numactions))#array of zeros


# ---------------------------------------------------------------------



def updateState(action):
    #change state vector
    #based on action
    if state[action] ==1:
        state[action]==0
    else:
        state[action]==1

def checkSolved():
    if (state == finalState):
        solved=True
        return 1000
    else :
        return 0

def initializeState():
    state=initialState
    solved=False

def explore(agent):
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

def exploit(agent):
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


def calculateQ(agent, state, action, immreward):

    # agent.reward = (calculateQ())
    #        Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)] http://mnemstudio.org/path-finding-q-learning-tutorial.htm
    ####Q learning formula Q(s,a) = Rimm + GAMMA*Q(s,a)-1
    #       Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a]) #https://github.com/awjuliani/DeepRL-Agents/blob/master/Q-Table.ipynb
    #

    pass

def checkSolved(currentAction):
    if (currentAction == finalState):
        return True
    else:
        return False


def printQTable():
    for action in actions:
        qtable[0, 0, action] = action

    print(qtable)


def main():
    # =========================
    # Settings
    # =========================

    start = timeit.timeit()

    # =========================
    # Set up environment, agent
    # =========================

    redAgent = AgentClass.Agent()
    computer = EnvironmentClass.Environment()
    qtable = np.zeros((numstates, numstates), dtype=np.float)#array of zeros

    # =========================
    # Train agent
    # =========================
    """
       # for x in range(MAXTURNS):
    
          #  for x in agentList:
             #  # '''# 1. Check state '''
    
               # '''# 2. Choose action '''
                #a = random.choice(possibleRedActions)
    
               # '''# 3. Perform Action '''
                #completedActions.append([x, redAgent.chooseAction(x)])
    
               # ''' #1. Check state '''
    
               # '''# 4. Get Reward '''
    
        #        calculateQValues(red.qTable)
    """


    for i in numtrials:
        if i % 2 == 0:
            explore(redAgent)
        else:
            exploit(redAgent)




    end = timeit.timeit()

    printQTable()

# =========================
#if __name__== "__main__":
#    main()
#    pass
















#state numbers reflect computer e.g., first might be firewall active?
