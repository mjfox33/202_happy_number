from code_202_happy_number import Solution

def test_example_1():
    s = Solution()
    n = pow(2,30)
    output = False
    assert s.isHappy(n) == output

def test_example_2():
    s = Solution()
    n = 2
    output = False
    assert s.isHappy(n) == output
