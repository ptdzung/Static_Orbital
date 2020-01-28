#
# CS1010S --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *
from math import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    endcurve1 = curve1(1)
    startcurve2 = curve2(0)
    newcurve2=translate(x_of(endcurve1) - x_of(startcurve2), y_of(endcurve1) - y_of(startcurve2))(curve2)
    return connect_rigidly(curve1, newcurve2)

##########
# Task 2 #
##########

def show_points_gosper(level, num_points, initial_curve):
    curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)(repeated(gosperize, level)(initial_curve))
    return draw_points(num_points, curve)

show_points_gosper(5, 500, arc)

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(scale(0.5/cos(theta))(curve_fn)), translate(0.5, tan(theta) * 0.5)(rotate(-theta)(scale(0.5/cos(theta))(curve_fn)))))
    return inner_gosperize

# testing
draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
