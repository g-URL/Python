xP, yP = 190, 200   # Coordinates for point P.
xA, yA, xB, yB, xC, yC = 200, 100, 100, 200, 200, 300   # Coordinates for vertices of triangle ABC.


# =============================  INFORMATION  =================================
#
# Assignment 1: Point and Triangle
# Class: CPSC 235
# By: R. Apperley
# Date: September 26th, 2016
# Scope: Program that highlights a point (P) differently depending if it is inside, outside or on triangle ABC.
#
# ============================  /INFORMATION  =================================



# ==============================  FUNCTIONS  ==================================

def triangle(x1, y1, x2, y2, x3, y3):
    '''Draws a white triangle with vertices (x1, y1, x2, y2, x3, y3).'''
    print("color", 255, 255, 255)
    print("line", x1, y1, x2, y2)
    print("line", x2, y2, x3, y3)
    print("line", x3, y3, x1, y1)


def point(xp, yp, R, G, B):
    '''Prints and highlights point (xp, yp) in RGB.'''
    print("color", R, G, B)
    print("fillcircle", xp, yp, 5)
    print("color", 255, 255, 255)
    print("line", xp, yp, xp, yp)

    
def line_check(xp, yp, x1, y1, x2, y2):
    '''Checks if point (xp, yp) is on line (x1, y1, x2, y2).'''
    if (x1 != x2):
        # y = mx + b
        m = ((y2 - y1) / (x2 - x1))
        b = y1 - (m * x1)
        if ((yP == ((m * xP) + b)) and ((xp >= min(x1, x2)) and (xp <= max(x1, x2))) and ((yp >= min(y1, y2)) and (yp <= max(y1, y2)))):     
            return True
    elif ((xp == x1) and ((yp >= min(y1, y2)) and (yp <= max(y1, y2)))):
        return True

            
def ray_line_check(xp, yp, x1, y1, x2, y2):
    '''Checks if line (x1, y1, x2, y2) is horizontal.
    Checks if the rightward horizontal ray initiated from (xp, yp) intersects line (x1, y1, x2, y2).'''
    if (x1 != x2):
        mr = 0
        m = ((y2 - y1) / (x2 - x1))
        if ((mr == m) and ((yp == y1) and (yp == y2)) and ((xp < min(x1,x2)) or (xp > max(x1,x2)))):
            return True


def ray_vertices_check(xp, yp, x1, y1, x2, y2, x3, y3):
    '''Checks if the rightward horizontal ray, initiated from (xp, yp),
    intersects the max/min vertices of triangle (x1, y1, x2, y2, x3, y3) with respect to the y axis.'''
    if ((((xp != x1) and (yp == y1)) or ((xp != x2) and (yp == y2)) or ((xp != x3) and (yp == y3))) and ((yp == max(y1,y2,y3)) or (yp == min(y1,y2,y3)))):
        return True

        
def ray_intersect_check(xp, yp, x1, y1, x2, y2):
    '''Checks if the rightward horizontal ray, initiated from (xp, yp), will intersect (x1, y1, x2, y2).'''
    if (x1 != x2):  
        # y = mx + b
        m = ((y2 - y1) / (x2 - x1))
        b = y1 - (m * x1)
        if (m != 0):
            xi = ((yp - b) / m)
            yi = ((m * xi) + b)
            if (((xi >= xp) and (xi <= max(x1, x2))) and ((yi >= min(y1, y2)) and (yi <= max(y1, y2)))):
                return True
    elif (((xp < x1) or (xp < x2)) and ((yp >= min(y1, y2)) and (yp <= max(y1, y2)))):
        return True
            
    
def main():
    '''Function that highlights a point differently if the point lies on, outside or inside the triangle.'''
    triangle(xA, yA, xB, yB, xC, yC)
    intercepts = 0
    
    # Checks if point P lies on triangle ABC.
    if ((line_check(xP, yP, xA, yA, xB, yB) == True) or (line_check(xP, yP, xB, yB, xC, yC) == True) or (line_check(xP, yP, xC, yC, xA, yA) == True)):
        point(xP, yP, 0, 0, 255)
    
    # Checks if the rightward horizontal ray, initiated from P, will intersect a horizontal AB, BC or CA.
    elif ((ray_line_check(xP, yP, xA, yA, xB, yB) == True) or (ray_line_check(xP, yP, xB, yB, xC, yC) == True) or (ray_line_check(xP, yP, xC, yC, xA, yA) == True)):
        point(xP, yP, 0, 255, 0)
    
    # Checks if the rightward horizontal ray, initiated from P, will intersect the max/min vertices of ABC with respect to the y axis.
    elif (ray_vertices_check(xP, yP, xA, yA, xB, yB, xC, yC) == True):
        point(xP, yP, 0, 255, 0)
        
    # Counts the number of times the rightward horizontal ray, initiated from P, intersects ABC.
    else:
        if (ray_intersect_check(xP, yP, xA, yA, xB, yB) == True):
            intercepts = intercepts + 1
            
        if (ray_intersect_check(xP, yP, xB, yB, xC, yC) == True):
            intercepts = intercepts + 1
                    
        if (ray_intersect_check(xP, yP, xC, yC, xA, yA) == True):
            intercepts = intercepts + 1
                
        # Checks if yP is equal to the middle vertex of ABC with respect to the y axis.
        # Checks if the rightward horizontal ray initiated from P intersects ABC 2 times.
        if ((yP in (yA, yB, yC)) and ((yP != min(yA, yB, yC)) and (yP != max(yA, yB, yC))) and (intercepts == 2)):
            intercepts = intercepts - 1
           
        # Checks if the rightward horizontal ray initiated from P intersects ABC 3 times.
        elif (intercepts == 3):
            intercepts = intercepts - 1                                  
       
        # Highlights P with a colour depending on the number of times the rightward horizontal ray, initiated from P, intersects ABC.
        # If ABC is intersected 0 or 2 times, P is outside ABC. If ABC is intersected 1 time, P is inside ABC.
        if (intercepts == 0):
            point(xP, yP, 0, 255, 0)
        
        if (intercepts == 2):
            point(xP, yP, 0, 255, 0)
        
        if (intercepts == 1):
            point(xP, yP, 255, 0, 0)
     
# =============================  /FUNCTIONS  ==================================



# ===============================  PROGRAM  ===================================

main()

# ==============================  /PROGRAM  ===================================
