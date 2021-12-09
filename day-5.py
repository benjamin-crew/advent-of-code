import math

# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

# An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

# An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....
# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

# Consider all of the lines. At how many points do at least two lines overlap?

def map_points(coords_list, grid):
    for line in range(len(coords_list)):
        
        y1 = int(coords_list[line][0][0])
        y2 = int(coords_list[line][1][0])
        x1 = int(coords_list[line][0][1])
        x2 = int(coords_list[line][1][1])

        print(f"Num: {line}, {x1}, {y1} -> {x2}, {y2}")

        # Map horizontals
        if x1 == x2:

            if y1 < y2:
                # print(list(range(y1, y2+1)))
                for num in range(y1, y2+1):
                    # print(num)
                    print(f"x1={x1}, num={num}")
                    print(grid[x1][num])
                    grid[x1][num] += 1

            elif y2 < y1:
                # print(list(range(y2, y1+1)))
                for num in range(y2, y1+1):
                    # print(num)
                    grid[x1][num] += 1

            # Map singles
            else:
                grid[x1][y1] += 1
        
        # Map verticals
        elif y1 == y2:
            
            if x1 < x2:
                # print(list(range(x1, x2+1)))
                for num in range(x1, x2+1):
                    grid[num][y1] += 1

            if x2 < x1:
                # print(list(range(y2, y1+1)))
                for num in range(x2, x1+1):
                    grid[num][y1] += 1
        
        # Map diagonals
        else:
            x_distance = abs(x1-x2)
            y_distance = abs(y1-y2)

            # Think this one works
            if x_distance == y_distance:
                if y1 < y2:
                    if x1 < x2:
                        for num in range(y1, y_distance+1):
                            print(num)
                            grid[y1][num] += 1
                            y1 += 1

                if y1 > y2:
                    pass

                
            else:
                pass

    return(grid)
                

def create_grid(x, y):
    grid = []
    x_axis = []
    y_axis = []

    for i in range(x):
        x_axis.append(0)

    for y in range(y):
        grid.append(x_axis.copy())

    return(grid)

def get_x(coords_list):

    x = 0
    for num in range(len(coords_list)):
        if int(coords_list[num][0][0]) > x:
            x = int(coords_list[num][0][0])

        if int(coords_list[num][1][0]) > x:
            x = int(coords_list[num][1][0])

    return(x+1)

def get_y(coords_list):
    
    y = 0
    for num in range(len(coords_list)):
        if int(coords_list[num][0][1]) > y:
            y = int(coords_list[num][0][1])

        if int(coords_list[num][1][1]) > y:
            y = int(coords_list[num][1][1])

    return(y+1)

### Import data
filename = 'day-5-coords.txt'
with open(filename) as coords_txt:
    coords_list = [[line_segments.strip().split(",") for line_segments in vent_lines.split('->')] for vent_lines in coords_txt.read().split('\n')]
###

# Create and populate grid
x = get_x(coords_list)
y = get_y(coords_list)
grid = create_grid(x, y)

print(f"x={len(grid[0])}, y={len(grid)}")
map_points(coords_list, grid)

# See where lines overlap
overlapping_lines = 0
for row in grid:
    print(row)
    for num in row:
        if num > 1:
            overlapping_lines += 1

print(f"Overlapping Lines: {overlapping_lines}")