import math
import itertools
from itertools import permutations
import random

## (A) Lists all states #####################################################################################################################

def list_states():
    states = list(permutations('012345678', 9))             # getting all possiple states
    return states
    
states = list_states()
# for i in range(0,len(states)):                            # list all states 
#     print("State:", i+1, states[i])
print("(A) The 2nd state = ",states[1])                         # print the second state 
print("(A) Number of states = ",len(states))                    # How many states?


## (B) Get the resultant state of an action ( up:1, down:2, left:3, right:4) and a state as input ###########################################

def action_result(current_state, action):
    current_state = str(current_state)
    count =1
    for i in current_state:                             # calculate the indeces of the empty cell
        if i == '0':
            empty_row = math.ceil(count/3)
            empty_cols = count - ((empty_row-1)*3)
            empty_count = count
        count += 1

    output_state = ""
    if action == 1:                                     # 1: moving up
        if empty_row == 3:
            output_state = current_state
        else:
            for i in range(0,9):
                if i == (empty_count-1):
                    output_state += current_state[empty_count+2]
                elif i == (empty_count+2):
                    output_state += current_state[empty_count-1]
                else: output_state += current_state[i]

    elif action == 2:                                     # 2: down
        if empty_row == 1:
            output_state = current_state
        else:
            for i in range(0,9):
                if i == (empty_count-1):
                    output_state += current_state[empty_count-4]
                elif i == (empty_count-4):
                    output_state += current_state[empty_count-1]
                else: output_state += current_state[i]

    elif action == 3:                                     # 3: left
        if empty_cols == 3:
            output_state = current_state
        else:
            for i in range(0,9):
                if i == (empty_count-1):
                    output_state += current_state[empty_count]
                elif i == (empty_count):
                    output_state += current_state[empty_count-1]
                else: output_state += current_state[i]

    elif action == 4:                                     # 4: right
        if empty_cols == 1:
            output_state = current_state
        else:
            for i in range(0,9):
                if i == (empty_count-1):
                    output_state += current_state[empty_count-2]
                elif i == (empty_count-2):
                    output_state += current_state[empty_count-1]
                else: output_state += current_state[i]
    
    return output_state

input_state = '012345678'
action = 3 

#action_result('input_state', (moving up:1, down:2, left:3, right:4))
output_state = action_result(input_state, action)

print("(B) Output state for input state of [", input_state, "] and action [", action, "] is [",output_state, "]")


## (C) Random actions to reach the goal state of each row is divisible by 3  ################################################################

intial_state = input("enter intial state: ")

progress_state = intial_state
while True:
    random_action = random.randrange(1, 5)
    progress_state = action_result(progress_state, random_action)
    remain = ((int(progress_state[0])+int(progress_state[1])+int(progress_state[2]))%3) + ((int(progress_state[3])+int(progress_state[4])+int(progress_state[5]))%3) + ((int(progress_state[6])+int(progress_state[7])+int(progress_state[8]))%3)
    print("Action [", random_action, "], result state [", progress_state, "], division remaining= ", remain)
    if ((int(progress_state[0])+int(progress_state[1])+int(progress_state[2]))%3 ==0) and ((int(progress_state[3])+int(progress_state[4])+int(progress_state[5]))%3 ==0) and ((int(progress_state[6])+int(progress_state[7])+int(progress_state[8]))%3 ==0):
        print("(C) Goal achieved! The resultant state is [", progress_state, "]")
        break
    
## end of secion one ########################################################################################################################