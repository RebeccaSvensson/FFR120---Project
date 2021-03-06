import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


class Passenger:

    def __init__(self, id, rownr=None, colnr=None):
        self.rownr = rownr  # seat row
        self.colnr = colnr  # seat number

        self.id = id

        self.seat_destination = None  # [seat row, seat number]

        self.seated = False
        self.blocking = False
        self.waiting = False
        self.getting_back = False

        self.luggage = True
        self.left_luggage = 0
        self.blocking_destination = None

    def __repr__(self):
        #      return str(self.id) + ' (' + str(self.rownr) + ',' + str(self.colnr) + ')'
        return str(self.seat_destination)

    def __str__(self):
        return self.__repr__()

    def move(self, rownrdir, colnrdir):
        self.rownr = self.rownr + rownrdir
        self.colnr = self.colnr + colnrdir

    def moveTo(self, new_row_nr, new_col_nr):
        self.rownr = new_row_nr
        self.colnr = new_col_nr

    def set_position(self, rownr, colnr):
        self.rownr = rownr
        self.colnr = colnr

    def set_seated(self, isSeated):
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

    def handle_luggage(self):
        if self.luggage:
            if self.rownr == self.seat_destination[0] and self.colnr == n_seats_in_row:
                self.left_luggage += 1
                if self.left_luggage == 3:
                    self.luggage = False

    def next_row(self):
        if self.rownr + 1 == self.seat_destination[0]:
            return True
        else:
            return False

    def now_blocking(self, nr_in_the_way):
        self.blocking = True
        self.seated = False

        if self.seat_destination[1] == 1 or self.seat_destination[1] == plane.layout.shape[1] - 2:
            self.blocking_destination = [self.seat_destination[0] + 1, n_seats_in_row]
        else:
            self.blocking_destination = [self.seat_destination[0] + nr_in_the_way, n_seats_in_row]


class Plane:

    def __init__(self, nr_of_rows, seats_in_row, aisle_width):
        plane_width = 2 * seats_in_row + aisle_width
        plane_length = nr_of_rows + seats_in_row

        self.layout = np.ones((plane_length, plane_width))  # matrix, 0 is aisle, 1 is seats and -1 is unavailable
        self.layout[0, :] = -1
        self.layout[(-seats_in_row + 1)::, :] = -1
        self.layout[0, 0:seats_in_row] = 0
        self.layout[:, seats_in_row] = 0

        self.positions = -np.ones((plane_length, plane_width))  # matrix with passenger ID

        self.passengers = []

        self.waiting_passengers = []
        self.in_plane_passengers = []

    def let_in_more_passengers(self):
        if self.positions[0, 0] == -1:
            if self.waiting_passengers:
                passenger = self.waiting_passengers.pop(0)
                passenger.set_position(0, 0)
                self.in_plane_passengers.append(passenger)
                self.positions[0, 0] = passenger.id


