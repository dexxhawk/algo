package main

import (
	"fmt"
)

func main() {
	var a[10] int
	
	for i := 0; i < 10; i++ {
		fmt.Scan(&a[i])
	}
	var d[10] int 

	cur_d := 0
	flag := 1
	
	for i := 0; i < len(a); i++ {
		if a[i] != 2 && flag == 1 {
			continue
		}
		if a[i] == 1 {
			d[i] = cur_d
		} else if a[i] == 2{
			flag = 0
			cur_d = 0
		}
		cur_d++
	}

	cur_d = 0
	flag = 1
	for i := len(a) - 1; i > -1; i-- {
		if a[i] != 2 && flag == 1 {
			continue
		}
		if a[i] == 1 && cur_d != 0 && (d[i]	> cur_d || d[i] == 0) {
			d[i] = cur_d
		} else if a[i] == 2 {
			flag = 0
			cur_d = 0
		}
		cur_d++
	}

	ans := 0
	for i := 0; i < len(d); i++ {
		ans = max(ans, d[i])
	}
	fmt.Println(ans)
}