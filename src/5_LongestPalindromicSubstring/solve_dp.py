class Solution:
    def longestPalindrome(self, s: str) -> str:
        """動的計画法による最長回文部分文字列の探索

            基本的な考え方:
            1. dp[i][j]をiからjまでの部分文字列が回文かどうかを示す
            2. dp[i][j]がTrueの場合、s[i]とs[j]が同じであり、dp[i+1][j-1]もTrueである必要がある
            3. dp[i][i]は常にTrue（長さ1の文字列は回文）
            4. dp[i][i+1]はs[i]とs[i+1]が同じ場合にTrue（長さ2の文字列は回文）

        Args:
            s (str): 探索対象の文字列

        Returns:
            str: 最長回文部分文字列

        Notes:
            - 時間計算量: O(n^2)
            - 空間計算量: O(n^2)
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max_len = 0, 1

        # 長さ1は全て回文
        for i in range(n):
            dp[i][i] = True

        # 長さ2をチェック
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, max_len = i, 2

        # 長さ3以上をチェック
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start, max_len = i, length

        return s[start : start + max_len]
