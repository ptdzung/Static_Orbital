#
# CS1010S --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *
from math import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(scale(0.5/cos(theta))(curve_fn)), translate(0.5, tan(theta) * 0.5)(rotate(-theta)(scale(0.5/cos(theta))(curve_fn)))))
    return inner_gosperize





# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(10)(0.1), 50)



# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below
##print(profile_fn(lambda: gosper_curve(10)(0.1), 500))


# Time measurements
# Average time: 85.3845703058735


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

##print(profile_fn(lambda: gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1), 500))

#  Average time: 89.90147605990602

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

##print(profile_fn(lambda: your_gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1), 500))

# Average time: 1648.3140510992057


# Conclusion:
#  The more customized the functions, the more time it takes for the programme to run. Hence, there is a speed advantage for more generalized functions.

##########
# Task 2 #
##########

#  1) Yes.


#  2) The time complexity for 'rotate' is O(n), but the time complexity for 'joe_rotate' is O(n^2), because x and y are functions that call curve(t).


##########
# Task 3 #
##########

original_rotate = rotate
##replace_fn(rotate, joe_rotate)
replace_fn(rotate, original_rotate)

t = 5
trace(x_of)
gosper_curve(t)(0.5)
untrace(x_of)
gosper_curve(t)(0.5)



#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1         <3>         <4>
#                      2         <5>         <10>
#                      3         <7>         <22>
#                      4         <9>         <46>
#                      5         <11>         <95>
#
#  Evidence of exponential growth in joe_rotate.

