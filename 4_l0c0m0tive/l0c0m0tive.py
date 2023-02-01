"""Functions which helps the locomotive engineer to keep track of the train."""


# Example on the exercism page
fruits = ("apple", "banana", "cherry")
more_fruits = ["orange", "kiwi", "melon", "mango"]

# fruits and more_fruits are unpacked and then their elements are packed into combined_fruits
combined_fruits = *fruits, *more_fruits

print(combined_fruits)
# If there is no * on to the left of the "=" the result is a tuple

# If the * operator is used on the left side of "=" the result is a list
(*combined_fruits_too,) = *fruits, *more_fruits
print(combined_fruits_too)


# From what I understood, * is general purpose and ** is made for dictionaries

# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # * on the left of the = returns a list
    (*wagon_list,) = args
    return wagon_list


print(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5))


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # would love to figure out a way to write just one end_wagon variable
    [end_wagon1, end_wagon2, locomotive, *rest_of_wagons] = each_wagons_id
    wagons = [locomotive, *missing_wagons, *rest_of_wagons, end_wagon1, end_wagon2]
    return wagons


print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))


# TODO: define the 'add_missing_stops()' function
def add_missing_stops(a, **kargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    from_to = a
    (
        *stops,
    ) = (
        kargs.values()
    )  #  this way I get the values as a list and not with dict_values(...) attached to the list

    # these are both dicts

    from_to["stops"] = stops  # not sure if I'm supposed to do it like this
    return from_to


print(
    add_missing_stops(
        {"from": "New York", "to": "Miami"},
        stop_1="Washington, DC",
        stop_2="Charlotte",
        stop_3="Atlanta",
        stop_4="Jacksonville",
        stop_5="Orlando",
    )
)

# TODO: define the 'extend_route_information()' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


print(
    extend_route_information(
        {"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}
    )
)


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    row1, row2, row3 = wagons_rows
    
    # rows have the same colors, now this needs to be done for the columns

    newrow1 = [row1[0], row2[0], row3[0]]
    newrow2 = [row1[1], row2[1], row3[1]]
    newrow3 = [row1[2], row2[2], row3[2]]
    
    return [newrow1, newrow2, newrow3]


print(
    fix_wagon_depot(
        [
            [(2, "red"), (4, "red"), (8, "red")],
            [(5, "blue"), (9, "blue"), (13, "blue")],
            [(3, "orange"), (7, "orange"), (11, "orange")],
        ]
    )
)
