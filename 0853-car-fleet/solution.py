class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) 
        print(cars)       
        stack = []

        for car in cars:
            time = (target - car[0]) / car[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        print(stack)
        return len(stack)



