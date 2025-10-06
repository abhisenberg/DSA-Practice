package main

import "fmt"

//https://leetcode.com/problems/rotting-oranges/

func orangesRotting(grid [][]int) int {
	var queue Queue
	m := len(grid)
	n := len(grid[0])
	freshOranges := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 2 {
				queue.enqueue([]int{i, j})
			} else if grid[i][j] == 1 {
				freshOranges++
			}
		}
	}

	if freshOranges == 0 {
		return 0
	}

	minute := 0
	for !queue.isEmpty() && freshOranges != 0 {
		fmt.Println(queue)
		level_size := len(queue)

		for level_size != 0 {

			indc := queue.dequeue().([]int)
			i, j := indc[0], indc[1]

			if i-1 >= 0 && grid[i-1][j] == 1 {
				grid[i-1][j] = 2
				queue.enqueue([]int{i - 1, j})
				freshOranges--
			}
			if j-1 >= 0 && grid[i][j-1] == 1 {
				grid[i][j-1] = 2
				queue.enqueue([]int{i, j - 1})
				freshOranges--
			}
			if i+1 < m && grid[i+1][j] == 1 {
				grid[i+1][j] = 2
				queue.enqueue([]int{i + 1, j})
				freshOranges--
			}
			if j+1 < n && grid[i][j+1] == 1 {
				grid[i][j+1] = 2
				queue.enqueue([]int{i, j + 1})
				freshOranges--
			}

			level_size--
		}
		minute++
	}

	if freshOranges != 0 {
		return -1
	}

	return minute
}
