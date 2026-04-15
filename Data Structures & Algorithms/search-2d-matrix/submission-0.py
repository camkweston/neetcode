class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        

        def find_row():
            candidate_row = 0
            candidate_row_first_val = matrix[0][0]

            l = 0
            r = len(matrix)

            while l < r:
                mid = (l + r) // 2

                if matrix[mid][0] <= target:
                    if matrix[mid][0] > candidate_row_first_val:
                        candidate_row_first_val = matrix[mid][0]
                        candidate_row = mid

                    l = mid + 1
                else:
                    r = mid
            
            return candidate_row
        


        target_row = find_row()
        print("Target row: ", target_row)

        if matrix[target_row][0] > target:
            return False
        elif matrix[target_row][0] == target:
            return True
        else:
            l = 0
            r = len(matrix[target_row])

            while l < r:
                mid = (l + r) // 2
                print(matrix[target_row][mid])

                if matrix[target_row][mid] == target:
                    return True
                elif matrix[target_row][mid] < target:
                    l = mid + 1
                else:
                    r = mid
            
            return False







