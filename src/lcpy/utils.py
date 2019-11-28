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
    # print(func.__name__, sig)
    # params = {k: k for k, _ in sig.parameters.items()}
    # print(params)
    return sig

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

    
    

    assert func{params} == Output
"""
    with open(f'./tests/test_{num}.py', 'w') as f:
        f.write(s)


if __name__ == '__main__':
    

    gen_test(num = 1234,
             module_name="1252_cells_with_odd_values_in_a_matrix")