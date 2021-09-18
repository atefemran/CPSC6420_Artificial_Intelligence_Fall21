
#######################################################################################################################################################################

################################################### Finding Optimal Path to a reward using Markov Decision Process ####################################################
###### For more details about the code and how to use it visit my git: https://github.com/atefemran/CPSC6420_Artificial_Intelligence_Fall21 | Atef Emran @ 2021 #######

#######################################################################################################################################################################

import copy

## state defintion class 
class State:    
    def __init__(self, state, blocked, value, reward, optimal_policy, optimal_s_prime):
        self.state = state     # x & y are the grid location, and d is the direction the robot is facing (1: up, 2: down, 3: left, and 4
        self.x = state[0]
        self.y = state[1]
        self.d = state[2]
        self.blocked = blocked
        self.value = value
        self.reward = reward
        self.optimal_policy = optimal_policy
        self.optimal_s_prime = optimal_s_prime

## Generates the map states | Input: x:grid width, y:grid hieght, d:number of possible directions, intial reward | Return: states list ################################
def states_generator(x,y,d, blocked_cells, initial_value, goal_cell, goal_reward, gameover_cell, gameover_penalty): 
    states_list = []
    for x in range(1,x+1):
        for y in range(1,y+1):
            for d in range(1,d+1):        
                # chack if any of these cells is blocked
                block_flag = 0
                for blocked in blocked_cells:
                    if (x == blocked[0]) and (y == blocked[1]):
                        block_flag = 1

                # Generate a new state and add it to the list
                if ((x == goal_cell[0]) and (y == goal_cell[1])):               # is it a goal cell?
                    generated_state = State([x,y,d], block_flag, 0, goal_reward, 0, 0)
                elif ((x == gameover_cell[0]) and (y == gameover_cell[1])):     # is it a gamover cell?
                    generated_state = State([x,y,d], block_flag, 0, gameover_penalty, 0, 0)
                else: 
                    generated_state = State([x,y,d], block_flag, 0, initial_value, 0, 0)
                states_list.append(generated_state)
    
    return states_list

