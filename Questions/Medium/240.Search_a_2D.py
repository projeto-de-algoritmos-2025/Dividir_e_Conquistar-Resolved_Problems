from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_submatrix(top, bottom, left, right):
            if top > bottom or left > right:
                return False
            
            mid_row = (top + bottom) // 2
            mid_col = (left + right) // 2
            pivot = matrix[mid_row][mid_col]
            
            if pivot == target:
                return True
            elif pivot < target:
                # Descarta parte superior esquerda
                return (
                    search_submatrix(mid_row + 1, bottom, left, right) or   # abaixo
                    search_submatrix(top, bottom, mid_col + 1, right)       # à direita
                )
            else:
                # Descarta parte inferior direita
                return (
                    search_submatrix(top, mid_row - 1, left, right) or      # acima
                    search_submatrix(top, bottom, left, mid_col - 1)        # à esquerda
                )
        
        if not matrix or not matrix[0]:
            return False
        
        return search_submatrix(0, len(matrix) - 1, 0, len(matrix[0]) - 1)
