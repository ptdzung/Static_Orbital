#
# CS1010S --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.
def starlight(pic1, pic2):
    big = pic1
    small = scale(9/10, pic1)
    inside = scale(9/10, pic2)
    return overlay(inside, overlay(small, big))

show(starlight(circle_bb, pentagram_bb))



# Entry 2 of 3
# ============
# Write your function here. It should return a rune.


# show(<your rune>)



# Entry 3 of 3
# ============
# Write your function here. It should return a rune.


# show(<your rune>)
