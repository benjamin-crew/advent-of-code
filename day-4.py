from puzzles import day4_draw as draw

# --- Day 4: Giant Squid ---
# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# Finally, 24 is drawn:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

# --- Part Two ---
# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

def check_winner(board, drawn_numbers, last_drawn):
    board_score = 0
    for row in board:
        for number in row:
            if number not in drawn_numbers:
                board_score += (int(number))

    print(f"Answer = {board_score * int(last_drawn)}")

def solution_two(filename):
    # Open the file and then use list comprehension to make a list of list of lists. Boards > Board > Row
    with open(filename) as boards_txt:
        boards = [[row.split() for row in board.split('\n')] for board in boards_txt.read().strip().split('\n\n')]

    winning_boards = []
    drawn_numbers = []

    while len(winning_boards) < 100:

        # Draw from draw, remove and append it to drawn_numbers
        if len(draw) > 0:
            drawn_numbers.append(str(draw.pop(0)))

            # If more than 4, you can start looking for winners
            if len(drawn_numbers) > 4:
                
                for board in boards:

                    # Check columns
                    i = 0
                    j = 0
                    line = 0

                    while j < 5:
                        if board[i][j] in drawn_numbers:
                            i += 1
                        else:
                            i = 0
                            j += 1
                        if i == 5:
                            print(f"Winning Column: {board[0][j]}, {board[1][j]}, {board[2][j]}, {board[3][j]}, {board[4][j]} ")
                            if board not in winning_boards:
                                winning_boards.append(board)
                            j = 6

                    # Check rows
                    for row in board:
                        line = 0
                        for number in drawn_numbers:
                            if number in row:
                                line += 1
                            if line == 5:
                                print(f"Winning Row: {row}")
                                if board not in winning_boards:
                                  winning_boards.append(board)
                                  break
                                else:
                                    break
        print(f"winning boards: {len(winning_boards)}")

        
    if len(winning_boards) == 100:

        board = winning_boards[-1]

        # Check columns
        i = 0
        j = 0
        line = 0

        while j < 5:
            if board[i][j] in drawn_numbers:
                i += 1
            else:
                i = 0
                j += 1
            if i == 5:
                print(f"Losing Column: {board[0][j]}, {board[1][j]}, {board[2][j]}, {board[3][j]}, {board[4][j]} ")
                last_drawn = drawn_numbers[-1]
                check_winner(board, drawn_numbers, last_drawn)
                return

        # Check rows
        for row in board:
            line = 0
            for number in drawn_numbers:
                if number in row:
                    line += 1
                if line == 5:
                    print(f"Losing Row: {row}")
                    last_drawn = drawn_numbers[-1]
                    check_winner(board, drawn_numbers, last_drawn)
                    return

def solution_one(filename):

    # Open the file and then use list comprehension to make a list of list of lists. Boards > Board > Row
    with open(filename) as boards_txt:
        boards = [[row.split() for row in board.split('\n')] for board in boards_txt.read().strip().split('\n\n')]

    drawn_numbers = []
    winner = False

    while winner is False:
        if len(draw) > 0:
            # Draw from draw, remove and append it to drawn_numbers
            drawn_numbers.append(str(draw.pop(0)))

            if len(drawn_numbers) > 4:
                
                for board in boards:
                    
                    # Check columns
                    i = 0
                    j = 0
                    line = 0

                    while j < 5:
                        if board[i][j] in drawn_numbers:
                            i += 1
                        else:
                            i = 0
                            j += 1
                        if i == 5:
                            print(f"Winning Column: {board[0][j]}, {board[1][j]}, {board[2][j]}, {board[3][j]}, {board[4][j]} ")
                            last_drawn = drawn_numbers[-1]
                            check_winner(board, drawn_numbers, last_drawn)

                            winner = True
                            return

                    # Check rows
                    for row in board:
                        line = 0
                        for number in drawn_numbers:
                            if number in row:
                                line += 1
                            if line == 5:
                                print(f"Winning Row: {row}")
                                last_drawn = drawn_numbers[-1]
                                check_winner(board, drawn_numbers, last_drawn)
                                
                                winner = True
                                return
                
        else:
            print("run out of numbers")
            return


filename = 'day-4-boards.txt'

# solution_one(filename)
solution_two(filename)
print("returned")