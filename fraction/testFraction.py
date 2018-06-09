from fraction import Fraction

myf = Fraction(3,5)
myf.show()
print(myf)
print("I ate ", myf, " pizza")

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
f4 = Fraction(3, 6)

f3 = f1 + f2
print(f3)
print(f1 == f4)

print("Subtraction")
print(f1 - f2)
print(f2 - f1)

print(f1, "<", f4, f1 < f4)
print(f1, ">", f4, f1 > f4)
print(f4, "*", f2, f4 * f2)
print(f1, "/", f2, f1 / f2)
