# lcpy

[LeetCode CLI](https://github.com/leetcode-tools/leetcode-cli) helper for python.

## Features

- Generate testing files for test locally using pytest.
- Provide common algorithm and data structure modules for easy prototyping.

## Modules

### Algorithms

- Divide and Conquer: fastSelect, fastMultiply, mergeSort, quickSort, binary search
- Dynamic Programming: Knapsack
- Graph: BFS, DFS, Dijkstra, connected components, Topological Sort
- Random: shuffle

### Data structures

#### TreeNode

- `build_root`: return TreeNode instance from given list.
- `__str__`: print tree in bfs (ignore None node).

#### ListNode (Linked List):

- `build_head`: return ListNode instance from given list.
- `__str__`: print linked list.

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

---

## TODO

- [ ] Bit Manipulation
- [ ] name 'List' is not defined
- [ ] cannot generate testing without adding `pass`.
- [ ] add tree visualizer function
- [ ] generate testing file for non `class Solution` problem.