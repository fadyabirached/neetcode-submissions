class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
             rowChecker = set()
             for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rowChecker:
                    return False
                    
                rowChecker.add(board[i][j])

        for i in range(len(board)):
             colChecker = set()
             for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in colChecker:
                    return False
                    
                colChecker.add(board[j][i]) 

        for boxRow in range(0,9,3):
            for boxCol in range(0,9,3):
                boxChecker = set()

                for i in range(3):
                   for j in range(3):
                        if board[boxRow+ i][boxCol+j] == '.' :
                            continue
                        if board[boxRow+ i][boxCol+j] in boxChecker:
                            return False
                        boxChecker.add(board[i+boxRow][j+boxCol])

        return True

        


        
        