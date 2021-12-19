def read_indata():
    with open("indata.txt") as file:
        data = file.read()
    return data

def refactor_indata(indata):
    indata = indata.split("\n\n")
    indata[0] = [int(x) for x in indata[0].split(",")]
    for i in range(1,len(indata)):
        indata[i] = indata[i].split("\n")
        indata[i] = [[int(x) for x in row.split()] for row in indata[i]]
    return indata

def calc_a(indata):
    numbers = indata[0]
    boards = indata[1:]
    marked_numbers = [[] for _ in range(len(boards))]
    for num in numbers:
        for i, board in enumerate(boards):
            for row in board:
                if num not in row:
                    continue
                marked_numbers[i].append(num)
                for row in board:
                    bingo = True
                    for x in row:
                        if x not in marked_numbers[i]:
                            bingo = False
                            break
                    if bingo:
                        break
                if not bingo:
                    for j in range(len(board[0])):
                        bingo = True
                        for k in range(len(board)):
                            if board[k][j] not in marked_numbers[i]:
                                bingo = False
                                break
                        if bingo:
                            break
                if bingo:
                    unmarked_sum = sum([sum(row) for row in board]) - sum(marked_numbers[i])
                    return unmarked_sum * num
                break

def calc_b(indata):
    numbers = indata[0]
    boards = indata[1:]
    marked_numbers = [[] for _ in range(len(boards))]
    for num in numbers:
        bingo_indexes = []
        for i, board in enumerate(boards):
            for row in board:
                if num not in row:
                    continue
                marked_numbers[i].append(num)
                for row in board:
                    bingo = True
                    for x in row:
                        if x not in marked_numbers[i]:
                            bingo = False
                            break
                    if bingo:
                        bingo_indexes.append(i)
                        break
                for j in range(len(board[0])):
                    bingo = True
                    for k in range(len(board)):
                        if board[k][j] not in marked_numbers[i]:
                            bingo = False
                            break
                    if bingo:
                        bingo_indexes.append(i)
                        break
        if len(boards) > 1 and len(bingo_indexes) > 0:
            new_boards = []
            new_marked_numbers = []
            for i in range(len(boards)):
                if i not in bingo_indexes:
                    new_boards.append(boards[i])
                    new_marked_numbers.append(marked_numbers[i])
            boards = new_boards
            marked_numbers = new_marked_numbers
        elif len(boards) == 1 and bingo:
            unmarked_sum = sum([sum(row) for row in boards[0]]) - sum(marked_numbers[0])
            return unmarked_sum * num
                    
def main():
    indata = read_indata()
    indata = refactor_indata(indata)
    a = calc_a(indata)
    b = calc_b(indata)
    print(a,b)

if __name__ == "__main__":
    main()