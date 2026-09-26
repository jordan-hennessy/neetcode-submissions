class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        n = ROWS * COLS

        # we want to traverse from left to right until we hit the end or an already visited square (could also keep going until end and reduce the end by one)

        res = []

        visited = set()

        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 4

        i, j = 0, 0

        status = RIGHT

        while n != len(res):

            if status == RIGHT:
                while j < COLS and (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                    j += 1
                status = DOWN
                j -= 1
                i += 1


            if status == DOWN:
                while i < ROWS and (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                    i += 1
                status = LEFT
                i -= 1
                j -= 1

            
            if status == LEFT:
                while j >= 0 and (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                    j -= 1
                status = UP
                j += 1
                i -= 1
            
            if status == UP:
                while i >= 0 and (i, j) not in visited:
                    res.append(matrix[i][j])
                    visited.add((i, j))
                    i -= 1
                status = RIGHT
                i += 1
                j += 1

            
        return res

            

        

        


        