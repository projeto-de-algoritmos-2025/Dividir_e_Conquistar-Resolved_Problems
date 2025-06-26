from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        index_arr = list(range(len(nums)))

        def merge_sort(start, end):
            if end - start <= 1:
                return
            mid = (start + end) // 2
            merge_sort(start, mid)
            merge_sort(mid, end)

            merged = []
            left_idx = start
            right_idx = mid
            inv_count = 0

            temp = []

            while left_idx < mid and right_idx < end:
                if nums[index_arr[right_idx]] < nums[index_arr[left_idx]]:
                    temp.append(index_arr[right_idx])
                    inv_count += 1
                    right_idx += 1
                else:
                    temp.append(index_arr[left_idx])
                    count[index_arr[left_idx]] += inv_count
                    left_idx += 1

            while left_idx < mid:
                temp.append(index_arr[left_idx])
                count[index_arr[left_idx]] += inv_count
                left_idx += 1

            while right_idx < end:
                temp.append(index_arr[right_idx])
                right_idx += 1

            # Coloca a ordem ordenada de volta em index_arr
            index_arr[start:end] = temp

        merge_sort(0, len(nums))
        return count
