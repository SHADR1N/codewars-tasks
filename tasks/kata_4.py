from typing import List


def longest_slide_down(pyramid: List[list]):
    dp = pyramid.copy()

    for i in range(len(dp) - 2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]

