# student solution
import math
import numpy as np
def largest_triangle_proof(n, radius):
    """
    Prove the pattern of largest area of a triangle that can be 
    inscribed inside a give circle. 
    
    This function returns the height of largest area of a triangle 
    that can be inscribed inside a circle with the given radius, 
    and base of the triangle is the diameter of the circle

    Args:
      radius: radius of the circle
      n: gradient

    Returns:
      height of the largest triangle
    """
    # set the centre of the circle to (0,0)
    origin_x = 0.0
    origin_y = 0.0

    #The lower this value the higher quality the circle is with more points generated
    stepSize = 180/n

    base_length = 2 * radius
    t_values = np.radians(np.arange(0.0, 180.0, stepSize))
    positions = np.array([(radius * np.cos(t_values) + origin_x, radius * np.sin(t_values) + origin_y)])
    temp_area = 0.5 * base_length * (radius * np.sin(t_values))

    return positions[0,1,np.argmax(temp_area)]

def largest_triangle_area(n, radius, h=0.0):
    """
    Returns the largest area of a triangle that can be inscribed inside a
    circle with the given radius.

    Args:
      radius: radius of the circle
      h: the starting height of triangle found after the proof of max area based on diameter as the base of triangle
      n: gradient

    Returns:
      Area of the largest inscribed triangle
    """
    h = largest_triangle_proof(n, radius)
    # The largest triangle is an equilateral triangle
    largest_A = float('-inf')
    step = radius / n
    
    for d in np.arange(0, radius, step):
        base_length = 2 * math.sqrt(radius**2 - d**2)
        area = 0.5 * base_length * (d + h)
        if d == 0:
            largest_A=area
        elif area>=largest_A:
            largest_A=area
    return largest_A

