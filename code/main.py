from random import randint


class Field:

    def __init__(self) -> None:
        self.boxes = [set() for _ in range(9)]
        self.rows = [set() for _ in range(9)]
        self.colums = [set() for _ in range(9)]
        self.board = []
        nums = randint(9, 81)
        for _ in range(nums):
            b, r, c, el = 0, 0, 0, 0
    
    def isValidSudoku(self) -> bool:
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != '.':
                    if self.board[i][j] in self.rows[i]:
                        return False
                    self.rows[i].add(self.board[i][j])
                    if self.board[i][j] in self.columns[j]:
                        return False
                    self.columns[j].add(self.board[i][j])
                    indx = (i // 3) * 3 + (j // 3)
                    if self.board[i][j] in self.boxes[indx]:
                        return False
                    self.boxes[indx].add(self.board[i][j])
        return True
    
    def addElem(self, b : int, r : int, c : int , el : str) -> bool:
        self.boxes[b].add(el)
        self.rows[r].add(el)
        self.colums[c].add(el)
        if self.isValidSudoku():
            return True
        else:
            self.boxes[b].remove(el)
            self.rows[r].remove(el)
            self.colums[c].remove(el)
            return False

if __name__ == '__main__':
    c = Field()
    