

def gen_test(num, module_name):
    """
    generate test file
    """
    s = \
f"""
import inspect
from importlib import import_module
module_name = "{module_name}"

def test_{num}():

    m = import_module(module_name)  

    s = m.Solution()

    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]

    func = getattr(s, fn)

    n = 2
    m = 3
    indices = [[0,1],[1,1]]


    assert func(n, m, indices) == 6
"""
    with open(f'./tests/test_{num}.py', 'w') as f:
        f.write(s)


if __name__ == '__main__':
    

    gen_test(num = 1234,
             module_name="1252_cells_with_odd_values_in_a_matrix")