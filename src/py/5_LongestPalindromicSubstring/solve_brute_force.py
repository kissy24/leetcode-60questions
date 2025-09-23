class Solution:
    def longestPalindrome(self, s: str) -> str:
        """総当たり法による最長回文部分文字列の探索

            基本的な考え方:
            1. 文字列の全ての部分文字列を生成する
            2. それぞれが回文かどうか判定する
            3. 回文の中で最も長いものを記録する

        Args:
            s (str): 探索対象の文字列

        Returns:
            str: 最長回文部分文字列

        Notes:
            - 時間計算量: O(n^3)
        """
        max_len = 0
        output = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j+1]
                if sub_str == sub_str[::-1] and len(sub_str) > max_len:
                    max_len = len(sub_str)
                    output = sub_str
        return output