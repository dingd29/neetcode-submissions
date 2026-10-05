class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each 3x3 box
            for k in range (3):
                for l in range (3):
                    dic = defaultdict(lambda: 1)
                    for i in range (3*k, 3*k+3):
                        for j in range (3*l, 3*l+3):
                            if board[i][j].isdigit():
                                dic[board[i][j]] -= 1
                                if dic[board[i][j]] == -1:
                                    return False
        #check each row:
            for i in range (9):
                dic = defaultdict(lambda: 1)
                for j in range (9):
                    if board[i][j].isdigit():
                        dic[board[i][j]] -= 1
                        if dic[board[i][j]] == -1:
                            return False
        #check each column:
            for j in range (9):
                dic = defaultdict(lambda: 1)
                for i in range (9):
                    if board[i][j].isdigit():
                        dic[board[i][j]] -= 1
                        if dic[board[i][j]] == -1:
                            return False
            return True