# Pattern can be: BackToFrontSorted, Random, WindowAisle, WindowAisleSorted, Blocks, ReversePyramid, BackToFront, SteffenModified
def create_boarding_groups(pattern, passengers, plane):
    sorted_list = []

    if pattern is 'BackToFrontSorted':
        sorted_list = sorted(passengers, key=lambda passenger: (passenger.seat_destination[0]))
        sorted_list.reverse()

    elif pattern is 'Random':
        temp_passenger_list = passengers.copy()
        random.shuffle(temp_passenger_list)
        sorted_list = temp_passenger_list

    elif pattern is 'Blocks' or pattern is 'ReversePyramid' or pattern is 'BackToFront':  # Blocks are front, back, middle
        n_blocks = 3
        limits = np.linspace(0, plane.layout.shape[0], n_blocks + 1)
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

        elif pattern is 'BackToFront':
            for i in range(n_blocks - 1, -1, -1):
                sorted_list.extend(blocks[i])


    elif pattern is 'WindowAisle':
        window = []
        aisle = []
        middle = []

        for passenger in passengers:
            seat_number = passenger.seat_destination[1]
            if seat_number == 0 or seat_number == plane.layout.shape[1] - 1:
                window.append(passenger)

            elif seat_number == 1 or seat_number == plane.layout.shape[1] - 2:
                middle.append(passenger)

            else:
                aisle.append(passenger)

        sorted_list = window + middle + aisle


    elif pattern is 'WindowAisleSorted':
        window = []
        aisle = []
        middle = []
        for passenger in passengers:
            seat_number = passenger.seat_destination[1]
            if seat_number == 0 or seat_number == plane.layout.shape[1] - 1:
                window.append(passenger)
            elif seat_number == 1 or seat_number == plane.layout.shape[1] - 2:
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

    elif pattern is 'SteffenModified':
        block_1 = []
        block_2 = []
        block_3 = []
        block_4 = []
        temp_passengers = passengers.copy()
        random.shuffle(temp_passengers)

        for passenger in temp_passengers:
            if passenger.seat_destination[0] % 2 == 0 and passenger.seat_destination[1] > plane.layout.shape[1] / 2:
                block_1.append(passenger)
            elif passenger.seat_destination[0] % 2 == 0 and passenger.seat_destination[1] < plane.layout.shape[1] / 2:
                block_2.append(passenger)
            elif passenger.seat_destination[0] % 2 != 0 and passenger.seat_destination[1] > plane.layout.shape[1] / 2:
                block_3.append(passenger)
            else:
                block_4.append(passenger)

        sorted_list = block_1 + block_2 + block_3 + block_4

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

    first_prio = []
    second_prio = []
    third_prio = []
    fourth_prio = []

    for passenger in plane.in_plane_passengers:
        if passenger.blocking:
            first_prio.append(passenger)
        elif passenger.waiting:
            second_prio.append(passenger)
        elif passenger.getting_back:
            third_prio.append(passenger)
        else:
            fourth_prio.append(passenger)

    priority_order = first_prio + second_prio + third_prio + fourth_prio

    for passenger in priority_order:
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

        passenger.handle_luggage()

        if passenger.blocking:
            if colnr == destcolnr:
                if rownr == passenger.seat_destination[0]:
                    if passenger.luggage:
                        continue
                colnrdir = 0
                rownrdir = np.sign(destrownr - rownr)
                if rownr + 2 < plane.layout.shape[0]:
                    idTwoSteps = int(plane.positions[rownr + 2, colnr])
                    if idTwoSteps != -1:
                        if passengers[idTwoSteps].seat_destination[0] == rownr + 1:
                            continue
                if rownr + 3 < plane.layout.shape[0]:
                    idThreeSteps = int(plane.positions[rownr + 3, colnr])
                    if idThreeSteps != -1:
                        if passengers[idThreeSteps].seat_destination[0] == rownr + 1:
                            continue

                update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)
                if passenger.correct_row():
                    passenger.blocking = False
                    passenger.getting_back = True

            else:
                colnrdir = np.sign(destcolnr - colnr)
                rownrdir = 0
                update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)
            continue

        # If passenger at the correct row:
        if passenger.correct_row():
            # Case 7
            if passenger.correct_seat():
                passenger.seated = True
                passenger.waiting = False
                passenger.getting_back = False

            elif passenger.luggage:
                continue

            # Case 5 and 6
            else:
                if destcolnr < colnr:
                    # Direction to move
                    rownrdir = 0
                    colnrdir = -1
                else:
                    rownrdir = 0
                    colnrdir = 1
                update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)

        # Case 4
        elif colnr == n_seats_in_row:  # and passenger.next_row():

            rownrdir = np.sign(destrownr - rownr)
            colnrdir = 0
            if rownrdir < 0:
                update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)
                continue

            # Case 2 and 3
            if not passenger.waiting:
                idTwoSteps = int(plane.positions[rownr + 2, colnr])
                idThreeSteps = int(plane.positions[rownr + 3, colnr])
                if idTwoSteps != -1:
                    if passengers[idTwoSteps].seat_destination[0] == rownr + 1:
                        continue
                if idThreeSteps != -1:
                    if passengers[idThreeSteps].seat_destination[0] == rownr + 1:
                        continue

            if not passenger.next_row():
                update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)
                continue

            destcoldir = np.sign(destcolnr - colnr)

            # == Check way and move if relevant ==

            # If first seat is yours, move.
            if destcolnr == colnr + destcoldir:
                update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)
                continue

            # If second seat yours, check if empty
            elif destcolnr == colnr + 2 * destcoldir:
                idAisle = int(plane.positions[destrownr, colnr])
                idFirst = int(plane.positions[destrownr, colnr + destcoldir])

                if idAisle != -1:
                    destAisle = passengers[idAisle].seat_destination
                    if destAisle[1] == destcolnr - destcoldir:
                        tell_them_to_move(passenger.id, [idAisle])
                        continue
                if idFirst != -1:
                    destFirst = passengers[idFirst].seat_destination
                    if destFirst[1] == destcolnr - destcoldir:
                        tell_them_to_move(passenger.id, [idFirst])
                        continue
                update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)

            # If third seat yours:
            else:
                idAisle = int(plane.positions[destrownr, colnr])
                idSeat1 = int(plane.positions[destrownr, colnr + destcoldir])
                idSeat2 = int(plane.positions[destrownr, colnr + 2 * destcoldir])

                idOthers = []

                if idAisle != -1:
                    destAisle = passengers[idAisle].seat_destination
                    if destAisle[0] == destrownr:
                        if destAisle[1] == destcolnr - destcoldir or destAisle[1] == destcolnr - 2 * destcoldir:
                            idOthers.append(idAisle)
                if idSeat1 != -1:
                    idOthers.append(idSeat1)
                    # passengers(idSeat2).tell_them_to_move()
                if idSeat2 != -1:
                    idOthers.append(idSeat2)
                if len(idOthers) != 0:
                    tell_them_to_move(passenger.id, idOthers)
                    continue
                else:
                    update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)

        # Case 1
        elif rownr == 0 and colnr < n_seats_in_row:
            rownrdir = 0
            colnrdir = 1
            update_position(passenger.id, rownr, colnr, rownrdir, colnrdir)

    plane.let_in_more_passengers()

    if seated == len(passengers):
        return True

    return False


