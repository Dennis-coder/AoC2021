def get_sets(board):
    rows = [set([board[0][0], board[0][1], board[0][2], board[0][3], board[0][4]]),
            set([board[1][0], board[1][1], board[1][2], board[1][3], board[1][4]]),
            set([board[2][0], board[2][1], board[2][2], board[2][3], board[2][4]]),
            set([board[3][0], board[3][1], board[3][2], board[3][3], board[3][4]]),
            set([board[4][0], board[4][1], board[4][2], board[4][3], board[4][4]])]
    cols = [set([board[0][0], board[1][0], board[2][0], board[3][0], board[4][0]]),
            set([board[0][1], board[1][1], board[2][1], board[3][1], board[4][1]]),
            set([board[0][2], board[1][2], board[2][2], board[3][2], board[4][2]]),
            set([board[0][3], board[1][3], board[2][3], board[3][3], board[4][3]]),
            set([board[0][4], board[1][4], board[2][4], board[3][4], board[4][4]])]
    diags = [set([board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]]), 
             set([board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]])]
    return ((*rows,), (*cols,), (*diags,))

def refactor_indata(indata):
    numbers, *boards = indata.split("\n\n")
    numbers = (*[int(x) for x in numbers.split(",")],)
    boards = (*[get_sets((*[(*[int(x) for x in row.split()],) for row in y.split("\n")],)) for y in boards],)
    return (numbers, boards)

def calc_a(bingo_data):
    numbers, boards = bingo_data
    low = 4
    high = len(numbers) - 1
    while low != high:
        mid = (high + low) // 2
        used_numbers = set(numbers[:mid])
        new_boards = []
        for (rows, cols, diags) in boards:
            bingo = False
            for row in rows:
                if row.issubset(used_numbers):
                    bingo = True
                    break
            for col in cols:
                if col.issubset(used_numbers):
                    bingo = True
                    break
            if bingo:
                new_boards.append((rows, cols, diags))
        if len(new_boards) > 0:
            high = mid    
            boards = new_boards
        else:
            low = mid + 1
    used_numbers = set(numbers[:mid + 1])
    unmarked_sum = sum([sum(row.difference(used_numbers)) for row in boards[0][0]])
    return unmarked_sum * numbers[mid]


def calc_b(bingo_data):
    numbers, boards = bingo_data
    low = 4
    high = len(numbers) - 1
    while low != high:
        mid = (high + low) // 2
        used_numbers = set(numbers[:mid])
        new_boards = []
        for (rows, cols, diags) in boards:
            bingo = False
            for row in rows:
                if row.issubset(used_numbers):
                    bingo = True
                    break
            for col in cols:
                if col.issubset(used_numbers):
                    bingo = True
                    break
            for diag in diags:
                if diag.issubset(used_numbers):
                    bingo = True
                    break
            if not bingo:
                new_boards.append((rows, cols, diags))
        if len(new_boards) > 0:
            low = mid + 1
            boards = new_boards
        else:
            high = mid    
    used_numbers = set(numbers[:mid + 1])
    unmarked_sum = sum([sum(row.difference(used_numbers)) for row in boards[0][0]])
    return unmarked_sum * numbers[mid]