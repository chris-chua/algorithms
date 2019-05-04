"""
A median on the hypotenuse divides the right angled triangle in two isoceles triangle.
Hence AM = BM = CM. 
So, ∡MCB = ∡MBC.
To find ∡MBC, use tan(∡MBC) = AB / BC.

math.atan(x)
    Return the arc tangent of x, in radians.
"""

from math import atan, degrees

ab = int(input())
bc = int(input())

print('{0:.0f}°'.format(degrees(atan(ab / bc))))