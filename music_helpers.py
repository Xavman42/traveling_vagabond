import neoscore.core.neoscore
from neoscore.western import notehead_tables
from neoscore.western.duration import Duration
from neoscore.western.notehead import Notehead
from itertools import permutations


def initialize_helpers():
    global locked
    locked = {}


def lock_to_screen(glyph):
    global locked
    x, y = neoscore.core.neoscore.get_viewport_center_pos()
    locked_x = glyph.x - x
    locked[str(glyph)] = [glyph, locked_x]


def unlock_from_screen(glyph):
    global locked
    del locked[str(glyph)]


def unlock_all_from_screen():
    global locked
    locked.clear()


def move_locked_glyphs():
    global locked
    x, y = neoscore.core.neoscore.get_viewport_center_pos()
    for key in locked:
        locked[key][0].x = locked[key][1] + x


def aminoacid_to_symbol(amino, staff):
    match amino:
        case 'A':
            return Notehead(staff.unit(1), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'C':
            return Notehead(staff.unit(2), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'D':
            return Notehead(staff.unit(3), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'E':
            return Notehead(staff.unit(4), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'F':
            return Notehead(staff.unit(5), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'G':
            return Notehead(staff.unit(6), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'H':
            return Notehead(staff.unit(7), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'I':
            return Notehead(staff.unit(8), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'K':
            return Notehead(staff.unit(9), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'L':
            return Notehead(staff.unit(10), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'M':
            return Notehead(staff.unit(11), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'N':
            return Notehead(staff.unit(12), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'P':
            return Notehead(staff.unit(13), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'Q':
            return Notehead(staff.unit(14), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'R':
            return Notehead(staff.unit(15), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'S':
            return Notehead(staff.unit(16), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'T':
            return Notehead(staff.unit(17), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'V':
            return Notehead(staff.unit(18), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'W':
            return Notehead(staff.unit(19), staff, "g'", Duration(1, 4), table=notehead_tables.X)
        case 'Y':
            return Notehead(staff.unit(20), staff, "g'", Duration(1, 4), table=notehead_tables.X)


def brute_force_tsp(w, N):
    a = list(permutations(range(1, N)))
    last_best_distance = 1e10
    for i in a:
        distance = 0
        pre_j = 0
        for j in i:
            distance = distance + w[j, pre_j]
            pre_j = j
        distance = distance + w[pre_j, 0]
        order = (0,) + i
        if distance < last_best_distance:
            best_order = order
            last_best_distance = distance
            print("order = " + str(order) + " Distance = " + str(distance))
    return last_best_distance, best_order