import numpy as np
import random

class Passenger:

    def __init__(self, id, rownr = None, colnr = None):
        self.rownr = rownr  # seat row
        self.colnr = colnr  # seat number

        self.id = id

        self.seat_destination = None     # [seat row, seat number]

        self.seated = False
        self.blocking = False
        self.waitingFor = []
        
        self.blocking_destination = None

    def __repr__(self):
  #      return str(self.id) + ' (' + str(self.rownr) + ',' + str(self.colnr) + ')'
        return str(self.seat_destination)

    def __str__(self):
        return self.__repr__()

    def move(self, rownrdir,colnrdir):
        self.rownr = self.rownr + rownrdir
        self.colnr = self.colnr + colnrdir
        
    def set_position(self,rownr,colnr):
        self.rownr = rownr
        self.colnr = colnr

    def set_seated(self,isSeated):
        self.seated = isSeated
        
    def correct_seat(self):
        if self.correct_row():
            if self.blocking:
                if self.colnr == self.blocking_destination[1]:
                    self.blocking = False
                    return True
            elif self.colnr == self.seat_destination[1]:
                self.seated = True
                return True
        return False

    def correct_row(self):
        if self.blocking:
            if self.rownr == self.blocking_destination[0]:
                return True
        elif self.rownr == self.seat_destination[0]:
            return True
        else:
            return False
    
    def next_row(self):
        if self.rownr + 1 == self.seat_destination[0]:
            return True
        else:
            return False
            
    def now_blocking(self, other_id):
        self.blocking = True
        self.seated = False
        if colnr < n_seats_in_row:
            self.blocking_destination = [self.destination[0] + 1 + self.destination[1], n_seats_in_row]
        else:
            self.blocking_destination = [self.destination[0] + 1 + 2*n_seats_in_row - self.destination[1], n_seats_in_row]
            
        passengers(other_id).waitingFor.append(self.id)
                      
    def not_blocking(self):
        self.blocking = False
        
        


class Plane:

    def __init__(self, nr_of_rows, seats_in_row, aisle_width):
        plane_width = 2*seats_in_row + aisle_width
        plane_length = 1 + nr_of_rows + seats_in_row

        self.layout = np.ones((plane_length, plane_width))  #matrix, 0 is asile and 1 is seats
        self.layout[0,:] = -1
        self.layout[-seats_in_row::,:] = -1
        self.layout[0,0:seats_in_row] = 0
        self.layout[:,seats_in_row] = 0

        self.positions = -np.ones((plane_length, plane_width))  # matrix with passenger ID

        self.passengers = []

        self.waiting_passengers = []
        self.in_plane_passengers = []

    def let_in_more_passengers(self):
        if self.positions[0,0] == -1:
            if self.waiting_passengers:
                passenger = self.waiting_passengers.pop(0)
                passenger.set_position(0,0)
                self.in_plane_passengers.append(passenger)
                self.positions[0,0] = passenger.id
                

    def update_positions(in_plane_passengers):
        positions = -np.ones([nr_of_rows+seats_in_row+1,2*seats_in_rows+1])
        for passenger in in_plane_passenger:
            rownr = passenger.rownr
            colnr = passenger.colnr
            id = passenger.id
            positions[rownr,colnr] = id


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

#time loop, assuming only three seats
def step_in_time():
    seated = 0

    for passenger in plane.in_plane_passengers:
        if passenger.seated:
            seated += 1
            continue

        # Current position
        rownr = passenger.rownr
        colnr = passenger.colnr

        # Destination in colnr
        if passenger.blocking:
            destcolnr = passenger.blocking_destination[1]
            destrownr = passenger.blocking_destination[0]
        else:
            destcolnr = passenger.seat_destination[1]
            destrownr = passenger.seat_destination[0]
            
        # If passenger at the correct row:
        if passenger.correct_row():
            # Case 7
            if passenger.correct_seat():
                if passenger.blocking:
                    passenger.blocking = False
                else:
                    passenger.seated = True
             
            # Case 5 and 6
            else: #if not passenger.blocking:
                if destcolnr < colnr:
                    # Direction to move
                    rownrdir = 0
                    colnrdir = -1
                else:
                    rownrdir = 0
                    colnrdir = 1
                update_position(passenger.id,rownr,colnr,rownrdir,colnrdir)
        
        # Case 4
        elif colnr == n_seats_in_row and passenger.next_row():
            rownrdir = 1
            colnrdir = 0

            # == Check way and move if relevant ==
            
            # If first seat is yours, move.
            if destcolnr == colnr + destcolnr:
                update_position(passenger.id,rownr,colnr,rownrdir,colnrdir)
            
            # If second seat yours, check if empty
            elif destcolnr == colnr + 2*destcolnr:
                idSeat = plane.positions[rownr+rownrdir,colnr+colnrdir]
                # If first seat empty
                if idSeat == -1:
                    update_position(passenger.id,rownr,colnr,rownrdir,colnrdir)
                elif passengers(idSeat).seat_destination[1] == passengers(idSeat).colnr:
                    print('tell them to move')
                    continue
                    #passengers(idSeat).tell_them_to_move()
                else:
                    update_position(passenger.id,rownr,colnr,rownrdir,colnrdir)

            # If third seat yours:
            else:
                idSeat1 = plane.positions[rownr+rownrdir,colnr+colnrdir]
                idSeat2 = plane.positions[rownr+rownrdir,colnr+2*colnrdir]
                
                if idSeat1 == -1 and idSeat2 == -1:
                    update_position(passenger.id,rownr,colnr,rownrdir,colnrdir)
                else:
                    if idSeat1 == -1:
                        print('tell them to move')
                        continue#passengers(idSeat2).tell_them_to_move()
                    if idSeat2 == -1:
                        print('tell them to move')
                        continue#passengers(idSeat1).tell_them_to_move()
        
        # Case 1
        elif rownr == 0 and colnr < n_seats_in_row:
            rownrdir = 0
            colnrdir = 1
            update_position(passenger.id,rownr,colnr,rownrdir,colnrdir)
        # Case 2 and 3
        else:
            rownrdir = 1
            colnrdir = 0
            update_position(passenger.id,rownr,colnr,rownrdir,colnrdir)

    plane.let_in_more_passengers()

    if seated == len(passengers):
        return True

    return False

def update_position(id,rownr,colnr,rownrdir,colnrdir):
    if plane.positions[rownr+rownrdir,colnr+colnrdir] == -1:
        plane.positions[rownr,colnr] = -1
        passengers[id].move(rownrdir,colnrdir)
        plane.positions[rownr+rownrdir,colnr+colnrdir] = id

def tell_them_to_move(id, other_ids):
    for other_id in other_ids:
        passengers[other_id].now_blocking(id)
        
    #1. Blocking = True on those blocking


def start_boarding():
    plane.let_in_more_passengers()
    allSeated = False
    t = 1
    while not allSeated: #for i in range(6): #    
        t += 1
        print(t)
        allSeated = step_in_time()


passengers = []

nr_of_rows = 2
n_seats_in_row = 3
aisle_width = 1

n_passengers = nr_of_rows * 2 * n_seats_in_row

plane = Plane(nr_of_rows, n_seats_in_row, aisle_width)
plane.passengers = passengers

for i in range(n_passengers):
    passenger = Passenger(i)
    passengers.append(passenger)

assign_seats(passengers, plane)

passengers_sorted = create_boarding_groups('BackToFront', passengers, plane)
plane.waiting_passengers = passengers_sorted

maxTime = 100

#Start boarding
start_boarding()
