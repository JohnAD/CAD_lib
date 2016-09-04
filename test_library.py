#!python3
from CAD_lib.geometry import Point, LineString, Line

print("Testing CAD_lib...")


print("  Testing Point")

pA = Point((1,2,3))
assert pA.coords==[(1.0, 2.0, 3.0)]

pB = Point(4, 5, 6)
assert pB.coords==[(4.0, 5.0, 6.0)]

pC = Point(2.0, -5)
assert pC.coords==[(2.0, -5.0)]


print("  Testing Line")

lnA = Line(pA, pB)
assert str(lnA)=="Line [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)]"

lnB = Line(pB, (-3, 99, 12.345))
assert str(lnB)=="Line [(4.0, 5.0, 6.0), (-3.0, 99.0, 12.345)]"
assert lnB.coord==[(4.0, 5.0, 6.0), (-3.0, 99.0, 12.345)]


print("  Testing LineString")

lsA = LineString([pA, pB, pC])
assert str(lsA)=="LineString [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (2.0, -5.0)]"

lsB = LineString([(0, 0), (1, 1), (2,1), (2,2)])
assert str(lsB)=="LineString [(0.0, 0.0), (1.0, 1.0), (2.0, 1.0), (2.0, 2.0)]"

print("Testing complete.")