class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        low= 0 
        high= len(mat[0])-1
        m=high

        def findrow(mat, col):
            x= len(mat)
            maxi= float('-inf')
            ind= 0
            
            for i in range(x):
                if mat[i][col]> maxi:
                    maxi= mat[i][col]
                    ind= i
            return ind

        while low<=high:
            col=(low+high)//2
            row=findrow(mat, col)

            left= mat[row][col-1] if col-1>= 0 else float('-inf')
            right= mat[row][col+1] if col+1< m+1 else float('-inf')

            if mat[row][col]> left and mat[row][col]> right:
                return [row, col]
            elif mat[row][col] > left:
                low= col+1
            else:
                high= col-1

        return -1


        