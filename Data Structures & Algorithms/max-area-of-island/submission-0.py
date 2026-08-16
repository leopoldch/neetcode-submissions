class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        maxArea = 0
        rowLength = len(grid)
        colLength = len(grid[0])

        def exploreIsland(i, j , visitedCells):
            if not (0<=i<=rowLength-1) or not (0<=j<=colLength-1):
                return 0                
            
            paddings = [[0,1], [1,0], [0,-1], [-1,0]]

            visitedCells.add((i,j))
            areaExplored = 1

            for paddingI, paddingJ in paddings:

                if not (0<=i+paddingI<=rowLength-1) or not (0<=j+paddingJ<=colLength-1):
                    continue
    
                if (i+paddingI, j+paddingJ) in visitedCells:
                    continue
                
                if grid[i+paddingI][j+paddingJ] == 1:
                    localAreaExplore = exploreIsland(i+paddingI, j+paddingJ, visitedCells)
                    areaExplored += localAreaExplore
            
            return areaExplored

        
        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] ==1:
                    visitedCells = set()
                    # explore the island
                    visitedCells.add((i,j))
                    islandArea = exploreIsland(i, j, visitedCells)
                    maxArea = max(maxArea, islandArea)
        
        return maxArea