## For a given state, action returns the new possible states | Input: input state, required action, all states list | Return: the new state, its cost ##################
def move(state, action, states_list):   
    # possiple actions are
    # A1: one cell in same direction facing. Cost: 1.5 | A2: two cells in same direction facing. Cost: 2 | 
    # A3: Turn left, stay in the same cell. Cost: 0.5
    # A4: Turn right, stay in the same cell. Cost: 0.5

    # A1: move one cell forward
    if action == "A1":
        cost = 1.5
        
        # Excuting the action
        if state.d == 1:            # facing up 
            x = state.x
            y = state.y + 1
            d = state.d
            for state_in_list in states_list:
                if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                    if state_in_list.blocked == 1:
                        state_prime = None
                    else:
                        state_prime = state_in_list
                    break
                else:
                    state_prime = None
        
        elif state.d == 2:          # facing down
            x = state.x
            y = state.y -1
            d = state.d
            for state_in_list in states_list:
                if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                    if state_in_list.blocked == 1:
                        state_prime = None
                    else:
                        state_prime = state_in_list
                    break
                else:
                    state_prime = None
        
        elif state.d == 3:          # facing left
            x = state.x - 1
            y = state.y
            d = state.d
            for state_in_list in states_list:
                if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                    if state_in_list.blocked == 1:
                        state_prime = None
                    else:
                        state_prime = state_in_list
                    break
                else:
                    state_prime = None
        
        elif state.d == 4:          # facing right
            x = state.x + 1
            y = state.y
            d = state.d
            for state_in_list in states_list:
                if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                    if state_in_list.blocked == 1:
                        state_prime = None
                    else:
                        state_prime = state_in_list
                    break
                else:
                    state_prime = None

    # A2: move two cells forward
    elif action == "A2":
        cost = 2
        
        # Excuting the action
        if state.d == 1:            # facing up 
            x = state.x
            y = state.y + 2
            d = state.d
            for state_in_list in states_list:
                if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                    if state_in_list.blocked == 1:
                        state_prime = None
                    else:
                        state_prime = state_in_list
                    break
                else:
                    state_prime = None
        
        elif state.d == 2:          # facing down
            x = state.x
            y = state.y - 2
            d = state.d
            for state_in_list in states_list:
                if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                    if state_in_list.blocked == 1:
                        state_prime = None
                    else:
                        state_prime = state_in_list
                    break
                else:
                    state_prime = None
        
        elif state.d == 3:          # facing left
            x = state.x - 2
            y = state.y
            d = state.d
            for state_in_list in states_list:
                if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                    if state_in_list.blocked == 1:
                        state_prime = None
                    else:
                        state_prime = state_in_list
                    break
                else:
                    state_prime = None
        
        elif state.d == 4:          # facing right
            x = state.x + 2
            y = state.y
            d = state.d
            for state_in_list in states_list:
                if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                    if state_in_list.blocked == 1:
                        state_prime = None
                    else:
                        state_prime = state_in_list
                    break
                else:
                    state_prime = None

    # A3: move left in the same cell
    elif action == "A3":
        cost = 0.5
        
        x = state.x
        y = state.y 
        
        if state.d == 1:
            d = 3
        elif state.d == 2:
            d = 4
        elif state.d == 3:
            d = 2
        elif state.d == 4:
            d = 1
        
        for state_in_list in states_list:
            if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                state_prime = state_in_list
                break
            else:
                state_prime = None
    
    # A4: move right in the same cell
    elif action == "A4":
        cost = 0.5
        
        x = state.x
        y = state.y 
        
        if state.d == 1:
            d = 4
        elif state.d == 2:
            d = 3
        elif state.d == 3:
            d = 1
        elif state.d == 4:
            d = 2

        for state_in_list in states_list:
            if (state_in_list.x) == x and (state_in_list.y == y) and (state_in_list.d ==d):
                state_prime = state_in_list
                break
            else:
                state_prime = None

    # checking the possibility of the new state (state prime) 
    if state_prime == None:
        state_prime = state         # stay in the same cell 
        cost = 0    
    else:                           # is getting to the new state will required passing a barrier
        for barrier in barriers_list:
            if barrier[0] == "row":
                if state_prime.y == barrier[1]:
                    if ((state_prime.x > barrier[2]) and (state.x <= barrier[2])) or ((state_prime.x >= barrier[3]) and (state.x < barrier[3])):
                            state_prime = state
                            cost = 0
                    elif ((state_prime.x < barrier[2]) and (state.x >= barrier[2])) or ((state_prime.x <= barrier[3]) and (state.x > barrier[3])):
                            state_prime = state
                            cost = 0
            if barrier[0] == "col":
                if state_prime.x == barrier[1]:
                    if ((state_prime.y > barrier[2]) and (state.y <= barrier[2])) or ((state_prime.y >= barrier[3]) and (state.y < barrier[3])):
                        state_prime = state
                        cost = 0
                    elif ((state_prime.y < barrier[2]) and (state.y >= barrier[2])) or ((state_prime.y <= barrier[3]) and (state.y > barrier[3])):
                        state_prime = state
                        cost = 0
        if (state_prime != state) and (action == "A2"):                 ## passing through a blocked cell 
            for blocked in states_list:         
                if blocked.blocked == 1:                                ## for each blocked cell 
                    if state.y == blocked.y == state_prime.y:           ## the two states and the blocked cell are at the same col
                        if (state.x < blocked.x < state_prime.x) or (state.x > blocked.x > state_prime.x):
                            state_prime = state
                            cost = 0
                            
                    elif state.x == blocked.x == state_prime.x:         ## the two states and the blocked cell are at the same raw
                        if (state.y < blocked.y < state_prime.y) or (state.y > blocked.y > state_prime.y):
                            state_prime = state
                            cost = 0
    
    return state_prime, cost

