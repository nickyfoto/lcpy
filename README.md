# lcpy

[LeetCode CLI](https://github.com/leetcode-tools/leetcode-cli) helper for python.

## Features

- Generate testing files for test locally using pytest.
- Provide common algorithm and data structure modules for easy prototyping.

## Modules

### Algorithms

- Divide and Conquer: fastSelect, fastMultiply, mergeSort, quickSort, binary search
- Dynamic Programming: Knapsack
- Graph: BFS, DFS, Dijkstra, connected components, Topological Sort, [floyd_warshall](https://github.com/nickyfoto/lcpy/blob/cca942de112c5d122385f835af79935475587c8e/src/lcpy/graph.py#L20)
- Random
	- [shuffle](https://github.com/nickyfoto/lcpy/blob/bdc1de5964a5fcb96701fd158cd746e5a39f5108/src/lcpy/sort.py#L26)
- Backtracking
	- [value based permutation](https://github.com/nickyfoto/lcpy/blob/c845cc91e6f6783cb7b733a4ec77cd9f979fbe24/src/lcpy/bt.py#L6)
	- [subset](https://github.com/nickyfoto/lcpy/blob/bd1417168891034cc5320f8332d2b0d9972ed0b9/src/lcpy/bt.py#L32)

### Data structures

#### TreeNode

- `build_root`: return TreeNode instance from given list.

##### instance method

- `__str__`: print tree in bfs (ignore None node).
- `pre`: return pre order of DFS traversal
- `post`: return post order of DFS traversal

#### ListNode (Linked List):

- `build_head`: return ListNode instance from given list.
- `__str__`: print linked list.
- `value_eq`: value based equality check.

#### PriorityQueue

- max heap pq

#### Graph

#### DiGraph

#### Trie

#### UnionFind

#### OrderedCounter

## Installation

```
git clone https://github.com/nickyfoto/lcpy.git
pip3 install ./lcpy
```

Install in editable mode

```
pip3 install -e ./lcpy
```

## Usage

generate module and test template

```sh
lcpy cp <some_file.py>
```

---

## TODO

- [ ] Bit Manipulation
- [ ] Concurrency
- [ ] ShellSort
- [ ] Red-Black BST, B-Tree
- [ ] Convex Hull
- [ ] Sparse Vectors
- [ ] Max Flow
- [ ] Redix Sorts
- [ ] Regular Expression
- [ ] name 'List' is not defined
- [ ] cannot generate testing without adding `pass`.
- [ ] add tree visualizer function
- [ ] generate testing file for non `class Solution` problem.