# lcpy

[LeetCode CLI](https://github.com/leetcode-tools/leetcode-cli) helper for python.

## Features

- Generate testing files for test locally using pytest.
- Modulize common algorithm and data structure for easy prototyping.

## Modules

### Algorithms

- Dynamic Programming: Knapsack
- Graph: dijkstra, connected components, 

### Data structures

#### TreeNode

- `build_root`: return TreeNode instance from given list.
- `__str__`: print tree in bfs (ignore None node).

#### ListNode (Linked List):

- `build_head`: return ListNode instance from given list.
- `__str__`: print linked list.

#### Priority Queue

- max heap pq

#### Graph

#### DiGraph

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

TODO

- [ ] name 'List' is not defined
- [ ] cannot generate testing without adding `pass`.
- [ ] add tree visualizer function
- [ ] generate testing file for non `class Solution` problem.