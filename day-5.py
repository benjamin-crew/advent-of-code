def map_points(coords_list, grid):
    for line in range(len(coords_list)):
        
        y1 = int(coords_list[line][0][0])
        y2 = int(coords_list[line][1][0])
        x1 = int(coords_list[line][0][1])
        x2 = int(coords_list[line][1][1])

        print(f"Num: {line}, {y1}, {x1} -> {y2}, {x2}")

        # Map horizontals
        if y1 == y2:

            if x1 < x2:
                for num in range(x1, x2+1):
                    grid[num][y1] += 1

            elif x1 > x2:
                for num in range(x2, x1+1):
                    grid[num][y1] += 1
            
            # Map singles
            else:
                grid[x1][y1] += 1
         
        # Map verticals
        elif x1 == x2:

            if y1 < y2:
                for num in range(y1, y2+1):
                    grid[x1][num] += 1

            elif y1 > y2:
                for num in range(y2, y1+1):
                    grid[x1][num] += 1
            

        
        # Map diagonals
        else:
            y_distance = abs(y1-y2)
            x_distance = abs(x1-x2)

            if x_distance == y_distance:
                if y1 < y2:
                    # Down-right diag
                    if x1 < x2:
                        for num in range(x1, x2+1):
                            grid[y1][num] += 1
                            y1 += 1

                    # Down-left diag
                    elif x1 > x2:
                        for num in range(y2, y1-1, -1):
                            grid[x2][num] += 1
                            x2 += 1
                elif y1 > y2:
                    # Up-right diag
                    if x1 < x2:
                        for num in range(x1, x2+1):
                            grid[y1][num] += 1
                            y1 -= 1
                    # Up-left diag
                    elif x1 > x2:
                        for num in range(x1+1, x2, -1):
                            grid[num-1][y1] += 1
                            y1 -= 1


def create_grid(y, x):
    grid = []
    y_axis = []
    x_axis = []

    for i in range(x):
        x_axis.append(0)

    for y in range(y):
        grid.append(x_axis.copy())

    return(grid)

def get_y(coords_list):

    y = 0
    for num in range(len(coords_list)):
        if int(coords_list[num][0][0]) > y:
            y = int(coords_list[num][0][0])

        if int(coords_list[num][1][0]) > y:
            y = int(coords_list[num][1][0])

    return(y+2)

def get_x(coords_list):
    
    x = 0
    for num in range(len(coords_list)):
        if int(coords_list[num][0][1]) > x:
            x = int(coords_list[num][0][1])

        if int(coords_list[num][1][1]) > x:
            x = int(coords_list[num][1][1])

    return(x+2)


### Import data
filename = 'day-5-coords.txt'
with open(filename) as coords_txt:
    coords_list = [[line_segments.strip().split(",") for line_segments in vent_lines.split('->')] for vent_lines in coords_txt.read().split('\n')]

# Create and populate grid
y = get_y(coords_list)
x = get_x(coords_list)
grid = create_grid(y, x)

print(f"y={len(grid)}, x={len(grid[0])}")
map_points(coords_list, grid)

# See where lines overlap
overlapping_lines = 0
for row in grid:
    for num in row:
        if num > 1:
            overlapping_lines += 1

print(f"Overlapping Lines: {overlapping_lines}")