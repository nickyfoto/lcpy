sort by compare two element a, b

```py
# LC 179
def largestNumber(self, nums: List[int]) -> str:
    if not any(nums):
        return "0"
    
    return "".join(sorted(map(str, nums), key=cmp_to_key(lambda n1, n2: -1 if n1+n2>n2+n1 else 1)))
```