def update_position(id, rownr, colnr, rownrdir, colnrdir):
    if plane.positions[rownr + rownrdir, colnr + colnrdir] == -1:
        plane.positions[rownr, colnr] = -1
        passengers[id].move(rownrdir, colnrdir)
        plane.positions[rownr + rownrdir, colnr + colnrdir] = id


def tell_them_to_move(id, other_ids):
    for other_id in other_ids:
        passengers[other_id].now_blocking(len(other_ids))
    passengers[id].waiting = True


def start_boarding():
    for t in range(number_of_timesteps):
        allSeated = step_in_time()

        if allSeated:
            return t
    return t


nr_runs = 1000
time_results = np.zeros(nr_runs)

# == Layout settings ==
nr_of_rows = 30
n_seats_in_row = 3
aisle_width = 1
boarding_method = 'Blocks'

n_passengers = nr_of_rows * 2 * n_seats_in_row

# == Video settings ==
number_of_timesteps = 1000

it = 0
while it < nr_runs:
    print(it)
    passengers = []

    # == Get the passengers in order ==
    plane = Plane(nr_of_rows, n_seats_in_row, aisle_width)
    plane.passengers = passengers

    for i in range(n_passengers):
        passenger = Passenger(i)
        passengers.append(passenger)

    assign_seats(passengers, plane)

    passengers_sorted = create_boarding_groups(boarding_method, passengers, plane)
    plane.waiting_passengers = passengers_sorted

    # == Start boarding ==
    ti = start_boarding()
    if ti != (number_of_timesteps-1):
        time_results[it] = ti
        it = it+1

print(f"Mean: {np.mean(time_results)}")
print(f"Median: {np.median(time_results)}")
print(f"Min time: {min(time_results)}")
print(f"Max time: {max(time_results)}")

plt.hist(time_results, bins = 30)
plt.gca().set(title = 'Time distribution for Rotating Blocks', xlabel='Boarding time', ylabel='Nr of runs')
plt.show()