# 1- Solving 8Puzzle using BFS DFS and UCS
## Problem Statement
In this project, the purpose is solving an 8-Puzzle Game using different search algorithms. The algorithms used are [1] Breadth First Search (BFS), [2] Depth First Search (DFS), and [3] Uniform Cost Search (UCS).

imageeeeeeeeee

learn more about the different algorithms:
imageeeeeeeeee
- [Breadth First Search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Depth First Search (DFS)](https://en.wikipedia.org/wiki/Depth-first_search)
- [Uniform Cost Search (UCS)](https://www.educative.io/edpresso/what-is-uniform-cost-search)

## Program / Code Summary
The program receives the user input of `InitialState`, `GoalState`, and `SearchMethod`, based on the input the corresponding algorithm function is provoked which then uses the `action_result` function and `State` class to output the generated path from the chosen algorithm along with the number of states visited by the algorithm to reach this path.

## Example
User Input:
`InitialState = '867013254'      # the intial state of the puzzle from top left to bottom right
GoalState = '123804765'         # the goal state of the puzzle from top left to bottom right
SearchMethod = 'ucs'            # "bfs", "dfs", or "ucs" `

The output:
`Reached the goal! Number of iteration = 53590 , size of closed states: 13178
Depth / Number of actions =  21
Actions and States are:  [['867013254'], ['Down', '067813254'], ['Left', '607813254'], ['Left', '670813254'], ['Up', '673810254'], ['Up', '673814250'], ['Right',
'673814205'], ['Right', '673814025'], ['Down', '673014825'], ['Down', '073614825'], ['Left', '703614825'], ['Up', '713604825'], ['Up', '713624805'], ['Right', '713624085'], ['Down', '713024685'], ['Down', '013724685'], ['Left', '103724685'], ['Up', '123704685'], ['Up', '123784605'], ['Right', '123784065'], ['Down', '123084765'], ['Left', '123804765']]`
