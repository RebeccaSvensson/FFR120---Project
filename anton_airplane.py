import matplotlib as mpl
from matplotlib import pyplot
import numpy as np

class Plane_map:
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np

    def __init__(self):
        self.grid = []
        self.x_length = 9
        self.y_length = 58
        
        self.body =  np.zeros((self.x_length,self.y_length),dtype=int)
        
        self.body[1:8,1::2] = 5
        self.body[1:8,::2] = 1 
        self.body[4,:] = 1
     
    def return_body(self):
        return self.body
        
        
       

    def plot_plane(self):
        self.bounds=[0,5]
        self.cmap = mpl.colors.ListedColormap(['blue','black','red'])
        self.norm = mpl.colors.BoundaryNorm(self.bounds, self.cmap.N)
        self.img = self.plt.imshow(self.body,interpolation='nearest')#, cmap = cmap,norm=norm)
        return self.img
    


        
class Agent:
    
    def __init__(self, x_position, y_position, destination, status ):
        self.x_position = x_position
        self.y_position = y_position
        self.destination_x = destination
        self.destination_y = status
        #self.status = status   #Tuple for destination or mapping, seat_number correesponds to tuple

    def set_position(self,x_position,y_position ):
        self.x_position = x_position
        self.y_position = y_position



body_airplane = Plane_map()

body = body_airplane.return_body()


bounds=[0,5]
cmap = mpl.colors.ListedColormap(['blue','black','red'])
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
img = pyplot.imshow(body,interpolation='nearest')

agents_waiting =[]
agents_searching =[]

for i in range (0,3):
    agents_waiting.append(Agent(None,None,3-i,6))
    agents_waiting.append(Agent(None,None,i+5,6))
    print(i)
for i in range (0,3):
    agents_waiting.append(Agent(None,None,3-i,8))
    agents_waiting.append(Agent(None,None,i+5,8))
    print(i)
for i in range (0,3):
    agents_waiting.append(Agent(None,None,3-i,10))
    agents_waiting.append(Agent(None,None,i+5,10))
    print(i)
enter = True

temp_test = True
agent_index = 1
for a in range (1, 50):
  
    if enter:
        if  agents_waiting:
            agents_searching.append(agents_waiting.pop(-1))
            agents_searching[-1].set_position(0,0)
        
        enter = False
    for agent in agents_searching:
        if a%2 == 0:
            enter = True
        
        
        if agent.y_position != agent.destination_y:
            if agent.x_position != 4: #middlerow
                agent.x_position += 1
                body[agent.x_position][agent.y_position] = 2
                body[agent.x_position-1][agent.y_position] = 1
                
            else:
                
                agent.y_position += 1
                body[agent.x_position][agent.y_position] = 2
                body[agent.x_position][agent.y_position-1] = 1
        else:
        
            if agent.x_position <  agent.destination_x:
                agent.x_position += 1
                body[agent.x_position][agent.y_position] = 2
                body[agent.x_position-1][agent.y_position] = 1
            elif  agent.x_position >  agent.destination_x:
                agent.x_position -= 1
                body[agent.x_position][agent.y_position] = 2
                body[agent.x_position+1][agent.y_position] = 1
            
    img = pyplot.imshow(body,interpolation='nearest')
    pyplot.pause(1)
    

pyplot.show()

