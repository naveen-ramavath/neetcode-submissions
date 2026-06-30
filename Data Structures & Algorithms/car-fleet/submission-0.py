class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        times = []

        for pos, spd in cars:
            times.append((target - pos) / spd)

        fleets = 0

        while times:
            cur = times.pop(0)
            fleets += 1

            while times and times[0] <= cur:
                times.pop(0)

        return fleets