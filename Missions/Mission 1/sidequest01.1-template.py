#
# CS1010S --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(rune, count):
    a = stackn(count, rune) #make side
    b = stackn((count - 2), quarter_turn_left(rune)) #make top and bottom
    c = stack_frac(((count - 2)/(count - 1)), rune, quarter_turn_right(b)) #stack bottom and middle
    d = stack_frac(1/count, quarter_turn_right(b), c) # stack bottom, middle and top
    e = quarter_turn_left(stack_frac(1/count, quarter_turn_right(a), (stack_frac((count -2)/(count - 1), quarter_turn_right(d), quarter_turn_right(a)))))
    return e
# Test
show(egyptian(heart_bb, 5))
