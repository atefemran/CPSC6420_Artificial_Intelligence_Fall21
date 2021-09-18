# 2- Markov Decision Process (MDP): Finding Optimal Path
## Problem Statement
The purpose is finding the optimal path for a robot in a given map with a goal cell reward and game-over cell penalty. The case study map is below. The code receives the map parameters, goal and penalty data, and the initial state, the noise [0:1], and the discount factor [0:1], and returns the value and policy iterations results along with the optimal path (which maximizes the value) from the start state.

![Map Example](https://raw.githubusercontent.com/atefemran/CPSC6420_Artificial_Intelligence_Fall21/main/1-Solving_8Puzzle_BFS_DFS_and_UCS/images/8_puzzle.png)

Note: You can create different maps by changing the map parameters in the `Initializing the map` section in the code. For example: the map shown above has the below parameters: /
`grid_width = 5`
`grid_height = 5`
`possible_directions = ["A1", "A2", "A3", "A4"]`          # direction the robot is facing (1: up, 2: down, 3: left, and 4
`blocked_cells = [[2,2], [3,2], [2,3]]`                   # blocked cels
`goal_cell = [5,5]`                                       # x,y coordinates of the goal cell
`goal_reward = 100`                                  
`gameover_cell = [4,4]`                                   # x,y coordinates of the game-over cell
`gameover_penalty = -1000`
`barriers_list = [["row", 5, 2, 3], ["col", 5, 3, 4]]`    # [(1)"barrier along a row or col", (2) row or col number, (3)(4) the two cells splitted by the barrier]                                      

Note that using these parameters, the robot states are defined with location and orientation [X-Location, Y-Location, Orientation].

## Program / Code Summary
The program receives the input to build the map along with the MDP parameters, then finds the optimal route from the indicated start cell to the goal cell with the highest reward. High level of the code and how it works is in the below code structure diagram.

![Code structure](https://raw.githubusercontent.com/atefemran/CPSC6420_Artificial_Intelligence_Fall21/main/1-Solving_8Puzzle_BFS_DFS_and_UCS/images/8_puzzle.png)


## Examples

![Examples](https://raw.githubusercontent.com/atefemran/CPSC6420_Artificial_Intelligence_Fall21/main/1-Solving_8Puzzle_BFS_DFS_and_UCS/images/8_puzzle.png)

Note the change in the optimal route when the noise value was increased as the value for state (4,3,1) is significantly lower when the noise was introduced because there is a probability now of landing in the game-over cell (moving one cell ahead instead of 2 cells). That's why the robot took a longer route to avoid this high penalty probability.

### Sample output
`--------------------------------------------------
                 The Optimal Path
 Discount factor (gamma) =  0.9 , noise =  0.2
--------------------------------------------------
[1, 1, 4] Two cells ahead ⇈
[3, 1, 4] Two cells ahead ⇈
[5, 1, 4] Turn left ←
[5, 1, 1] Two cells ahead ⇈
[5, 3, 1] Turn left ←
[5, 3, 3] Two cells ahead ⇈
[3, 3, 3] Turn right →
[3, 3, 1] Two cells ahead ⇈
[3, 5, 1] Turn right →
[3, 5, 4] Two cells ahead ⇈
[3, 5, 4] Goal Cell!
--------------------------------------------------`
