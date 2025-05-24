class Solution:
    def longestPalindrome(self, s: str) -> str:
        """最長回文部分文字列を探索する

            基本的な考え方:
            1. 中心から左右に拡張して回文をチェックする
            2. 各文字を中心として、または2文字の間を中心として回文をチェックする
            3. 最長の回文部分文字列を記録する

        Args:
            s (str): 探索対象の文字列
        Returns:
            str: 最長回文部分文字列

        Notes:
            - 時間計算量: O(n^2)
            - 空間計算量: O(1)
        """
        start, max_len = 0, 1

        def expand_around_center(left: int, right: int) -> int:
            """指定された中心から拡張して回文の長さを返す"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            # 奇数長の回文をチェック (中心が1文字)
            len1 = expand_around_center(i, i)
            # 偶数長の回文をチェック (中心が2文字の間)
            len2 = expand_around_center(i, i + 1)

            current_max = max(len1, len2)
            if current_max > max_len:
                max_len = current_max
                # 開始位置を計算
                start = i - (current_max - 1) // 2

        return s[start : start + max_len]
