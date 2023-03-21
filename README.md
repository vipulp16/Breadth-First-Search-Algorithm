*** Breadth First Search Algorithm ***
--- 8- Puzzle Problem ---

ENPM 661 Project 1 

\# To execute the program,run the file named \'main.py\' using python IDE. (The code was initially written in Jupyter Notebook)

\# Check for the necessary libraries required to successfully execute the program:

 - Numpy : Used to perform operations on array(matrix) like adding elements, modifying elements in the matrix, looking of a particular element in the matrix, etc.

 - Copy : Used to copy the array

 - OS : Used to work with the entries in the .txt file generated

 - SYS : Used to exit the program for invalid input

\# As the code promts, Enter :  
- \'1\' to run the code using start and goal state from TEST CASE 1.  
    --initial_state = ([[1, 6, 7],[2, 0, 5], [4, 3, 8]]) 
    --final_goal = ([[1, 4, 7], [2, 5, 8], [3, 0, 6]])

- \'2\' to run the code using start and goal state from TEST CASE 2.  
    --initial_state = ([[4, 7, 8], [2, 1, 5], [3, 6, 0]]) 
    --final_goal = ([[1, 4, 7], [2, 5, 8], [3, 0, 6]])

- \'0\' to run the code to allow the user input the start state and taking 
    --initial_state = Input from user
    --Goal State as [[1, 4, 7], [2, 5, 8], [3, 6, 0]].

\* Explaining the Output:
 - The result is displayed in the output terminal with all the steps taken to achieve it.
 - 'Nodes.txt' file will be generated in the working directory containing all the nodes explored.
 - 'nodepath.txt' file will be generated in the working directory containing all the states of the puzzles.
 - ''NodesInfo.txt' file will be generated in the working directory containing the information of possible nodes explored. 
