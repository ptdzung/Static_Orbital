#
# CS1010S --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(number, picture):
    if number == 1:
        return picture
    else:
        pic = picture
        n = 2
        for i in range(number, 1 , -1):
            pic = overlay_frac(1/n, scale((i - 1)/number, picture), pic)
            n = n + 1
        return pic



## Test
##show(tree(4, circle_bb))


##########
# Task 2 #
##########


# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(picture, number):
    i = 0
    r = 1/2 - 1/number
    pic = translate(0, r, scale(2/number, picture))
    for i in range(1, number):
        newpic = translate(r*cos(pi/2 - pi*2*i/number), r*sin(pi/2 - pi*2*i/number), scale(2/number, picture))
        pic = overlay_frac(i/(i+1), pic, newpic)
    return pic
##
### Test
show(helix(make_cross(rcross_bb), 9))
