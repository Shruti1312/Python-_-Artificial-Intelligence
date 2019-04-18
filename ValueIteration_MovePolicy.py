import os
import numpy as np
import operator

orientations = [(-1, 0),(1, 0), (0, 1), (0, -1)]

def rotate_left(action):
    if action == (-1,0):
        return (0, -1)
    elif action == (1, 0):
        return (0, 1)
    elif action == (0, 1):
        return (-1, 0)
    elif action == (0, -1):
        return (1, 0)
def rotate_right(action):
    if action == (-1,0):
        return (0, 1)
    elif action == (1,0):
        return (0, -1)
    elif action == (0, 1):
        return (1,0 )
    elif action == (0, -1):
        return (-1, 0)

def Min(orient, utilititities):
    action = orient[0];
    best_cost = utilititities( action )
    for a in orient:
        a_score = utilititities( a )
        if a_score < best_cost:
            action = a
            best_cost = a_score
    return action

def GetMax(actions, utlitity):
    return Min(actions, lambda x: -utlitity(x))


reward = {}
states = set()
goal_states = set()

def actions(state):
    if state in goal_states:
        return [None]
    else:
        return orientations

def Move(s, direction):
        nextstate = tuple(map(operator.add, s, direction))
        isStatevalid = nextstate in states
        if isStatevalid:
            return nextstate
        else:
            return s

def Transition(state, action):
    if action == None:
        return [(0.0, state)]
    else:
        return [(0.7, Move(state, action)),
                (0.1, Move(state, rotate_right(action))),
                (0.1, Move(state, rotate_left(action))),
                (0.1, Move(state, rotate_left(rotate_left(action))))]

def calculate_movepolicy(grid, goal, grideSize, epsilon = 0.01, gamma = 0.9):
    goal_states.add(goal)
    for x in range(grideSize):
            for y in range(grideSize):
                reward[x, y] = grid[x][y]
                states.add((x, y))

    Utility = dict([(s, 0) for s in states])
    while True:
        UCost = Utility.copy()
        diff = 0
        for s in states:
            Utility[s] = reward[s] + gamma * max([sum([p * UCost[s1] for (p, s1) in Transition(s, a)])
                                        for a in actions(s)])
            diff = max(diff, abs(Utility[s] - UCost[s]))
        if diff < epsilon * (1 - gamma) / gamma:
             break;
    policy = {}
    for s in states:
        policy[s] = GetMax(actions(s), lambda a :sum([p * UCost[s1] for (p, s1) in Transition(s, a)]))
    chars = {(1, 0):'Down', (0, 1):'Right', (-1, 0):'Up', (0, -1):'Left', None: '.'}
    matrix = [[0 for x in range(grideSize)] for y in range(grideSize)]
    for (s,a) in policy.items():
        i =  int(s[0])
        j = int(s[1])
        matrix[i][j] = chars[a]
    return matrix

#Entity representing the city area
class Speedracer:
    CitySize = 0
    NumberOfCarsOnRun = 0
    NumberOfObstacles = 0
    StartPositionsOfCars = []
    LocationsOfObstacles = []
    EndPositionsOfcars = []
    RoadMap = [[]]
    MovePolicy = [[]]

speedracerObj = Speedracer()

#Defining the city road map with obstacles, end positions, and start positions
def GetProblemInfo(filename):
    f = open(filename)
    lines = f.readlines()
    sizeOfGrid = int(lines[0])
    numberCars = int(lines[1])
    numberObstacles = int(lines[2])
    speedracerObj.CitySize = sizeOfGrid
    speedracerObj.NumberOfCarsOnRun = numberCars
    speedracerObj.NumberOfObstacles = numberObstacles

    i = 3
    while i < numberObstacles + 3:
        speedracerObj.LocationsOfObstacles.append(lines[i].rstrip())
        i = i + 1

    j = i
    while j < numberCars + i:
        speedracerObj.StartPositionsOfCars.append(lines[j].rstrip())
        j = j + 1

    w= j
    while w < numberCars + j:
        speedracerObj.EndPositionsOfcars.append(lines[w].rstrip())
        w = w + 1

