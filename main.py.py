#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Breadth First Search Algorithm
# 8-puzzle problem


# Importing necessary libraries
import numpy as np
import sys
import copy
import os


# Function for getting user input 
def user_input():
    print("Welcome to the Puzzle!!!\n\n\nEnter number from 0-8 \n" )
    print("Input matrix example:")
    print("The digits here represents element in the input matrix")
    print("[ 1  2  3 ]\n[ 4  5  6 ]\n[ 7  8  9 ]\n\n")
    initial_state = np.zeros(9)
    for i in range(9):
        states = int(input("Enter the number for element  "+ str(i + 1)+ ":    "))
        if states < 0 or states > 8:
            print("You entered wrong input. Please enter values between 0 and 8.")
            sys.exit("Please Start Again!!!!!")
        else:
            initial_state[i] = np.array(states)
    return np.reshape(initial_state, (3, 3))


# Function for checking the user data for repeated element numbers 
def check_repeated(l): 
    array = np.reshape(l, 9)
    # Checking fof the repeated entries in each element
    for i in range(9):
        counter_appear = 0
        f = array[i]
        for j in range(9):
            if f == array[j]:
                counter_appear += 1
        if counter_appear >= 2:
            print("The entered input is Invalid, same number is entered more than one time")
            sys.exit("Please Start Again!!!!!!!")


# Function for checking if the user input matrix is solvable
def check_solvable(g):
    arr = np.reshape(g, 9)
    cntr_s = 0
    for i in range(9):
        if not arr[i] == 0:
            chk_e = arr[i]
            for x in range(i + 1, 9):
                if chk_e < arr[x] or arr[x] == 0:
                    continue
                else:
                    cntr_s += 1
    if cntr_s % 2 == 0:
        print("The puzzle can be solved...... \n\nGnerating path.....")
    else:
        print("\n Generating nodes......")

        
# Creating a class "Node" to call all the objects required for puzzle solving        
class Node: 
    def __init__(self, node_no, data, parent, act, cost): 
        # Stote the data
        self.data = data
        # Work with the parent node
        self.parent = parent
        self.act = act
        self.node_no = node_no
        self.cost = cost

        
# Calculating the location of the blank tile in the 3 by 3 matrix and returns the output as a pair, (i,j)
# Function for finding the position of blank / 0 in the matrix.
def find_zero(puzzle): 
    # storing the elemnt position in i and j
    i, j = np.where(puzzle == 0)
    i = int(i)
    j = int(j)
    return i, j


# Function to move the blank tile(0) to the left if possible.
def move_left(data):
    i, j = find_zero(data)
    if j == 0:
        return None
    else:        
        new_arr = np.copy(data)
        # Creating a array to temporarily store the modified data
        tmp = new_arr[i, j - 1]
        new_arr[i, j] = tmp
        # Moving the element 0
        new_arr[i, j - 1] = 0
        return new_arr


# Function to move the blank tile(0) to the right if possible.
def move_right(data):
    i, j = find_zero(data)
    if j == 2:
        return None
    else:
        new_arr = np.copy(data)
        # Creating a array to temporarily store the modified data
        tmp = new_arr[i, j + 1]
        new_arr[i, j] = tmp
        # Moving the element 0
        new_arr[i, j + 1] = 0
        return new_arr


# Function to move the blank tile(0) up if possible.
def move_up(data):
    i, j = find_zero(data)
    if i == 0:
        return None
    else:
        new_arr = np.copy(data)
        # Creating a array to temporarily store the modified data
        tmp = new_arr[i - 1, j]
        new_arr[i, j] = tmp
        # Moving the element 0
        new_arr[i - 1, j] = 0
        return new_arr


# Function to move the blank tile(0) down if possible.
def move_down(data):
    i, j = find_zero(data)
    if i == 2:
        return None
    else:
        new_arr = np.copy(data)
        # Creating a array to temporarily store the modified data
        tmp = new_arr[i + 1, j]
        new_arr[i, j] = tmp
        # Moving the element 0
        new_arr[i + 1, j] = 0
        return new_arr


# Function to move the blank tile.
def move_tile(action, data):
    # checking for the movement of element 0(blank tile)
    # move up
    if action == 'up':
        return move_up(data)
    # move down
    if action == 'down':
        return move_down(data)
    # move left
    if action == 'left':
        return move_left(data)
    # move right
    if action == 'right':
        return move_right(data)
    else:
        return None


# FUnction to show selected node as output in list_file
def print_position(lst_final):  
    print("\n Printing final solution...")
    for l in lst_final:
        print("\n Moving : " + str(l.act) + "\n" + "Resulting Matrix : " + "\n" + str(l.data) + "\t" + "node number:" + str(l.node_no))
        

# Function to write the nodes in nodePath.txt file 
def add_path(lst_final):
    # check if the file to be generated already exists
    if os.path.exists("nodePath.txt"):
        # Delete the exixing file
        os.remove("nodePath.txt")
    # Open the file nodePath.txt to write the path they are discovered
    f = open("nodePath.txt", "a")
    for k in lst_final:
        for g in range(len(k.data)):
            for h in range(len(k.data)):
                # Writing data to the file
                q=str(k.data[h][g])
                e=float(q)
                f.write(f'{int(e)} ')
        # Write to the file
        f.write("\n")  
    # Close the file 
    f.close()