## For a given state, what is the best policy | Input: input state, all states list, noise, discount factor | Return: max value, optimal policy, optimal state prime ##
def max_value(state, states_list, noise, gamma):           
    
    # the possible actions and thier associated cost
    possible_actions = []
    possible_s_prime = []
    possible_s_prime_cost = []
    for A in possible_directions:
        state_prime, cost = move(state, A, states_list)
        if cost != 0:       # didn't move
            # print(state_prime.state)
            possible_s_prime.append(state_prime)
            possible_s_prime_cost.append(cost)
            possible_actions.append(A)
    
    number_of_unexpected_actions = (len(possible_s_prime)) -1

    ## calculating the values list
    values_list = []
    for state_prime, cost in zip(possible_s_prime, possible_s_prime_cost):
       
        new_value = (1-noise)*((-cost) + (gamma * state_prime.value))   ## intial new value for this state
        
        # generating unexpected action and thier cost list for the state prime and the action
        unexpected_states_list = []
        unexpected_costs_list = []
        for unexpected, unexpected_cost in zip(possible_s_prime, possible_s_prime_cost):
            if unexpected == state_prime:
                continue
            else:
                unexpected_states_list.append(unexpected)
                unexpected_costs_list.append(unexpected_cost)
        for unexpected, unexpected_cost in zip(unexpected_states_list, unexpected_costs_list):
            new_value += (noise/number_of_unexpected_actions)*((-unexpected_cost) + (gamma * unexpected.value))

        # adding the the new value for the state prime and the action
        values_list.append(new_value)

    ## the max value for this state 
    max_value = -9999999999
    optimal_policy = ""
    optimal_s_prime = ""
    for value, action, s_prime in zip(values_list, possible_actions, possible_s_prime):
        if value > max_value:
            max_value = value
            optimal_policy = action
            optimal_s_prime = s_prime
            
    return max_value, optimal_policy, optimal_s_prime

## Updates all the states in the map | Input: all states list, goal, gameover cells, reward, penality, noise, gamma | Return: input states list, updated states list ##
def states_values_update(new_states_list, goal_cell, goal_reward, gameover_cell, gameover_penalty, noise, gamma):
    previous_state_list = []
    previous_state_list = new_states_list[:]
    new_states_list = []
    i =0
    for state in previous_state_list:
        # don't update the goal, gameover, or the blocked cells
        if state.blocked == 1:
            new_states_list.append(copy.deepcopy(state))
            continue
        elif (state.x == goal_cell[0]) and (state.y == goal_cell[1]):
            state.value = goal_reward
            new_states_list.append(copy.deepcopy(state))
            continue
        elif  (state.x == gameover_cell[0]) and (state.y == gameover_cell[1]):
            state.value = gameover_penalty
            new_states_list.append(copy.deepcopy(state))
            continue
        
        new_states_list.append(copy.deepcopy(state))
        new_states_list[-1].value, new_states_list[-1].optimal_policy, new_states_list[-1].optimal_s_prime = max_value(state, previous_state_list, noise, gamma)

        i+=1

    return previous_state_list, new_states_list

##  Finds the max value difference between any state in the previous and the updated states | Input: previous, current states list | Return: max value difference #####
def value_difference(previous_states_list, states_list):

    max_difference = 0
    for previous, state in zip(previous_states_list, states_list):
        # print(abs(previous.value -state.value))
        
        if (abs(previous.value -state.value)) > max_difference:
            max_difference = abs(state.value - previous.value)
    
    return max_difference

