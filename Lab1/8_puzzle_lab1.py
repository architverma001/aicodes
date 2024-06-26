
goal_state = [[5,1,4],[0,3,2],[7,6,8]]  # 0 is blank 
initial_state = [[1,3,4],[5,2,0],[7,6,8]]


from copy import deepcopy
class environment:
  class Node:
    # parent is state from which came
    # state is current state in which the node is in
    # cost is path cost used spend in reaching that node
    # visited array is used to store path taken 
      def __init__(self, parent = None, state = None ,cost = 0, visited=[]): 
          self.cost = cost
          self.parent = parent
          self.state = state
          self.visited = [*visited]
    
      def goal_test(self):

          if (self.state == goal_state):
              return True
          else:
              return False

      def validate(self, i, j):
          if(i>=0 and i<=2 and j>=0 and j<=2):
              return True
          else:
              return False

      def __lt__(self, other):
          return self.cost < other.cost

      def successor(self):
          current_state = self.state
          x,y = 0,0

          final_states = []

          for i in range(len(goal_state)):
              for j in range(len(goal_state[i])):
                  if current_state[i][j] == 0:
                      x = i
                      y = j
                      break
          
          a = [0,0,1,-1]
          b = [1,-1,0,0]

          for i in range(4):
              if (self.validate(x+a[i],y+b[i])):
                  new_state = deepcopy(current_state)
                  new_state[x][y] = new_state[x+a[i]][y+b[i]]
                  new_state[x+a[i]][y+b[i]] = 0

                  final_states.append(new_state)

          return final_states

from collections import defaultdict
from queue import PriorityQueue
import heapq

inital_state = [[1,3,4],[5,2,0],[7,6,8]]
explored = defaultdict(tuple)
frontier = PriorityQueue()

root_node = environment.Node(state=inital_state,)
frontier.put((root_node.cost, root_node))



def check_frontier(state, current_node):
    f = 0
    for i in frontier.queue:
        if(i[1].state == state):
            if(i[1].cost > current_node.cost +1):
                i[1].cost = current_node.cost+1
                i[1].parent = current_node     
            
            return True

    return False


def depth_d(d):

    depth = d
    depth_states = []

    while not frontier.empty():
        current_node = frontier.get()[1]

        if(len(current_node.visited) == depth):
            depth_states.append(current_node.state)
            continue

        if(environment.Node.goal_test(current_node)):
            break

        else:
            explored[   tuple(map(tuple, current_node.state))   ] = 1   # making 1 for visited   
            possible_states = environment.Node.successor(current_node)
            
            for i in possible_states:
                if (explored[ tuple(map(tuple, i))  ] == 1):
                    continue
                
                else:
                    if (check_frontier(i,current_node)):
                        continue            
                    else:
                        new_node = environment.Node(parent=current_node, state=i, cost=current_node.cost+1,visited =  [*current_node.visited]+[current_node])
                    frontier.put((new_node.cost, new_node))



    for i in depth_states:
        for j in i:
            print(j)
        print()
        print()



if __name__ == '__main__':
    depth_d(4)