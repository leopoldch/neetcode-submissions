class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        lenI = len(heights)
        lenJ = len(heights[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        reacheablePacific = set()
        reacheableAtlantic = set()

        def isInGrid(i,j):
            return (0<=i<lenI) and (0<=j<lenJ) 

        def explore(i, j, reacheableSet):
            if (i,j) in reacheableSet:
                return
            
            if not isInGrid(i,j):return

            reacheableSet.add((i,j))
            currentValue = heights[i][j]

            for di, dj in directions:
                if not isInGrid(i+di,j+dj):
                    continue
                if heights[i+di][j+dj] >= currentValue:
                    # water can flow 
                    explore(i+di, j+dj, reacheableSet)

        for i in range(lenI):
            explore(i,0, reacheablePacific)
            explore(i,lenJ-1, reacheableAtlantic)

        for j in range(lenJ):
            explore(0, j, reacheablePacific)
            explore(lenI-1, j, reacheableAtlantic)

        results = []

        for item in reacheablePacific:
            if item in reacheableAtlantic:
                results.append(item)

        return results


