#
# CS1010S --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's matric> Nguyen Thuy Duong

###############
# Mission 11a #
###############

##########
# Task 1 #
##########
# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x,x)

# (a) What are the types of the input and output of the generic square operation?(1 mark)
# Answer: square: (Generic-Num) -> (Generic-Num)

# (b) Why would we prefer to define square in the above way, rather than: (2 marks)
# def square(x):
#    return apply_generic("square",x)
# Answer: square is defined using mul. The function mul has already been
# implemented for different types of numbers (mul_ord, mul_rat, and mul_com). Hence
# the programmer would not need additional adjustments.
# If we use the latter way, we have to define square_ord, square_rat, and square_com 
# to put into the table procs so that the square function can work on different type of numbers.


##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by
# the name of the operator and a tuple of strings. For example, the add operator is indexed
# by ’add ord’ and (’ordinary’, ’ordinary’); negation is indexed by ’negate ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by ’make ord’ and just a string ’ordinary’.
# Explain why we have such a difference.
# Hint: Consider the differences in the process of the creation of a Generic-Num, such as create ordinary,
# and the operations we can apply on Generic-Num, such as add. How is make ord invoked, and how is add ord invoked?

# Answer:
# For make_ord:
# We have already put the function to the table: put("make","ordinary", make_ord)
# hence,
# def create_ordinary(x):
#   return get("make", "ordinary")(x) <---- will call make_ord(x)
# thus for generic number operator,  the constructor is indexed by 'make_ord' and 'ordinary'

# For add_odd:
# We have already put the function to the table: put("add",("ordinary","ordinary"), add_ord)
# --->hence add_odd will call add(x,y) ---> apply_generic("add", x, y) ---> get the tag
# --->get('add', type_tags)(contents) ---> result
# Here the type_tags we will need ('ordinary','ordinary') since there are two input numbers x,y.
# thus for generic number operator, the add operator is indexed by ’add_ord’ and (’ordinary’, ’ordinary’);







##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

#first_try = create_rational(9, 10)
#second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way: second_try

# What happens: raise Exception('No method for these types -- apply_generic', (op, type_tags))
# Exception: ('No method for these types -- apply_generic', ('add_rat', ('rational', 'rational')))
# It is not impossible to add 9/10 and 3/10 this way
# Why it happens:
# create_rational: (Generic-Num; Generic-Num) -> Generic-Rat.
# Generic-Num (i.e. number with tags) can only be created by create_ordinary. Putting a merely 9 or 10 will create
# a object of type RepNum, i.e. number without tags, which is the wrong input type for create_rational.

##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# r2_7 = create_rational(create_ordinary(2), create_ordinary(7))
# r3_1 = create_rational(create_ordinary(3), create_ordinary(1))
# csq = square(sub(r2_7, r3_1))
#https://drive.google.com/file/d/1VIjq0jSEcU5IdKYEFk-t9JLgC-3RhJ90/view?usp=sharing

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##            |       |       |  -->
##            +---+---+---+---+
##                |
##                v

##            +---+---+---+---+
##            |       |       |
##            +---+---+---+---+
##                |       |
##                v       v

##########
# Task 5 #
##########

# Within the generic rational number package, the internal add_rat function
# handled the addition operation. Why is it not possible to name this function "add"

# Answer:
# def add_rat(x,y):
#        return make_rat( add(mul(numer(x), denom(y)), <---- add function is already here
#                             mul(denom(x), numer(y))),
#                         mul(denom(x), denom(y)) )
# We can see that there is already a function add in the scope of add_rat (the global add function which is not put in any package), 
# so we can't change add_rat to the existing function add. It can lead to wrong input type or infinite loops, etc.

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x,y))
    def reprat(x,y):
        return (x,y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add,sub,mul,div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x,y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x,y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x,y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x,y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )
    
    def negate_rat(x): # (RepRat) -> Generic-Rat
        zero=create_ordinary(0)
        new_numer=apply_generic('sub',zero,numer(x))
        return make_rat(new_numer, denom(x))
    
    def is_zero_rat(x): # (RepRat) -> Py-Bool (Boolean)
        return apply_generic('is_zero',numer(x)) and not (apply_generic('is_zero',denom(x)))
    
    def is_equal_rat(x,y): # (RepRat, RepRat) -> Py-Bool (Boolean)
        return apply_generic('is_zero', sub_rat(x,y))
                             
    put("make","rational", make_rat)
    put("add",("rational","rational"), add_rat)
    put("sub",("rational","rational"), sub_rat)
    put("mul",("rational","rational"), mul_rat)
    put("div",("rational","rational"), div_rat)
    
    put("negate",("rational",), negate_rat)
    put("is_zero",("rational",), is_zero_rat)
    put("is_equal",("rational","rational"), is_equal_rat)
                             
install_rational_package()

def create_rational(x,y):
    return get("make","rational")(x,y)

######################################################
# Change the value for variable: r1_2, r2_4 and r1_8 #
######################################################
r1_2 = create_rational(create_ordinary(1), create_ordinary(2))
r2_4 = create_rational(create_ordinary(2), create_ordinary(4))
r1_8 = create_rational(create_ordinary(1), create_ordinary(8))
r0_1 = create_rational(create_ordinary(0), create_ordinary(1))
r4_8 = create_rational(create_ordinary(4), create_ordinary(8))

#################
# Do not change #
#################
#print(apply_generic('negate',r1_2),'hello')
#print(apply_generic('is_zero',r0_1),'test')
#print(is_equal(r2_4,r4_8))
print(is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)))	
