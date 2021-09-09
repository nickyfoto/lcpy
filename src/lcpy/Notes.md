sort by compare two element a, b

```py
# LC 179
def largestNumber(self, nums: List[int]) -> str:
    if not any(nums):
        return "0"
    
    return "".join(sorted(map(str, nums), key=cmp_to_key(lambda n1, n2: -1 if n1+n2>n2+n1 else 1)))
```

subset enumeration

```py
def enum_subset(n):
    """
    n = 3
    1 1
    2 2
    3 3, 2, 1
    4 4
    5 5, 4, 1
    6 6, 4, 2
    7 7, 6, 5, 4, 3, 2, 1
    """
    for state in range(1, 1 << n):
        subset = state
        while subset > 0:
            print(state, subset)
            subset = (subset - 1) & state
```