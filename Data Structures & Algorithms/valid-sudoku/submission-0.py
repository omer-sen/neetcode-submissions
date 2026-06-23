class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for y in range(9):
            for x in range(9):
                val = board[y][x]
                if val == ".":
                    continue

                box = (y // 3) * 3 + (x // 3)

                if val in rows[y] or val in cols[x] or val in boxes[box]:
                    return False

                rows[y].add(val)
                cols[x].add(val)
                boxes[box].add(val)

        return True
    

