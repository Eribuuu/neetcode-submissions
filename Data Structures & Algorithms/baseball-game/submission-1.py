class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        total = 0
        for char in operations:
            if char == '+':
                last = results.pop()
                first = results.pop()
                add = last + first
                results.append(first)
                results.append(last)
                results.append(add)
            elif char == 'D':
                last = results.pop()
                double =  last * 2
                results.append(last)
                results.append(double)
            elif char == 'C':
                results.pop()
            else:
                results.append(int(char))
        for score in results:
            total += score
        return total
