def map_points(coords_list, grid):
    for line in range(len(coords_list)):
        
        x1 = int(coords_list[line][0][0])
        y1 = int(coords_list[line][0][1])

        x2 = int(coords_list[line][1][0])
        y2 = int(coords_list[line][1][1])

        # Map horizontals
        if y1 == y2:

            #print(f"horizontals : ( {p1x}, {p1y} ) -> ( {p2x}, {p2y} )")

            if x1 < x2:
                for x in range(x1, x2+1):
                    grid[x][y1] += 1

            elif x1 > x2:
                for x in range(x2, x1+1):
                    grid[x][y1] += 1
            
        # Map verticals
        elif x1 == x2:

            #print(f"verticals : ( {p1x}, {p1y} ) -> ( {p2x}, {p2y} )")

            if y1 < y2:
                for y in range(y1, y2+1):
                    grid[x1][y] += 1

            elif y1 > y2:
                for y in range(y2, y1+1):
                    grid[x1][y] += 1
        
        # Map diagonals
        else:

            #print(f"diagonal : ( {p1x}, {p1y} ) -> ( {p2x}, {p2y} )")

            if y1 < y2:
                # Down-right diag
                if x1 < x2:
                    for x,y in zip(range(x1, x2+1),range(y1, y2+1)):
                        grid[x][y] += 1

                # Down-left diag
                elif x1 > x2:
                    for x,y in zip(reversed(range(x2, x1+1)),range(y1, y2+1)):
                        grid[x][y] += 1

            elif y2 < y1:
                # Up-right diag
                if x1 < x2:
                    for x,y in zip(range(x1, x2+1),reversed(range(y2, y1+1))):
                        grid[x][y] += 1

                # Up-right diag
                elif x1 > x2:
                    for x,y in zip(reversed(range(x2, x1+1)),reversed(range(y2, y1+1))):
                        grid[x][y] += 1


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