def max_score(arr, n):
    if not arr:
        return 0

    length = len(arr)
    dp = [float('-inf')] * length
    dp[0] = arr[0]

    for i in range(length):
        for j in range(1, n+1):
            if i + j < length:
                a1 = dp[i+j]
                a2 = dp[i]
                a3 = arr[i+j]
                dp[i + j] = max(dp[i + j], dp[i] + arr[i + j])

    return dp[-1]

# Example usage:
arr = [1, -1, -2, 4, -7, 3]
n = 2
print(max_score(arr, n))  # Output: 7
