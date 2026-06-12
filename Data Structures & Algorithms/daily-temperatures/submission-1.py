class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        for i in range(len(temperatures) - 1):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    stack.append(j - i)
                    break
                elif j == (len(temperatures) - 1):
                    stack.append(0)
        stack.append(0)

        return stack