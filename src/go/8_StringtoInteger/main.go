package main

import (
	"math"
	"regexp"
	"strconv"
	"strings"
)

func myAtoi(s string) int {
	// 空文字対処
	s_ := strings.TrimSpace(s)
	if s_ == "" {
		return 0
	}
	// 符号確認
	sign := 1
	if s_[0] == '+' {
		s_ = s_[1:]
	} else if s_[0] == '-' {
		sign = -1
		s_ = s_[1:]
	}
	// 正規表現判定
	ptn := `^(\d+)`
	re, _ := regexp.Compile(ptn)
	s_i := re.FindAllString(s_, 1)
	if len(s_i) == 0 {
		s_i = append(s_i, "0")
	}
	i, _ := strconv.Atoi(s_i[0])
	// 閾値判定
	max := int(math.Pow(2, 31)) - 1
	min := int(math.Pow(2, 31)) * -1
	ans := sign * i
	if ans > max {
		ans = max
	}
	if ans < min {
		ans = min
	}
	return ans
}