##  Runs the code and prints out the iterations and the optimal path | Input: start state, noise, discount factor | Return: print iterations results and optimal path #
def iterations_output_path(start_state, noise, gamma):          
    # getting the first state
    previous_states_list = states_list
    previous_states_list, new_states_list = states_values_update(states_list, goal_cell, goal_reward, gameover_cell, gameover_penalty, noise, gamma)
    max_diff = value_difference(previous_states_list, new_states_list)

    counter = 1

    print("iter ", counter)
    for state in new_states_list:
        if (state.blocked == 0):
            if ((state.x == goal_cell[0]) and (state.y == goal_cell[1])):
                print("state ", state.state, "V = ", round(state.value,2), "\t Best Action: ", "N/A", "\t Optimal State: ", state.state)
            elif ((state.x == gameover_cell[0]) and (state.y == gameover_cell[1])):
                print("state ", state.state, "V = ", round(state.value,2), "\t Best Action: ", "N/A", "\t Optimal State: ", state.state)
            else: 
                print("state ", state.state, "V = ", round(state.value,2), "\t Best Action: ", state.optimal_policy, "\t Optimal State: ", state.optimal_s_prime.state)
    print("--------------------------------------------------")

    while (max_diff > 0.01):
        previous_states_list, new_states_list = states_values_update(new_states_list, goal_cell, goal_reward, gameover_cell, gameover_penalty, noise, gamma)
        max_diff = value_difference(previous_states_list, new_states_list)

        counter += 1

        ## prining the first 10 iterations and the last iteration
        if (counter <= 10) or (max_diff <= 0.01):
            print("iter ", counter)
            for state in new_states_list:
                if (state.blocked == 0):
                    if ((state.x == goal_cell[0]) and (state.y == goal_cell[1])):
                        print("state ", state.state, "V = ", round(state.value,2), "\t Best Action: ", "N/A")
                    elif ((state.x == gameover_cell[0]) and (state.y == gameover_cell[1])):
                        print("state ", state.state, "V = ", round(state.value,2), "\t Best Action: ", "N/A")
                    else: 
                        print("state ", state.state, "V = ", round(state.value,2), "\t Best Action: ", state.optimal_policy, "\t Optimal State: ", state.state)
            print("--------------------------------------------------")

    ## prinitng the optimal path
    # finding the first state object
    for state in new_states_list:
        if state.state == start_state:
            start_state = state
            break
    # building the path
    state = start_state
    print("\t \t The Optimal Path \t")
    print(" Discount factor (gamma) = ", gamma, ", noise = ", noise)
    print("--------------------------------------------------")
    while True:
        if state.optimal_policy == "A1":
            action_output = "One cells ahead ↑" 
        elif state.optimal_policy == "A2":
            action_output = "Two cells ahead ⇈"
        elif state.optimal_policy == "A3":
            action_output = "Turn left ←"
        elif state.optimal_policy == "A4":
            action_output = "Turn right →"
        print(state.state, action_output)
        
        if state.optimal_s_prime == 0:
            print("Can't reach a goal")
            break

        if (state.optimal_s_prime.x == goal_cell[0]) and (state.optimal_s_prime.y == goal_cell[1]):
            print(state.state, "Goal Cell!")
            break

        state = state.optimal_s_prime
    print("--------------------------------------------------")

## Global Variables ###################################################################################################################################################

global grid_width
global grid_height
global possible_directions
global blocked_cells                    
global barriers_list

## Initializing the map  #############################################################################################################################################

grid_width = 5
grid_height = 5
possible_directions = ["A1", "A2", "A3", "A4"]          # direction the robot is facing (1: up, 2: down, 3: left, and 4
blocked_cells = [[2,2], [3,2], [2,3]]                   # blocked cels 
goal_cell = [5,5]                                       # x,y coordinates of the goal cell 
goal_reward = 100                                  
gameover_cell = [4,4]                                   # x,y coordinates of the gameover cell 
gameover_penalty = -1000
states_list = states_generator(grid_width,grid_height,len(possible_directions), blocked_cells, 0, goal_cell, goal_reward, gameover_cell, gameover_penalty) 
barriers_list = [["row", 5, 2, 3], ["col", 5, 3, 4]]    # [(1)"barrier along a row or col", (2) row or col number, (3)(4) the two cells splitted by the barrier]                                      

#####################################################################################################################################################################

def main():
    
    ## Case (B), (C)    : Gamma = 1, no noise       ##########
    ## Case (D)         : Gamma = 0.8, no noise     ##########
    ## Case (E)         : Gamma = 0.2. no noise     ##########
    ## Case (F)         : Gamma = 0.9, noise = 0.2  ##########

    gamma = 0.9
    noise = 0.2
    start_state = [1,1,4]
    iterations_output_path(start_state, noise, gamma)

if __name__ == "__main__":
    main()
