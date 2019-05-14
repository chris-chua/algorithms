"""Google interview question

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

"""
Solution: 
Take a 1 by 1 unit square and fit circle touching the sides of the square.

Area of circle / Area of square 
= #points in circle / #points generated

pi(1/2)^2 / (1^2)
= #points in circle / #points generated

pi/4
= #points in circle / #points generated

pi = 4 * #points in circle / #points generated

Check if random points (x, y) satisfy x^2 + y^2 <= 1
"""

import random

def estimate_pi(n):
    """
    Args:
    n: number of Monte Carlo trials

    Output:
    value of pi
    """
    circle_points = 0

    for _ in range(n):
        
        x = random.random()
        y = random.random()

        distance = (x ** 2) + (y ** 2)
        if distance <= 1:
            circle_points += 1
    
    pi = circle_points / n * 4
    return pi

if __name__ == '__main__':    
    print(estimate_pi(1000000))