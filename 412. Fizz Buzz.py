from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i) for i in range(1, n + 1)]

        return arr

print(Solution.fizzBuzz(Solution, 3))