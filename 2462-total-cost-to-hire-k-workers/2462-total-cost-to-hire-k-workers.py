import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, c: int) -> int:
        n = len(costs)

        left = []
        right = []

        i = 0
        j = n - 1

        for _ in range(c):
            if i <= j:
                heapq.heappush(left, (costs[i], i))
                i += 1

        for _ in range(c):
            if i <= j:
                heapq.heappush(right, (costs[j], j))
                j -= 1

        s1 = 0

        for _ in range(k):
            if not right:
                val, ind = heapq.heappop(left)
                s1 += val
                if i <= j:
                    heapq.heappush(left, (costs[i], i))
                    i += 1

            elif not left:
                val, ind = heapq.heappop(right)
                s1 += val
                if i <= j:
                    heapq.heappush(right, (costs[j], j))
                    j -= 1

            else:
                if left[0] <= right[0]:
                    val, ind = heapq.heappop(left)
                    s1 += val
                    if i <= j:
                        heapq.heappush(left, (costs[i], i))
                        i += 1
                else:
                    val, ind = heapq.heappop(right)
                    s1 += val
                    if i <= j:
                        heapq.heappush(right, (costs[j], j))
                        j -= 1

        return s1