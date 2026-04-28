class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [element for row in grid for element in row]
        arr.sort()
        if any(arr[i] % x != arr[i + 1] % x for i in range(len(arr) - 1)):
            return -1

        mid = arr[len(arr)//2]
        operations = 0
        for num in arr:
            operations += abs(num - mid) // x

        return operations
        
