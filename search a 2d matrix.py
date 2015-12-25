class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        aux=[]
        for i in matrix:
            aux=aux+i
        left=0
        right=len(aux)-1
        mid=(left+right)/2
        while aux[mid]!=target:
            if aux[mid]<target:
                left=mid+1
            elif aux[mid]>target:
                right=mid-1
            if left>right:
                return False
            mid=(left+right)/2
        return True
