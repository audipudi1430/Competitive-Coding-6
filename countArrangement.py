# Approach:
# - Use Backtracking to try placing each number at each position based on divisibility conditions.
# - For a valid placement (i % index == 0 or index % i == 0), mark the number as visited and recurse.
# - Backtrack by unmarking after exploring each possibility.
#
# Time Complexity: O(n!), since in the worst case we try almost all permutations (but pruning reduces some).
# Space Complexity: O(n), for the visited array and recursion stack depth.

class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        visited = [False] * (n + 1)

        def backtrack(index):
            nonlocal count
            if index > n:
                count += 1
                return
            for i in range(1, n + 1):
                if not visited[i] and (i % index == 0 or index % i == 0):
                    visited[i] = True
                    backtrack(index + 1)
                    visited[i] = False

        backtrack(1)
        return count
