# Name: Ashish Sadavarti
# Code: HackerRankLogoGenerator
# Code Description: Generates a text-based "HackerRank" logo pattern using
#                   Python's string alignment methods: rjust(), ljust(), and center().
# Copyright 2025

thickness = int(input()) # This must be an odd number, e.g., 5, 7, 9
c = 'H' # The character used to draw the logo

# Top Cone
# This section creates the upper triangular part of the logo.
# For each row 'i' from 0 to thickness-1:
# (c*i): Creates a string of 'H's, growing with 'i'.
# .rjust(thickness-1): Right-justifies the left part of the cone, padding with spaces on the left.
#                      This creates the ascending left slope.
# c: The single 'H' in the center of the cone's base.
# .ljust(thickness-1): Left-justifies the right part of the cone, padding with spaces on the right.
#                      This creates the ascending right slope.
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
# This section creates the two vertical pillars above the middle belt.
# For each row 'i' from 0 to thickness:
# (c*thickness): Creates a solid block of 'H's with width 'thickness'.
# .center(thickness*2): Centers the left pillar within a field of size 'thickness*2'.
# .center(thickness*6): Centers the right pillar within a wider field of size 'thickness*6'.
# These two centered strings are concatenated to form the row.
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
# This section creates the wide, central horizontal belt of the logo.
# For each row 'i' for half the thickness (rounded down if odd, then +1):
# (c*thickness*5): Creates a very wide block of 'H's (5 times the base thickness).
# .center(thickness*6): Centers this wide block within the overall width, ensuring alignment.
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
# This section is identical to the Top Pillars, creating the lower vertical pillars.
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
# Bottom Cone
# This section creates the lower, inverted triangular part of the logo.
# For each row 'i' from 0 to thickness-1:
# (thickness-i-1): Calculates the decreasing number of 'H's for the inverted triangle.
# (c*(thickness-i-1)).rjust(thickness): Right-justifies the left side of the inverted cone.
# c: The single 'H' in the center.
# (c*(thickness-i-1)).ljust(thickness): Left-justifies the right side of the inverted cone.
# The entire inverted cone part is then right-justified within a larger field
# (thickness*6) to align it correctly with the wider parts of the logo structure.
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
