class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 27 sets in total, 9 row, 9 col, 9 boxes

        #adding to sets and checking against them as we loop through the rows 
        #so that we don't have to ever look at the same box again.

        #need a way to track which set we are on of the 3 groups
        rowSets = []
        columnSets = []
        boxSets = []
        for i in range(9):
            boxSets.append(set())
        boxCounter = 1
        for row in range(9):
            rowSets.append(set())
            for col in range(9):
                item = board[row][col]
                if row == 0:
                    columnSets.append(set())
               
                boxCounter+=1
                if (col < 3):
                    if (row < 3):
                        boxIndex = 0
                    elif (row < 6):
                        boxIndex = 3
                    else:
                        boxIndex = 6
                elif (col < 6):
                    if (row < 3):
                        boxIndex = 1
                    elif (row < 6):
                        boxIndex = 4
                    else:
                        boxIndex = 7
                else:
                    if (row < 3):
                        boxIndex = 2
                    elif (row < 6):
                        boxIndex = 5
                    else:
                        boxIndex = 8

                if (item != "."):
                    if (item in rowSets[row] or item in columnSets[col] or item in boxSets[boxIndex]):
                        return False
                    rowSets[row].add(board[row][col])
                    columnSets[col].add(board[row][col])
                    boxSets[boxIndex].add(board[row][col])
        return True

                

        