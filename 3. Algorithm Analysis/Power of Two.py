# LeetCode 231

# 1
def isPowerOfTwo(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n = n/2
    if n == 1:
        return True
    else:
        return False

# 2
def isPowerOfTwo(n):
    if n == 0:
        return False
    diff_bits = n & (n-1) # 비트연산 : 2의 n제곱수와 2의 (n-1)제곱수는 AND 연산하면 0임
    if diff_bits == 0:
        return True
    else:
        return False