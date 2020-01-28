#
# CS1010S --- Programming Methodology
#
# Mission 11b
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: A0184573W Dinh Nho Bao

###############
# Mission 11b #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x,x)

# (a) What are the types of the input and output of the generic square operation?(1 mark)
# Answer: (Generic-Num) -> Generic-Num

# (b) Why would we prefer to define square in the above way, rather than: (2 marks)
# def square(x):
#    return apply_generic("square",x)
# Answer: Because defining square using mul utilizes pre-defined functions in the table procs,
# such as mul_ord, mul_rat or mul_com. Using square(x) would require defining other functions,
# such as square_ord, square_rat or square_com, and adding them to the table.



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

# Answer: It depends on the number of inputs that each corresponding function requires. For
# make_ord(x), only 1 argument is required, hence only 1 string "ordinary" is required for the make operator.
# For add_ord(x, y), 2 arguments are required, hence 2 strings ("ordinary", "ordinary") are required for the add operator.


##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic complex number. Here are two tries at
# producing 9+10i. Which is the right way?

# first_try = create_complex(9, 10)
# second_try = create_complex(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce c9+10i and c3+10i and then try to add
# them? Why does this happen?

# Right way: second_try
# What happens: raise Exception('Bad tagged datum -- type_tag ', datum)
# Exception: ('Bad tagged datum -- type_tag ', 9)

# Why it happens: create_complex takes in 2 Generic-Num type inputs, which are created by create_ordinary.
# The numbers 9 and 10, despite being ordinary numbers, do not have tags, so they are not of the Generic-Num type.

##########
# Task 4 #
##########

# Produce expressions that define c2_plus_7i to be the generic complex number whose real part is 2
# and whose imaginary part is 7, and c3_plus_1i to be the generic complex number whose real part
# is 3 and whose imaginary part is 1. Assume that the expression
# >>> csq = square(sub(c2_plus_7i, c3_plus_1i))
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
# c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))
# c3_plus_1i = create_complex(create_ordinary(3), create_ordinary(1))
# csq = square(sub(c2_plus_7i, c3_plus_1i))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##            |   |   |    ---|--->
##            +---+---+---+---+
##                |
##                v

##            +---+---+---+---+
##            |   |   |   |   |
##            +---+---+---+---+
##                |       |
##                v       v

##########
# Task 5 #
##########

# Within the generic complex number package, the internal add_com function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: Because the fuction add_com calls the function add, so if we rename the function as
# "add" will cause the programme to enter an infinite loop.

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_complex_package, indicating clearly your modifications.
def install_complex_package():
    def make_com(x,y):
        return tag(repcom(x,y))
    def repcom(x,y):
        return (x,y)
    def real(x):
        return x[0]
    def imag(x):
        return x[1]
    def tag(x):
        return attach_tag("complex",x)
    # add,sub,mul,div: (RepCom, RepCom) -> Generic-Com
    def add_com(x,y):
        return make_com( add(real(x), real(y)),
                         add(imag(x), imag(y)) )
    def sub_com(x,y):
        return make_com( sub(real(x), real(y)),
                         sub(imag(x), imag(y)) )
    def mul_com(x,y):
         return make_com(sub(mul(real(x), real(y)),
                             mul(imag(x), imag(y))),
                         add(mul(real(x), imag(y)),
                             mul(real(y), imag(x))))
    def div_com(x,y):
        com_conj = complex_conjugate(y)
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com(div(real(x_times_com_conj), real(y_times_com_conj)),
                        div(imag(x_times_com_conj), real(y_times_com_conj)))
    def complex_conjugate(x):
        return (real(x),negate(imag(x)))
    def negate(x):
        return make_com(negate(real(x)), negate(imag(x)))
    # negate: (RepCom) -> Generic-Com
    def is_zero_com(x):
        return is_zero(real(x)) and  is_zero(imag(x))
    # is_zero_com: (RepCom) -> Boolean
    def is_eq_com(x, y):
        return is_equal(real(x), real(y)) and is_equal(imag(x), imag(y))
    # is_eq_com: (RepCom, RepCom) -> Boolean
    
    put("make","complex", make_com)
    put("add",("complex","complex"), add_com)
    put("sub",("complex","complex"), sub_com)
    put("mul",("complex","complex"), mul_com)
    put("div",("complex","complex"), div_com)
    put("negate",("complex",), negate)
    put("is_zero_com",("complex",), is_zero_com)
    put("is_equal",("complex","complex"), is_eq_com)
    
install_complex_package()

def create_complex(x,y):
    return get("make","complex")(x,y)

######################################################
# Change the value for variable: c_neg3_plus_10i, c1_plus_2i and c1_plus_3i #
######################################################
c_neg3_plus_10i = create_complex(create_ordinary(-3), create_ordinary(10))
c1_plus_2i = create_complex(create_ordinary(1), create_ordinary(2))
c1_plus_3i = create_complex(create_ordinary(1), create_ordinary(3))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(c_neg3_plus_10i, mul(c1_plus_2i, c1_plus_3i)),
        add(c1_plus_2i, c1_plus_3i)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
