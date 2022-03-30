class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        output = [intervals[0]]
        for e in intervals[1:]:
            if output[-1][0] <= e[0] <= output[-1][-1]:
                output[-1][-1] = max(output[-1][-1], e[-1])
            else:
                output.append(e)
                
        return output
