class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        lenx = len(grid[0])
        leny = len(grid)

        number_of_island = 0

        def remove_surrounding(x: int, y:int):
            # x + 1 ; x - 1
            # y + 1; y - 1
            vals = [-1, 1]
            for val in vals:
                if x+val >= 0 and x+val <= lenx-1:
                    if grid[y][x+val] == "1":
                        grid[y][x+val] = "0"
                        remove_surrounding(x+val,y )
                if y+val >= 0 and y+val <= leny-1:
                    if grid[y+val][x] == "1":
                        grid[y+val][x] = "0"
                        remove_surrounding(x, y+val)
            return                

        for y in range(leny):
            for x in range(lenx):
                if grid[y][x] == "0":
                    continue
                else:
                    number_of_island +=1
                    remove_surrounding(x, y)
        
        return number_of_island

