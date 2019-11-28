class Passenger:

    def __init__(self, id, seat):
        self.x = -1
        self.y = -1

        self.id = id

        self.seat_destination = seat

        self.seated = False
        self.blocking = False

    def __repr__(self):
        return str(self.id) + ' (' + str(self.x) + ',' + str(self.y) + ')'

    def move(self, xdir,ydir):
        newx = ´self.x+xdir
        newy = self.y+ydir
        if plane.
    
    def set_position(self,x,y):
        self.x = x
        self.y = y
        
    def set_seated(self,isSeated):
        self.seated = isSeated
        
    def correct_row(self):
        if self.x == self.seat_destination[0]:
            return True
        else:
            return False

class Plane:
# nrOfRows - of seats, not in grid or layout
# seatsInSegment - nr of seats on one side of aisle
# layout - grid over seat/aisle/nothing
# grid/positions - grid over who is where in plane 
# passengers - list of all passengers in order of id and seat
# waiting_passengers - queue of passengers outside plane
# in_plane_passengers - list of all inside plane

    def __init__(self,passengers):
    
        self.passengers = passengers
        
        self.nrOfRows = 20
        self.seatsInSegment = 3
        self.layout = np.ones([nrOfRows+seatsInSegment+1,2*seatsInSegments+1])   #matrix, 0=aisle, 1=seat, -1=nothing
        
        # Make a layout with an entrance, rows of seats with one aisle and some extra aisle space in the back
        self.layout[0,:] = -1
        self.layout[-seatsInSegment::,:] = -1
        self.layout[0,0:seatsInSegment] = 0
        self.layout[seatsInSegment,:] = 0
        
        self.positions = -np.ones([nrOfRows+seatsInSegment+1,2*seatsInSegments+1])   # matrix with passenger ID



        # Make a queue of passengers outside plane
        order = self.passangers.copy()
        order = random.shuffle(order)
        self.waiting_passengers = order    # sorted by boarding order
        
        self.in_plane_passengers = []

    def let_in_more_passengers(self):
        if self.positions[0,0] == -1:
            passenger = self.waiting_passangers.pop()
            passenger.setPosition(0,0)
            self.in_plane_passengers.append(passenger)
            
    def update_positions(in_plane_passengers):
        positions = np.-np.ones([nrOfRows+seatsInSegment+1,2*seatsInSegments+1])
        for passenger in in_plane_passenger:
            x = passenger.x
            y = passenger.y
            id = passenger.id
            positions[x,y] = id


def create_boarding_groups(pattern, passengers):
    if pattern is back_to_front:
        return groups
    elif pattern is random:
        return groups
    elif pattern is ...:
        return groups

def plot():
     
     
def start_boarding():
    plane.let_in_more_passengers()
    allSeated = False
    while not allSeated:
        allSeated = stepInTime()
        
    
    
maxTime = 100
# Make list of all passengers with id and seat
passengers = []     # list/hashmap?
for row in range(self.nrOfRows):
    for col in range(2*seatsInSegment):
        self.passengers.append(Passenger(row*2*seatsInSegment + col))

# Initialize plane
plane = Plane(passengers)

# Create a queue of passengers
queue = random.shuffle(passengers)

# Sort queue according to boarding pattern
queue = boarding_groups(pattern,queue,plane)

#Start boarding
start_boarding()

#time loop, assuming only three seats
def step_in_time():
    seated = 0
    
    for passenger in plane.in_plane_passengers:
        if passenger.seated:
            seated += 1
            continue
        
        # Current position
        x = passenger.x
        y = passenger.y
        
        # destination in x
        destx = passenger.seat_destination[0]

        # If passenger in aisle at the correct row:
        if passenger.correct_row():
            if destx == x and not passenger.blocking:
                passenger.set_seated(True)
                continue
            elif destx < x:
                # Direction to move
                xdir = -1
                ydir = 0
            else:
                xdir = 1
                ydir = 0
            
            # If next pos empty
            if plane.positions[x+xdir,y+ydir] == -1:
                # If any of first two seats, move
                if destx == x+xdir or destx == x+2*xdir:
                    plane.positions[x,y] = -1
                    passenger.move(xdir,ydir)
                    plane.positions[x+xdir,y+ydir] = passenger.ID
                    
                else:
                    if plane.positions[x+2*xdir,y+2*ydir] == -1:
                        passenger.move(xdir,ydir)
                    else:
                        idOtherPassenger = plane.positions[x+2*xdir,y+2*ydir]

                        tell_them_to_move(passenger[idOtherPassenger])

            # If not empty:
            else:
                # Check who is there
                idOtherPassenger = plane.positions[x+xdir,y+ydir]
                # Check where they are going
                otherDest = passengers[idOtherPassenger].destination
                
                #if all okay, but need to wait:
                if otherDest[0]+xdir == destx or otherDest[0]+2*xdir == destx:
                    continue
                else: #If they are blocking
                    tell_them_to_move(passenger.id, passenger[idOtherPassenger])
                    
        else:
            xdir = 0
            ydir = 1
            if plane.positions[x+xdir,y+ydir] == -1:
                plane.positions[x,y] = -1
                passenger.move(xdir,ydir)
                plane.positions[x+xdir,y+ydir] = passenger.ID
    
    plane.let_in_more_passengers()
    
    if seated == len(passengers):
        return true
        
    return false
    
def tell_them_to_move():
    #1. Blocking = True on those blocking
    #2. Back up.

