#
# CS1010S --- Programming Methodology
#
# Contest 2.3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.
def starlight(pic1, pic2):
    big = pic1
    small = scale(9/10, pic1)
    inside = scale(9/10, pic2)
    return overlay(inside, overlay(small, big))

show(anaglyph(starlight(circle_bb, pentagram_bb)))


# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