def SetDestinationAndMovePolicy(position):
    sizeOfGrid = speedracerObj.CitySize
    matrix = [[0 for x in range(sizeOfGrid)] for y in range(sizeOfGrid)]
    for i in range(0, sizeOfGrid):
        for j in range(0, sizeOfGrid):
                matrix[i][j] = -1

    for obs in speedracerObj.LocationsOfObstacles:
        obstacleCordinates = obs.split(",")
        iObs = int(obstacleCordinates[0])
        jObs = int(obstacleCordinates[1])
        matrix[iObs][jObs] = matrix[iObs][jObs] + -100

    destinationPos = speedracerObj.EndPositionsOfcars[position]
    destCor = destinationPos.split(",")
    iendPos = int(destCor[0])
    jendPos = int(destCor[1])
    matrix[iendPos][jendPos] = 99

    speedracerObj.RoadMap = np.transpose(matrix)

    speedracerObj.MovePolicy = calculate_movepolicy(speedracerObj.RoadMap, (jendPos, iendPos), speedracerObj.CitySize)

def turn_left1(CurrMove):
    changedMove = ""
    if CurrMove == "Up":
        changedMove = "Left"
    elif CurrMove == "Down":
        changedMove = "Right"
    elif CurrMove == "Right":
        changedMove = "Up"
    elif CurrMove == "Left":
        changedMove = "Down"
    return changedMove

def turn_right1(CurrMove):
    changedMove = ""
    if CurrMove == "Up":
        changedMove = "Right"
    elif CurrMove == "Down":
        changedMove = "Left"
    elif CurrMove == "Right":
        changedMove = "Down"
    elif CurrMove == "Left":
        changedMove = "Up"
    return changedMove

def CalculateGoalCost(position):
    listCost = []
    for itr in range(10):
       value = 0
       currPos = (speedracerObj.StartPositionsOfCars[position]).split(",")
       currPosi = int(currPos[1])
       currPosj = int(currPos[0])
       endPos = (speedracerObj.EndPositionsOfcars[position]).split(",")
       endPosi = int(endPos[1])
       endPosj = int(endPos[0])
       np.random.seed(itr)
       swerve = np.random.random_sample(1000000)
       k = 0
       while not (currPosi == endPosi and currPosj == endPosj):
           move = speedracerObj.MovePolicy[currPosi][currPosj]
           swerveValue = swerve[k]
           if swerveValue > 0.7:
               if swerveValue > 0.8:
                   if swerveValue > 0.9:
                       move = turn_left1(turn_left1(move))
                   else:
                       move = turn_right1(move)
               else:
                   move = turn_left1(move)

           if move == "Left":
               if not ((currPosj - 1) < 0):
                   currPosj = currPosj - 1
           elif move == "Right":
               if not((currPosj + 1) > (speedracerObj.CitySize - 1)):
                   currPosj = currPosj + 1
           elif move == "Up":
               if not((currPosi - 1) < 0):
                   currPosi = currPosi - 1
           elif move == "Down":
              if not ((currPosi + 1) > (speedracerObj.CitySize - 1)):
                  currPosi = currPosi + 1

           value = value + int(speedracerObj.RoadMap[currPosi][currPosj])
           k = k + 1
       listCost.append(value)
    return int(np.floor(np.mean(listCost)))

if os.path.exists("output.txt"): os.remove("output.txt")
h = open("output.txt", "a")
if os.path.exists("input1.txt"):
   GetProblemInfo("input1" ".txt")
   for op in range(speedracerObj.NumberOfCarsOnRun):
          SetDestinationAndMovePolicy(op)
          v = str(CalculateGoalCost(op))
          h.write(v + "\n")
          reward.clear()
          states.clear()
          goal_states.clear()

