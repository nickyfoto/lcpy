import numpy as np

from lcpy.dc import easyMultiply
from lcpy.dc import fastMultiply
from lcpy.dc import fastSelect


def test_multiply():
    x = 1234
    y = 5678
    assert x*y == easyMultiply(x, y)
    assert x*y == fastMultiply(x, y)


def test_fastSelect():
    a = list(np.random.randint(100, size=100))
    for k in range(1, len(a)+1):
        assert fastSelect(a, k) == sorted(a)[k-1]
