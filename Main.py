import numpy as np
import random

class Passenger:

    def __init__(self, id, x = None, y = None):
        self.x = x  # seat row
        self.y = y  # seat number

        self.id = id

        self.seat_destination = None     # [seat row, seat number]

        self.seated = False
        self.blocking = False

    def __repr__(self):
  #      return str(self.id) + ' (' + str(self.x) + ',' + str(self.y) + ')'
        return str(self.seat_destination)

    def __str__(self):
        return self.__repr__()

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


#    def move(self, direction):

class Plane:

    def __init__(self, n_seat_rows, seats_in_row, aisle_width):
        plane_width = 2*seats_in_row + aisle_width

        self.layout = np.ones((n_seat_rows, plane_width))  #matrix, 0 is asile and 1 is seats
        self.layout[0,:] = -1
        self.layout[-seats_in_row::,:] = -1
        self.layout[0,0:seats_in_row] = 0
        self.layout[seats_in_row,:] = 0

        self.grid = -np.ones((n_seat_rows, plane_width))  # matrix with passenger ID

        self.passengers = []

        self.waiting_passengers = []
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
#    def let_in_more_passengers(self, n_passengers):


# Pattern can be: BackToFront, Random, WindowAisle, Blocks, ReversePyramid
def create_boarding_groups(pattern, passengers, plane):
    sorted_list = []

    if pattern is 'BackToFront':
        sorted_list = sorted(passengers, key=lambda passenger: (passenger.seat_destination[0]))
        sorted_list.reverse()

    elif pattern is 'Random':
        random.shuffle(passengers)
        sorted_list = passengers

    elif pattern is 'Blocks' or pattern is 'ReversePyramid':    # Blocks are front, back, middle
        n_blocks = 3
        limits = np.linspace(0, plane.layout.shape[0], n_blocks+1)
        limits = np.floor(limits)

        blocks = []
        for i in range(n_blocks):
            blocks.append([])

        for passenger in passengers:
            seat_row = passenger.seat_destination[0]
            block_list = np.where(limits <= seat_row)[0]
            block = block_list[-1]
            blocks[block].append(passenger)

        if pattern is 'Blocks':
            # Sorts the blocks so no connecting blocks are boarded after one another
            for i in range(0, n_blocks, 2):
                sorted_list.extend(blocks[i])

            for i in range(1, n_blocks, 2):
                sorted_list.extend(blocks[i])

        elif pattern is 'ReversePyramid':
            for i in range(0, n_blocks, 2):
                temp_list = create_boarding_groups('WindowAisle', blocks[i], plane)
                sorted_list.extend(temp_list)

            for i in range(1, n_blocks, 2):
                temp_list = create_boarding_groups('WindowAisle', blocks[i], plane)
                sorted_list.extend(temp_list)

    elif pattern is 'WindowAisle':
        window = []
        aisle = []
        middle = []
        for passenger in passengers:
            seat_number = passenger.seat_destination[1]
            if seat_number == 0 or seat_number == plane.layout.shape[1]-1:
                window.append(passenger)
            elif seat_number == 1 or seat_number == plane.layout.shape[1]-2:
                middle.append(passenger)
            else:
                aisle.append(passenger)

        window = sorted(window,
                             key=lambda passenger: (passenger.seat_destination[0]))
        window.reverse()
        middle = sorted(middle,
                             key=lambda passenger: (passenger.seat_destination[0]))
        middle.reverse()
        aisle = sorted(aisle,
                        key=lambda passenger: (passenger.seat_destination[0]))
        aisle.reverse()
        sorted_list = window + middle + aisle


    return sorted_list

def assign_seats(passengers, plane):
    seats = np.where(plane.layout == 1)
    seats = list(zip(seats[0], seats[1]))

    for passenger in passengers:
        seat = random.choice(seats)
        seats.remove(seat)

        passenger.seat_destination = seat

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

def start_boarding():
    plane.let_in_more_passengers()
    allSeated = False
    while not allSeated:
        allSeated = stepInTime()


n_passengers = 12
passengers = []

n_seat_rows = 3
n_seats_in_row = 2
aisle_width = 1

plane = Plane(n_seat_rows, n_seats_in_row, aisle_width)
plane.passengers = passengers

for i in range(n_passengers):
    passenger = Passenger(i, 0, 0)
    passengers.append(passenger)

assign_seats(passengers, plane)

passengers_sorted = create_boarding_groups('Blocks', passengers, plane)
plane.waiting_passengers = passengers_sorted     

maxTime = 100
# Make list of all passengers with id and seat
passengers = []     # list/hashmap?
for row in range(self.nrOfRows):
    for col in range(2*seatsInSegment):
        self.passengers.append(Passenger(row*2*seatsInSegment + col))


#Start boarding
start_boarding()

#time loop, assuming only three seats
