class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        n = len(position)
        stack = []

        posSpeed = list(zip(position, speed))
        posSpeed = sorted(posSpeed, reverse=True)


        for i in range(n):
            time = (target - posSpeed[i][0]) / posSpeed[i][1]            
            
            if not stack or time > stack[-1]:
                stack.append(time)
                

        return len(stack)




                
            

            

            