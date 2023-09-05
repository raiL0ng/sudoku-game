from typing import List

class Field:

    def __init__(self) -> None:
        # self.rows = []
        # self.colums = []
        # self.boxes = []
        self.board = []
    
    def isValidSudoku(self) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != '.':
                    if self.board[i][j] in rows[i]:
                        return False
                    rows[i].add(self.board[i][j])
                    if self.board[i][j] in columns[j]:
                        return False
                    columns[j].add(self.board[i][j])
                    indx = (i // 3) * 3 + (j // 3)
                    if self.board[i][j] in boxes[indx]:
                        return False
                    boxes[indx].add(self.board[i][j])
        return True
    

if __name__ == '__main__':
    c = Field()
    