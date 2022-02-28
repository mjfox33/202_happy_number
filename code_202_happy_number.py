class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(n):
            result = 0  
            for x in str(n):
                result += pow(int(x), 2)
            return result
        
        slow = digit_square_sum(n)
        fast = digit_square_sum(digit_square_sum(n))
        
        while slow != fast:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(digit_square_sum(fast))

        return 1 if slow == 1 else 0