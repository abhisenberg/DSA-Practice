package main

import "fmt"

func main() {
	de := []string{"0201", "0101", "0102", "1212", "2002"}
	ans := openLock(de, "0202")
	fmt.Println(ans)

	// fmt.Println(nextCodes("0000"))

}
