class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = False
        cols = []
        subs = []
        i = 0
        j = 0
        while i < len(board):
            co = []
            j = 0
            while j < len(board[i]):
                co.append(board[j][i])
                j += 1
            cols.append(co)
            i += 1
        for row in board:
            for i in range(len(row) - 1):
                # print(f"searching for {row[i]} in {row[i + 1:]}")
                if row[i] in row[i + 1:] and row[i] != ".":
                    return False
        for col in cols:
            # print(f"searching for {col[0]} in {col[1:]}")
            for j in range(len(col) - 1):
                if col[j] in col[j + 1:] and col[j] != ".":
                    return False
        k_s = 0
        for cs in [0, 3, 6]:
            for i in [0, 3, 6]:
                print(f"i at {i}")
                sub = []
                for j in range(i, i + 3):
                    print(f"j at : {j}")
                    for k in range(cs, cs + 3):
                        print(f"k  at: {k}")
                        print(f"adding {board[j][k]} to {sub}")
                        sub.append(board[j][k])
                    
                subs.append(sub)
        for grid in subs:
            for i in range(len(grid) - 1):
                if grid[i] in grid[i + 1:] and grid[i] != ".":
                    return False
        print(subs)        
        return True
