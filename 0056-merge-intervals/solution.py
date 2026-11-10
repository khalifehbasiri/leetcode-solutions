class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        results = []

        for interval in intervals:
            if not results or results[-1][1] < interval[0]:
                results.append(interval)
            else:
                results[-1][1] = max(results[-1][1], interval[1])

        return results