"""Solution to Ellen's Alien Game exercise."""


from re import T


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, location_x, location_y) -> None:
        print("ALIEN INBOUND")
        Alien.total_aliens_created += (
            1  #  the Alien. allows me to access a class attribute
        )
        #  to make an alien's health I don't need to put a var in the function because it
        #  will always initialize at 3
        self.health = 3

        self.x_coordinate = location_x
        self.y_coordinate = location_y

    def hit(self):
        self.health -= 1
        # return self.health  #  this makes it print immediatly, not necessary

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def teleport(self, coord_x: int, coord_y: int):
        self.x_coordinate = coord_x
        self.y_coordinate = coord_y

    def collision_detection(self, other_obj):
        pass


# ----------------------------------------------------------------------------
def new_aliens_collection(alien_list):
    the_aliens = []

    for alien in alien_list:
        uYu = Alien(alien[0], alien[1])
        the_aliens.append(uYu)
    return the_aliens


alien_start_pos = [(4, 7), (-1, 0)]
aliens = new_aliens_collection(alien_start_pos)

for alien in aliens:
    print(alien.x_coordinate, alien.y_coordinate)

# ----------------------------------------------------------------------------


#  creating the aliens
alien1 = Alien(1, 2)
alien2 = Alien(-8, -9)

print(alien1.health)
#  checking if the aliens have their data
print(alien1.x_coordinate)
print(alien2.y_coordinate)


print(alien2.health)
print(alien2.hit())  #  don't forget the () after the function or stuff doesn't run
print(alien2.health)
print(alien2.hit())
print(alien2.health)
alien2.hit()  # this hit kills it

print(alien2.is_alive())

alien1.teleport(6, 7)
print(alien1.x_coordinate)
print(alien1.y_coordinate)

print(alien1.collision_detection())

print(alien2.total_aliens_created)
print(Alien.total_aliens_created)

alien3 = Alien((1, 1))
print(alien1.total_aliens_created)
#  you can edit a variable name by pressing F2

# TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
