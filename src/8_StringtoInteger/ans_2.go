package main

func myAtoi_2(s string) int {
	const (
		INT_MAX = 2147483647  // 2^31 - 1
		INT_MIN = -2147483648 // -2^31
	)

	i := 0
	n := len(s)

	// ステップ1: 先頭の空白文字をスキップ
	for i < n && s[i] == ' ' {
		i++
	}

	if i == n {
		return 0
	}

	// ステップ2: 符号の判定
	sign := 1
	if s[i] == '-' {
		sign = -1
		i++
	} else if s[i] == '+' {
		i++
	}

	// ステップ3: 数字の読み取りと変換
	result := 0
	for i < n && s[i] >= '0' && s[i] <= '9' {
		digit := int(s[i] - '0')

		// オーバーフローチェック
		if result > (INT_MAX-digit)/10 {
			if sign == 1 {
				return INT_MAX
			}
			return INT_MIN
		}

		result = result*10 + digit
		i++
	}

	return sign * result
}
