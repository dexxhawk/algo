package main

import "fmt"

func main() {
	ans := 0
	mxm := 0
	var x int

	for {
		fmt.Scan(&x)
		if x == 0 {
			break
		}
		if x > mxm {
			mxm = x
			ans = 1
		} else if x == mxm {
			ans++
		}
	}

	fmt.Println(ans)
}