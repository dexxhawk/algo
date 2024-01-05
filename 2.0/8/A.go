package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Tree struct {
	root *Node
	flag bool
}

type Node struct {
	key int
	left, right *Node
}


func (t *Tree) add(node *Node, n int) *Node {
	if node == nil {
		return &Node{n, nil, nil};
	}
	if node.key == n {
		t.flag = true
		return node

	} else if n < node.key {
		node.left = t.add(node.left, n)
	} else {
		node.right = t.add(node.right, n)
	}
	return node
}

func (t *Tree) search(node *Node, n int) {
	if node == nil {
		return
	} 
	if node.key == n {
		t.flag = true
		return
	} else if n < node.key {
		t.search(node.left, n)
	} else {
		t.search(node.right, n)
	}
	return
}

func (t *Tree) Add(n int) string {
	t.flag = false
	t.root = t.add(t.root, n)
	if t.flag {
		return "ALREADY"
	}
	return "DONE"
}

func (t *Tree) Search(n int) string {
	t.flag = false
	t.search(t.root, n)
	if t.flag {
		return "YES"
	}
	return "NO"
}

func (t *Tree) print(node *Node, res string, lvl int) string {
	if node.left != nil {
		res = t.print(node.left, res, lvl + 1)
		res += "\n"
	}
	res += strings.Repeat(".", lvl)
	res += strconv.Itoa(node.key)

	if node.right != nil {
		res += "\n"
		res = t.print(node.right, res, lvl + 1)
	}
	return res
}


func (t *Tree) Print() string {
	res := ""
	return t.print(t.root, res, 0)
}



func main() {
	cin := bufio.NewScanner(os.Stdin)
	cout := bufio.NewWriter(os.Stdout)

	tree := Tree{root: nil, flag: false}

	for cin.Scan() {
		if cin.Text() == "" {
			break
		}

		str := strings.Split(cin.Text(), " ")

		if str[0] == "PRINTTREE" {
			fmt.Println(tree.Print())
			continue
		}
		n, _ := strconv.Atoi(str[1])
		if str[0] == "ADD" {
			fmt.Println(tree.Add(n))
		} else if str[0] == "SEARCH"{
			fmt.Println(tree.Search(n))
		}
		
	}

	cout.Flush()

}

