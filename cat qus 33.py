def climbStairs(n):
    # Base cases
    if n == 0 or n == 1:
        return 1

    # dp[i] will store the number of ways to reach step i
    dp = [0] * (n + 1)
    dp[0] = 1  # There's one way to stay at the ground
    dp[1] = 1  # There's one way to reach the first step

    # Fill the dp array
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Example usage:
n = 5
print(f"Number of ways to climb {n} steps: {climbStairs(n)}")
