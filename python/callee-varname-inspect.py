import inspect, ast

#   Getting the scope of the caller is apparently a non-trivial task in python.
#   Presumedly this is proof python 4 is an inevitibility (and it'll f...... have a f...... print statement *and* function like it always f...... should have), there's a lot not to like about python 3, and f...... vimscript can manage 'varname of the caller' -> (but the real question is) can Perl?
#   LINK: https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function

def foo(a, f, b):
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.findsource(frame[0])[0]
    nodes = ast.parse(''.join(string))

    i_expr = -1

    for (i, node) in enumerate(nodes.body):
        if hasattr(node, 'value') and isinstance(node.value, ast.Call) and hasattr(node.value.func, 'id') and node.value.func.id == 'foo':  # Here goes name of the function:
            i_expr = i
            break

    i_expr_next = min(i_expr + 1, len(nodes.body)-1)  
    lineno_start = nodes.body[i_expr].lineno
    lineno_end = nodes.body[i_expr_next].lineno if i_expr_next != i_expr else len(string)

    str_func_call = ''.join([i.strip() for i in string[lineno_start - 1: lineno_end]])
    params = str_func_call[str_func_call.find('(') + 1:-1].split(',')

    print(params)

e = 1 + 7
c = 3
foo(e, 100, b=c)

