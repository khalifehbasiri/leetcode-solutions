class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        columns = {i: [] for i in range(9)}
        rows = {i: [] for i in range(9)}
        boxes = {(r, c): [] for r in range(3) for c in range(3)}

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
                    boxes[(i // 3, j // 3)].append(board[i][j]) 

        for elem in columns:
            if len(set(columns[elem])) != len(columns[elem]):
                return False

        for elem in rows:
            if len(set(rows[elem])) != len(rows[elem]):
                return False
        
        for elem in boxes:
            if len(set(boxes[elem])) != len(boxes[elem]):
                return False

        return True