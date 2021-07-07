from lcpy.math import quickMod
from math import pow

def test_quickMod():
    x = 1234
    y = 5
    mod = 11
    assert quickMod(x, y, mod) == divmod(int(pow(x, y)), mod)[1]