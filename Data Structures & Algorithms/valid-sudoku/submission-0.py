from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            
        for col_i in range(9):
            local_set = set()

            for row_i in range(9):
                if board[row_i][col_i] == ".": continue
                if board[row_i][col_i] in local_set:
                    return False
                local_set.add(board[row_i][col_i])

                counter_row = Counter(board[row_i])
                for key,val in counter_row.items():
                    if key == ".":continue
                    if val > 1:
                        return False
        
        paddings = [0,1,2]
        for i in range(0,9,3):
            paddings_x = [i+pad for pad in paddings]
            for j in range(0,9,3):
                paddings_y = [j+pad for pad in paddings]
                local_set = set()
                for i in paddings_x:
                    for j in paddings_y:
                        if board[i][j] == '.': continue
                        if board[i][j] in local_set:
                            return False
                        local_set.add(board[i][j])
        return True


            