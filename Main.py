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
    
    def setPosition(self,x,y):
        self.x = x
        self.y = y
        
    def setSeated(self,isSeated):
        self.seated = isSeated

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
            
    def updatePositions(in_plane_passengers):
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
     
     
def startBoarding():
    plane.let_in_more_passengers()
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
queue = boardingGroups(pattern,queue,plane)

#Start boarding
startBoarding()
stepInTime()

#tidsloop
def stepInTime():
"""    seated = []
    correctRow = []
    inAisle = []
    for passenger in plane.in_plane_passengers:    
        # för listor för olika states
        if passenger.seated: #passenger.locationState == 2:
            seated.append(passenger)
        elif passenger.checkRow(): #passenger.locationState == 1:
            correctRow.append(passenger)
        else: #passenger.locationState == 0
            inAisle.append(passenger)"""
    
    for passenger in plane.in_plane_passengers:
        if passenger.seated:
            continue
        
        # Current position
        x = passenger.x
        y = passenger.y
        
        # destination in x
        destx = passenger.seat_destination[0]

        # If passenger in aisle at the correct row:
        if passenger.correctRow():
            if destx == x:
                passenger.setSeated(True)
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
                    passenger.move(xdir,ydir)
                else:
                    if plane.positions[x+2*xdir,y+2*ydir] == -1:
                        passenger.move(xdir,ydir)
                    else:
                        
                    
                    #if all okay, but need to wait:
                    continue
                elif passenger.de
                    passenger.move(xdir,ydir)
                if plane.positions[x+2*xdir,y+2*ydir] == -1:
                    passenger.move(xdir,ydir)
            # If not empty:
            else:
                # Check who is there
                idOtherPassenger = plane.positions[x+xdir,y+ydir]
                # Check where they are going
                otherDest = passengers[idOtherPassenger].destination
                
                if 
                if xdir*otherDest[0] > xdir*passenger.destination[0]:
                    continue
                else:
                    tellThemToMove(passenger[idOtherPassenger])
                    

        else:
            passenger.move(0,1)
    
    
    
    for passenger in correctRow:
        
        passenger.move()
        
        row = passenger.getXPosition()
        column = passenger.getYPosition()
        destination = passenger.getDestination()
        direction = math.sgn(destination[1] - column)
        
        if column + direction == destination[1] and not cells[row][column+direction].isOccupied():
            move to correct seating

        kolla om någon är ivägen mellan aisle och destination
            om någon är ivägen, kolla om dess plats är innanför din plats:
        om lugnt med alla platser:
            move one step
        om inte lugnt med någon plats:
            backa och låt dem flytta
    
    for passenger in inAisle:
        if cell under is free:
            move one step down
    

    if not cells[0][0].isOccupied():
        # Let a new enter
        passengersInPlane.append(passengers.pop())

