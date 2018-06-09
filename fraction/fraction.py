# Find greatest common denominator using Eucled's method
def gcd(m,n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:

    # Constructor
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        if bottom < 0:
            self.num *= -1 
            self.den *= -1 

    # Basic print
    def show(self):
        print(self.num, "/", self.den)

    # Override print method
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # Override the "+" operator
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

    # Using integer division: //
        return Fraction(newnum//common, newden//common)

    # Override == operator to enable deep equality
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
                

    # Use dir(3)  to view all methods an integer has
    # To check a particular method use
    # hasattr(3, "__sub__")
    def __sub__(self, other):
        newnum = self.num * other.den - other.num * self.den
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common) 

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum 

    def __ge__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum 

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