# Function to add the information of visited nodes in NodeInfo.txt file
def add_node_info(visitd):  
    # Check if the file already exists
    if os.path.exists("NodesInfo.txt"):
        # Remove the file
        os.remove("NodesInfo.txt")
    # Open the file NodesInfo.txt to write the path they are discovered
    f = open("NodesInfo.txt", "a")
    for n in visitd:
        # Check if the node has a parent node 
        if n.parent is not None:
            # Writing in the format [Node Index, Parent Node, Cost]
            f.write(str(n.node_no) + " " + str(n.parent.node_no) + "\t" + str(n.cost) + "\n")
    # Close the file
    f.close()

    
# Function to add the explored nodes to Nodes.txt file
def add_node_explored(explored):
    # Check if the file already exists
    if os.path.exists("Nodes.txt"):
        # Remove the file
        os.remove("Nodes.txt")
    # Open the file Nodes.txt to write the path they are discovered
    f = open("Nodes.txt", "a")
    for element in explored:
        for i in range(len(element)):
            for j in range(len(element)):
                # Writing data in the file
                z=str(element[j][i])
                u=float(z)
                f.write(f'{int(u)} ')        
        f.write("\n")
    # Close the file
    f.close()

    
# Function to track the path from the Goal Node to the Starting Node (Back Tracking)
def path(node): 
    # Create empty list to add the back tracked path 
    b = [] 
    # Add node to the list
    b.append(node)
    parent_node = node.parent 
    # If it has a parent node ass the node to the file
    while parent_node is not None:
        b.append(parent_node)
        # Continuing to look for parent nodes in reverse order
        parent_node = parent_node.parent
    return list(reversed(b))  


# Function to execute the above defined functions and find the nodes 
def explore_nodes(node):
    print("\nExploring Nodes........")
    # Checking for the action to be performed
    actions = ["down", "up", "left", "right"]
    # Calling the final Node to be reached
    goal_node = final_goal
    node_q = [node]
    # Storing final nodes 
    fnl_nodes = []
    # Storing the nodes that have been visited
    visitd = []
    # Adding the data of nodes
    fnl_nodes.append(node_q[0].data.tolist())
    # Defining a unique ID to nodes formed
    node_cntr = 0

    while node_q:
        # Assigning the Object in node_q to the current_rt
        current_rt = node_q.pop(0)  
        # Using current_rt to check the progress 
        if current_rt.data.tolist() == goal_node.tolist(): 
            # Printing output
            print("\nGoal reached")
            return current_rt, fnl_nodes, visitd

        for move in actions:
            # Storing the data of the movement of tiles
            temp_data = move_tile(move, current_rt.data)
            if temp_data is not None:
                node_cntr += 1
                # Create child node to access data and manipulate it 
                child_node = Node(node_cntr, np.array(temp_data), current_rt, move, 0) 
                # Add the child node data in final node list
                if child_node.data.tolist() not in fnl_nodes:  
                    # Adding the child node to node_q to keep the process running
                    node_q.append(child_node)
                    fnl_nodes.append(child_node.data.tolist())
                    # Adding child node to the visited list
                    visitd.append(child_node)
                    # Checking if the goal node is reached
                    if child_node.data.tolist() == goal_node.tolist():
                        print("\nGoal_reached") 
                        return child_node, fnl_nodes, visitd
    # Output none if chld node not reached
    return None, None, None 



# Execute

print("Welcome to the Project 1 - 8-Puzzle Board ")
test_input = input("Enter '1' to run the code for TEST CASE 1!! \nEnter '2' to run the code for TEST CASE 2!! \nEnter '0' to input the Start State manually!! \n")
#test_input = int(test_input)
if test_input == '1':
    initial_state = inp = np.array([[1, 6, 7], [2, 0, 5], [4, 3, 8]])
    final_goal = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])
elif test_input == '2':
    initial_state = inp = np.array([[4, 7, 8], [2, 1, 5], [3, 6, 0]])
    final_goal = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])
elif test_input == '0':
        # Taking input from the user
    inp = user_input()

    print("\nThe final goal State: \n",final_goal,"\n\n")

        # Checking for the repeated elements in the user input matrix
    check_repeated(inp)

        # Checking for the soluability of the matrix
    check_solvable(inp)
    final_goal = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])
else:
    sys.exit("Invalid Input, Please Start Again!!!!!")
        

# Adding the user input matrix to the code to find the path
root = Node(0, inp, None, None, 0)
goal, s, v = explore_nodes(root)


if goal is None and s is None and v is None:
    print("Goal State could not be reached, Sorry")
else:
    # Printing the path to the output terminal
    print_position(path(goal))
    
    # Writing data to nodePath.txt file
    add_path(path(goal))
    
    # Writing data to Nodes.tst file
    add_node_explored(s)
    
    # Writing data to NodesInfo.txt file
    add_node_info(v)


# In[ ]:




