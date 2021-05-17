# Primary colours
RED = (1.0, 0.0, 0.0)
YELLOW = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)

# Secondary colours
ORANGE = (0.5, 0.5, 0.0)
GREEN = (0.0, 0.5, 0.5)
PURPLE = (0.5, 0.0, 0.5)

"""
Da Vinci is a busy man and he wants to mix his colours in as few actions
as possible. 

The trouble is, his colours are not perfect. Assume that each of Da Vinci's paints
can be represented as percentages of red, yellow and blue.

(Assume that he only cares about the hue; his black and white are fine and
he'll use them to reduce the saturation and make a paint darker or lighter)

He has 2 units of each paint. What is the closest he can get to each of the
secondary colours?
"""

# Da Vinci's paints
VINCI_RED = (8.0, 0.1, 0.1)
VINCI_YELLOW = (0.1, 0.9, 0.0)
VINCI_BLUE = (0.05, 0, 0.95)

def ratio(left_volume, right_volume):
    total = left_volume + right_volume
    return (left_volume / total), (right_volume / total)

def value(amount, ratio):
    return amount * ratio

# What is the closest Da Vinci can get to green, orange and purple?
# Please round numbers to 2 decimal places
def paint_addition(left, left_volume, right, right_volume):
    left_ratio, right_ratio = ratio(left_volume, right_volume)
    new_colour = (
        round(left_ratio * left[0], 2) + round(right_ratio * right[0], 2),
        round(left_ratio * left[1], 2) + round(right_ratio * right[1], 2),
        round(left_ratio * left[2], 2) + round(right_ratio * right[2], 2),
    )
    print(new_colour)

    return (
        new_colour,
        left_volume + right_volume,
    )

def three_way_equality(color, destination):
    if color == destination:
        return destination
    
    differences = (
        (destination[0] - color[0], VINCI_RED),
        (destination[1] - color[1], VINCI_YELLOW),
        (destination[2] - color[2], VINCI_BLUE),
    )

    most_different = sorted(differences, key=lambda x: x[0], reverse=True)
    print(most_different)

    return most_different[0][1]

assert three_way_equality((0.5, 0.5, 0.5), RED) == VINCI_RED
assert three_way_equality((0.5, 0.5, 0.5), YELLOW) == VINCI_YELLOW
assert three_way_equality((0.5, 0.5, 0.5), BLUE) == VINCI_BLUE    

def repeat(left, left_volume, right, right_volume, destination):
    last_left = left
    last_right = right

assert paint_addition(RED, 5, YELLOW, 5) == ((0.5, 0.5, 0), 10)
assert paint_addition(VINCI_RED, 1, VINCI_BLUE, 1) == ((0.55, 0.05, 0.52), 2)
assert (
    paint_addition(VINCI_RED, 5, VINCI_BLUE, 4) == 
    ((0.6000000000000001, 0.06, 0.48), 9)
)

assert paint_addition(VINCI_YELLOW, 1, VINCI_BLUE, 1) == ((0.1, 0.5, 0.47), 2)