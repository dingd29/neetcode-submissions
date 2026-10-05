class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n = len(matrix[0])
        upperRow=0
        lowerRow=m-1
        midrow = 0
        while upperRow<=lowerRow:
            midrow = upperRow + (-upperRow+lowerRow)//2
            if matrix[midrow][0] <= target <= matrix[midrow][-1]:
                break
            elif target<matrix[midrow][0]:
                lowerRow = midrow-1
            elif target>matrix[midrow][n-1]:
                upperRow = midrow+1
        upper = 0
        lower = n-1
        while upper<=lower:
            mid = upper + (-upper+lower)//2
            if matrix[midrow][mid] < target:
                upper = mid+1
            elif target < matrix[midrow][mid]:
                lower = mid-1
            else:
                return True
        return False
        
            