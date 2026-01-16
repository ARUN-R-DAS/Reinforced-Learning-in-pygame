# The environment (no learning yet)

import random

GRID_SIZE = 5
ACTIONS = 4 #up,down,left,right

# hyperparameters
learning_rate = 0.1
gamma = 0.9
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01

# q-table
Q = {}

def reset():
    agent = [0,0]
    goal = [random.randint(0, GRID_SIZE-1),
            random.randint(0, GRID_SIZE-1)]
    return agent,goal

def step(agent, action):
    if action == 0: #up
        agent[1] -= 1
    elif action == 1: #down
        agent[1] += 1
    elif action == 2: #left
        agent[0] -= 1
    elif action == 3: #right
        agent[0] += 1

    # keep inside grid
    agent[0] = max(0, min(GRID_SIZE-1, agent[0]))
    agent[1] = max(0, min(GRID_SIZE-1, agent[1]))

    return agent

def get_q(state,action):
    return Q.get((state[0],state[1],action),0)

def best_action(state):
    values = [get_q(state,a) for a in range(ACTIONS)]
    return values.index(max(values))

EPISODES = 500

for episode in range(EPISODES):
    agent, goal = reset()
    steps = 0
    done = False

    while not done and steps < 50:
        steps += 1
        state = agent.copy()

        # choose action (explore vs exploit)
        if random.random() < epsilon:
            action = random.randint(0, ACTIONS-1)
        else:
            action = best_action(state)
        
        agent = step(agent, action)
        reward = -1
        if agent == goal:
            reward = 10
            done = True

        next_state = agent.copy()

        old_q = get_q(state, action)
        next_max = max(get_q(next_state, a) for a in range(ACTIONS))

        # Q-learning update
        new_q = old_q + learning_rate * (reward + gamma * next_max - old_q)
        Q[(state[0], state[1], action)] = new_q

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

    if episode % 50 == 0:
        print(f"Episode {episode} | Steps: {steps} | Epsilon: {epsilon:.2f}")