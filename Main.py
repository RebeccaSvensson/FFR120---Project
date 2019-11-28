class Passenger:

    def __init__(self):
        self.x
        self.y

        self.id

        self.seat_destination # vector [x_dest, y_dest]

        self.seated
        self.blocking

    def __repr__(self):
        return str(self.id) + ' (' + str(self.x) + ',' + str(self.y) + ')'

    def move(self, direction):
        if direction == 'positive_y':
            self.y +=1
        elif direction == 'negative_y':
            self.y -= 1
        elif direction == 'positive_x':
            self.x += 1
        elif direction == 'negative_x':
            self.x -= 1

    def check_if_right_seat(self):
        if self.seat_destination[1] == self.y_position:
            return True
        else: 
            False

class Plane:

    def __init__(self):
        self.layout     #matrix, 0 is asile and 1 is seats
        self.grid   # matrix with passenger ID

        self.passengers     # list/hashmap?

        self.waiting_passengers     # sorted by boarding order
        self.in_plane_passengers

    def let_in_more_passengers(self):


def create_boarding_groups(pattern, passengers):
    if pattern is back_to_front:
        return groups
    elif pattern is random:
        return groups
    elif pattern is ...:
        return groups




def plot():
    

tidsloop


