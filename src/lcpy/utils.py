import importlib
import inspect

def gen_params(module_name, target_fn):

    spec = importlib.util.spec_from_file_location(module_name, target_fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    # print(m, dir(m))
    s = m.Solution()
    fn, _ = inspect.getmembers(m.Solution, inspect.isfunction)[0]

    func = getattr(s, fn)
    sig = inspect.signature(func)
    # print(func, sig)
    params = {k: None for k, _ in sig.parameters.items()}
    # print(params)
    return str(params)

def gen_test(num, module_name, params):
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

    params = {params}
    res = None

    assert func(**params) == res
"""
    with open(f'./tests/test_{num}.py', 'w') as f:
        f.write(s)


if __name__ == '__main__':
    

    gen_test(num = 1234,
             module_name="1252_cells_with_odd_values_in_a_matrix")