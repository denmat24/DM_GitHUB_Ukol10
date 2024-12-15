from math import gcd
# Greatest Common Divisor - gcd
class Fraction:

    def __init__(self, num, den):
        # "constructor", more precisely "initializer"
        # initialize Fraction here
        # přidání objektu do instance
        self.num = num
        self.den = den

    def __repr__(self):
        # magic method for text representation
        # return Fraction as a string in `numerator/denominator` format, e.g 1/2, 3/4, 153/468 etc.
        return f"{self.num}/{self.den}"

    def normalize(self):
        # from this Fraction get normalized Fraction, return normalized Fraction
        common_div = gcd(self.num, self.den) # nalezení společného dělitele
        normalized_num = self.num // common_div # dělení čitatele
        normalized_den = self.den // common_div # dělení jmenovatele
        return Fraction(normalized_num, normalized_den) # vrácený zjednodušený zlomek

    def __eq__(self, other):
        # magic method for comparison `==`
        # compare two fractions if they are same
        # two Fractions are same if their normalized numerators and denominators are equal respectively
        self_norm = self.normalize() # čitatel po normalizaci
        other_norm = other.normalize() # jmenovatel po normalizaci
        return self_norm.num == other_norm.num and self_norm.den == other_norm.den # porovnání čitatele a jmenovatele - and

    def __lt__(self, other):
        # magic method for comparison `<`
        # compare two fractions if the first one is less than second one
        return self.num * other.den < self.den * other.num # převedení na spol. jmenovatel - není nutné dát do podmínky- porovnání pouze čitatele

    def __le__(self, other):
        # magic method for comparison `<=`
        # compare two fractions if the first one is less than or equal to the second one
        return self.num * other.den <= self.den * other.num # stejné jako výše

    def add(self, other):
        # take other Fraction, execute adding, return new Fraction with the result
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den # převedení na stejného jmenovatele a následné sečtení čitatele
        return Fraction(new_num, new_den).normalize() # nový zlomek převedený do základního tvaru

    def sub(self, other):
        # take other Fraction, execute subtraction, return new Fraction with the result
        new_num = self.num * other.den - other.num * self.den # převedení na stejného jmenovatele a následné odečtení čitatele
        new_den = self.den * other.den
        return Fraction(new_num, new_den).normalize() # nový zlomek převedený do základního tvaru

    def mul(self, other):
        # take other Fraction, execute multiplication, return new Fraction with the result
        new_num = self.num * other.num # násobení čitatelů
        new_den = self.den * other.den # násobení jmenovatelů
        return Fraction(new_num, new_den).normalize() # nový zlomek převedený do základního tvaru

    def div(self, other):
        # take other Fraction, execute division, return new Fraction with the result
        new_num = self.num * other.den # násobení čitetelem převráceného zlomku other=jmenovatel other
        new_den = self.den * other.num # násobení jmenovatelem převráceného zlomku other=čitatel other
        return Fraction(new_num, new_den).normalize() # nový zlomek převedený do základního tvaru

    def __add__(self, other):
        # magic method for operation `+`
        # same as add()
        return self.add(other)

    def __sub__(self, other):
        # magic method for operation `-`
        # same as sub()
        return self.sub(other)

    def __mul__(self, other):
        # magic method for operation `*`
        # same as mul()
        return self.mul(other)

    def __truediv__(self, other):
        # magic method for operation `/`
        # same as div()
        return self.div(other)


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""


# constructor
assert Fraction(1, 2).num == 1 and Fraction(1, 2).den == 2
print (f"constructor OK")
# repr
assert f"{Fraction(1, 2)}" == "1/2"
print (f"repr OK")
# normalization
assert Fraction(3, 6).normalize().num == 1 \
       and Fraction(3, 6).normalize().den == 2 \
       and type(Fraction(3, 6).normalize().num) is int \
       and type(Fraction(3, 6).normalize().den) is int
print (f"normalize OK")
# comparison magic
assert Fraction(1, 3) == Fraction(2, 6)
assert not(Fraction(1, 3) == Fraction(3, 1))
assert Fraction(1, 3) <= Fraction(1, 2)
assert Fraction(1, 3) < Fraction(1, 2)
print (f"comparison OK")

# operation methods
assert Fraction(1, 2).add(Fraction(1, 3)) == Fraction(5, 6)
assert Fraction(1, 2).sub(Fraction(1, 3)) == Fraction(1, 6)
assert Fraction(2, 2).mul(Fraction(1, 3)) == Fraction(1, 3)
assert Fraction(1, 2).div(Fraction(1, 3)) == Fraction(3, 2)
print (f"operations OK")
# operators magic
assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)
assert Fraction(1, 2) * Fraction(1, 3) == Fraction(1, 6)
assert Fraction(1, 2) / Fraction(1, 3) == Fraction(3, 2)
