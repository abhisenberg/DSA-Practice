package main

/*
Things to revise:

- Why do we fill the result array backwards? Why not backwards?
- How to initialize an empty array of size n in go?
-
*/

func sortedSquares(nums []int) []int {
	n := len(nums)
	l, r := 0, n-1
	res := make([]int, n)

	for i := n - 1; i >= 0; i-- {
		sq := 0
		if absInt(nums[l]) > absInt(nums[r]) {
			sq = nums[l]
			l++
		} else {
			sq = nums[r]
			r--
		}
		res[i] = sq * sq
	}

	return res
}

func absInt(x int) int {
	if x < 0 {
		return -x
	} else {
		return x
	}
}
