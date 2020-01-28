#
# CS1010S --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(pic, number):
    old_pic = pic
    if number <= 0:
        return None
    if number == 1:
        return pic
    else:
        return beside(old_pic, stackn(2, fractal(pic,  number - 1)))


# Test
##show(fractal(make_cross(rcross_bb), 4))
##show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic, number):
    old_pic = pic
    while number > 1:
        pic = beside(old_pic, stackn(2, pic))
        number -=1
    return pic

##show(fractal_iter(make_cross(rcross_bb), 3))
##show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########        

##def dual_fractal(pic1, pic2, n):
##    if n <= 0:
##        return None
##    elif n == 1:
##        return pic1
##    elif n == 2:
##        return quarter_turn_left(stack_frac(1/2, quarter_turn_right(pic1), quarter_turn_right(stackn(2, pic2))))
##    elif n % 2 == 0:
##        return 
##    else:
##        return beside(pic1, stackn(2, dual_fractal(pic2, pic1, n-1)))

def dual_fractal(pic1, pic2, n):
    if n <= 0:
        return None
    elif n == 1:
        return pic1
    elif n == 2:
        return beside(pic1, stackn(2, pic2))
    elif n % 2 == 0:
        return beside(pic1, beside(stackn(2, pic2), stackn(4, dual_fractal (pic1, pic2, n-2))))
    else:
        return beside(pic1, stackn(2, dual_fractal(pic2, pic1, n-1)))


##### Test
####show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
##show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
### Write your additional test cases here
##
### Note that when n is even, the first (biggest) rune should still be rune1
##
#############
### Task 1d #
#############
##

##def dual_fractal_iter(pic1, pic2, n):
##    if n % 2 == 1:
##        i = 1
##        pic = pic1
##        for i in range(n -1):
##            if i % 2 == 0:
##                new_pic = pic2
##            else:
##                new_pic = pic1
##            pic = beside(new_pic, stackn(2, pic))
##            i = i+1
##        return pic
##    else:
##        i = 1
##        pic = pic2
##        for i in range(n -1):
##            if i % 2 == 0:
##                new_pic = pic1
##            else:
##                new_pic = pic2
##            pic = beside(new_pic, stackn(2, pic))
##            i = i+1
##        return pic
####
##### Test
##show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
##show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
### show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
### Write your additional test cases here
##
### Note that when n is even, the first (biggest) rune should still be rune1
##
############
### Task 2 #
############
##

##def steps(pic1, pic2, pic3, pic4):
##    top_left = beside(stack(pic4, blank_bb), stackn(2, blank_bb))
##    top_right = beside(stackn(2, blank_bb),stack(pic1, blank_bb))
##    bottom_left = beside(stack(blank_bb, pic3), stackn(2, blank_bb))
##    bottom_right = beside(stackn(2, blank_bb), stack(blank_bb, pic2))
##    return overlay(overlay(top_left, bottom_left), overlay(bottom_right, top_right))

# Test
##show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
