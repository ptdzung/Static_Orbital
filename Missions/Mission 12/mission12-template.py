#
# CS1010S --- Programming Methodology
#
# Mission 12
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: A0184573W Dinh Nho Bao, 11a

from generic_arith_min import *

###########################
# Rational Number Package #
###########################

# Copy and paste the install_rational_package procedure from Mission
# 11a below and complete the tasks below for this mission.

    # Copy and paste your Mission 11a solution below here:

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


    


    ###########
    # Task 1a #
    ###########
def repord_to_reprat(x):
    return content(create_rational(create_ordinary(x), create_ordinary(1)))

    ###########
    # Task 2a #
    ###########
def RRmethod_to_ORmethod(method):
    return lambda ord, rat: method(repord_to_reprat(ord), rat)


def RRmethod_to_ROmethod(method):
    return lambda ord, rat: method(rat, repord_to_reprat(ord))

    ###########
    # Task 3a #
    ###########
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
        return make_rat( add(mul(numer(x), denom(y)), mul(denom(x), numer(y))), mul(denom(x), denom(y)) )
    def add_ord_rat(x, y):
        return RRmethod_to_ORmethod(add_rat)(x, y)   
    def add_rat_ord(x, y):
        return RRmethod_to_ROmethod(add_rat)(x, y)
            
    def sub_rat(x,y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_ord_rat(x, y):
        return RRmethod_to_ORmethod(sub_rat)(x, y)
    def sub_rat_ord(x, y):
        return RRmethod_to_ROmethod(sub_rat)(x, y)
        
    def mul_rat(x,y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def mul_ord_rat(x, y):
        return RRmethod_to_ORmethod(mul_rat)(x, y)
    def mul_rat_ord(x, y):
            return RRmethod_to_ROmethod(mul_rat)(x, y)
    
    def div_rat(x,y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )
    def div_ord_rat(x, y):
        return RRmethod_to_ORmethod(div_rat)(x, y)
    def div_rat_ord(x, y):
        return RRmethod_to_ROmethod(div_rat)(x, y)
    
    def negate_rat(x): # (RepRat) -> Generic-Rat
        zero=create_ordinary(0)
        new_numer=apply_generic('sub',zero,numer(x))
        return make_rat(new_numer, denom(x))
    
    def is_zero_rat(x): # (RepRat) -> Py-Bool (Boolean)
        return apply_generic('is_zero',numer(x)) and not (apply_generic('is_zero',denom(x)))
    
    def is_equal_rat(x,y): # (RepRat, RepRat) -> Py-Bool (Boolean)
        return apply_generic('is_zero', sub_rat(x,y))
    def is_equal_ord_rat(x, y):
        return RRmethod_to_ORmethod(is_equal_rat)(x, y)
    def is_equal_rat_ord(x, y):
        return RRmethod_to_ROmethod(is_equal_rat)(x, y)
    
    put("make","rational", make_rat)
    put("add",("rational","rational"), add_rat)
    put("add",("ordinary","rational"), add_ord_rat)
    put("add",("rational","ordinary"), add_rat_ord)
    put("sub",("rational","rational"), sub_rat)
    put("sub",("ordinary","rational"), sub_ord_rat)
    put("sub",("rational","ordinary"), sub_rat_ord)
    put("mul",("rational","rational"), mul_rat)
    put("mul",("ordinary","rational"), mul_ord_rat)
    put("mul",("rational","ordinary"), mul_rat_ord)
    put("div",("rational","rational"), div_rat)
    put("div",("ordinary","rational"), div_ord_rat)
    put("div",("rational","ordinary"), div_rat_ord)
    
    put("negate",("rational",), negate_rat)
    put("is_zero",("rational",), is_zero_rat)
    put("is_equal",("rational","rational"), is_equal_rat)
    put("is_equal",("ordinary","rational"), is_equal_ord_rat)
    put("is_equal",("rational","ordinary"), is_equal_rat_ord)
                             
install_rational_package()

def create_rational(x,y):
    return get("make","rational")(x,y)



###########################
# Complex Number Package  #
###########################

# Copy and paste the install_complex_package procedure from Mission
# 11b below and complete the tasks below for this mission.

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
    put("is_eq_com",("complex","complex"), is_eq_com)
    
install_complex_package()


    ###########
    # Task 1b #
    ###########
def repord_to_repcom(x):
    return content(create_complex(create_ordinary(x), create_ordinary(0)))

    ###########
    # Task 2b #
    ###########
def CCmethod_to_OCmethod(method):
    return lambda ord, com: method(repord_to_repcom(ord), com)


def CCmethod_to_COmethod(method):
    return lambda com, ord: method(com, repord_to_repcom(ord))

    ###########
    # Task 3b #
    ###########
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
        return make_com( add(real(x), real(y)), add(imag(x), imag(y)) )
    def add_ord_com(x, y):
        return CCmethod_to_OCmethod(add_com)(x, y)
    def add_com_ord(x, y):
        return CCmethod_to_COmethod(add_com)(x, y)
    
    def sub_com(x,y):
        return make_com( sub(real(x), real(y)),
                         sub(imag(x), imag(y)) )
    def sub_ord_com(x, y):
        return CCmethod_to_OCmethod(sub_com)(x, y)
    def sub_com_ord(x, y):
        return CCmethod_to_COmethod(sub_com)(x, y)
    
    def mul_com(x,y):
         return make_com(sub(mul(real(x), real(y)),
                             mul(imag(x), imag(y))),
                         add(mul(real(x), imag(y)),
                             mul(real(y), imag(x))))
    def mul_ord_com(x, y):
        return CCmethod_to_OCmethod(mul_com)(x, y)
    def mul_com_ord(x, y):
        return CCmethod_to_COmethod(mul_com)(x, y)
    
    def div_com(x,y):
        com_conj = complex_conjugate(y)
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com(div(real(x_times_com_conj), real(y_times_com_conj)),
                        div(imag(x_times_com_conj), real(y_times_com_conj)))
    def div_ord_com(x, y):
        return CCmethod_to_OCmethod(div_com)(x, y)
    def div_com_ord(x, y):
        return CCmethod_to_COmethod(div_com)(x, y)
    
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
    def is_eq_ord_com(x, y):
        return CCmethod_to_OCmethod(is_eq_com)(x, y)
    def is_eq_com_ord(x, y):
        return CCmethod_to_COmethod(is_eq_com)(x, y)
    # is_eq_com: (RepCom, RepCom) -> Boolean
    
    put("make","complex", make_com)
    put("add",("complex","complex"), add_com)
    put("add",("ordinary","complex"), add_ord_com)
    put("add",("complex","ordinary"), add_com_ord)
    put("sub",("complex","complex"), sub_com)
    put("sub",("ordinary","complex"), sub_ord_com)
    put("sub",("complex","ordinary"), sub_com_ord)
    put("mul",("complex","complex"), mul_com)
    put("mul",("ordinary","complex"), mul_ord_com)
    put("mul",("complex","ordinary"), mul_com_ord)
    put("div",("complex","complex"), div_com)
    put("div",("ordinary","complex"), div_ord_com)
    put("div",("complex","ordinary"), div_com_ord)
    put("negate",("complex",), negate)
    put("is_zero_com",("complex",), is_zero_com)
    put("is_equal",("complex","complex"), is_eq_com)
    put("is_equal",("ordinary","complex"), is_eq_ord_com)
    put("is_equal",("complex","ordinary"), is_eq_com_ord)
    
install_complex_package()


def create_complex(x,y):
    return get("make","complex")(x,y)


#################
# Do not change #
#################

n3 = create_ordinary(3)
r3_1 = create_rational(create_ordinary(3), create_ordinary(1))
r2_7 = create_rational(create_ordinary(2), create_ordinary(7))

def gradeThis_rational_package():
    rationalA = is_equal(n3, r3_1)
    rationalB = is_equal(sub(add(n3, r2_7), r2_7), n3)
    if rationalA and rationalB:
        print("Well done! Your install_rational_package is complete!")
    else:
        print("Please check your solution for install_rational_package.")


n3 = create_ordinary(3)
c3_plus_0i = create_complex(create_ordinary(3), create_ordinary(0))
c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))

def gradeThis_complex_package():
    complexA = is_equal(n3, c3_plus_0i)
    complexB = is_equal(sub(add(n3, c2_plus_7i), c2_plus_7i), n3)
    if complexA and complexB:
        print("Well done! Your install_complex_package is complete!")
    else:
        print("Please check your solution for install_complex_package.")

gradeThis_rational_package()
gradeThis_complex_package()
