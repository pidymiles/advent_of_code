# target area: x=25..67, y=-260..-200
"""
The subject of eigenanalysis seeks to find a coordinate system, in which
the solution to an applied problem has a simple expression.
"""
"""
 ⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼
⎟VECTORS AND LINEAR ALGEBRA⎟
 ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
The target area is a 2-D rectangle, it has a vertical vector and a horizontal vector
Each vector represents the magnitude (length) of the rectangles edges

     ⎡25⎤        ⎡-260⎤
 x⃗ = ⎣67⎦    y⃗ = ⎣-200⎦

To solve this problem faster, we need to know if the two vectors, x⃗ & y⃗ are linear independent or dependent

   ⎡25⎤      ⎡-260⎤   ⎡0⎤
c1*⎣67⎦ + c2*⎣-200⎦ = ⎣0⎦

Simplified...

(25*c1) + (-260*c2) = 0
    c1 + (-10.4*c2) = 0
    
(-260*c1) + (-200*c2) = 0
    c1 + (1.3*c2) = 0 
    
Subtract both equations:
    c1 + (-10.4*c2) = 0
 -  c1 +   (1.3*c2) = 0 
⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺ 
           -11.7*c2 = 0
                 c2 = 0
           
Use c2=0 to solve for c1...
 (25*c1) + (-260*0) = 0
              25*c1 = 0
                 c1 = 0

To satisfy both of the above equations, c1 AND c2 must be equal to 0:

    if c1 OR c2 == 0; then x⃗ & y⃗ are linear dependent
>>>if c1 AND c2 == 0; then x⃗ & y⃗ are linear independent<<<

For this problem, they are linear independent and knowing this we can ignore the 3rd Dimension completely
and draw a 2D line representing the y⃗ vector (the height of the target area)

The function of this program works because the probe is underwater,
the horizontal velocity will decrease until zero and then remain constant.
The vector that we want to measure has acceleration that is non-zero, we want to focus on the y⃗ vector

Linear independence means that adding information to one vector has a redundant effect on the other
Since only one axis or vector is required to solve the problem, we can ignore the first half of the input
"""

#INPUT
y_min = -260
y_max = -200

"""
((n+1)/2) is the binomial coefficient. It represents the number of distinct pairs that can be selected from N+1 objects.
 ⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼
⎟DISPLACEMENT VARIABLE⎟
 ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
displacement = final position - initial position

Final position cannot exceed -260 or we miss the target area
displacement is equal to our y_min
d = -260 - 0
d = -260
"""

"""
 ⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼⎼
⎟TESTING INITIAL VELOCITY⎟
 ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺
Test starting velocity = y_vel
y_prime variable measures speed before hitting the target area


.............#....#............
.......#..............#........
...............................
S........................#.....
...............................
...............................
......................(y_prime)
...............................
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTT#TT
....................TTTTTTTTTTT
....................TTTTTTTTTTT
....................TTTTTTTTTTT

"""

y_vel = -y_min-1


y_prime = 0
#Calulate Apex (Triangular number sequence)
while y_vel > 0:

    y_prime += y_vel
    y_vel -= 1


print (y_prime)






