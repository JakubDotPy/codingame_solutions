import sys
import math
from functools import partial
import operator as op


debug = partial(print, file=sys.stderr, flush=True)
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

result_d = {}

num = int(input())
for i in range(num):
    n = input()
    debug(n)
    operation, arg_1, arg_2 = n.split()
    val = None

    if operation == 'VALUE' and arg_1.isalnum():
        val = int(arg_1)

    if arg_1.lstrip('-').isdigit():
        arg_1 = int(arg_1)

    if arg_2.lstrip('-').isdigit():
        arg_2 = int(arg_2)

    result_d[i] = {
        'value'    : val,
        'operation': operation,
        'arg_1'    : arg_1,
        'arg_2'    : arg_2,
    }

oper_d = {
    'ADD' : op.add,
    'SUB' : op.sub,
    'MULT': op.mul,
}


def resolve_cell(cell):
    if cell['value'] is not None:
        return cell['value']

    if cell['operation'] == 'VALUE':
        if not isinstance(cell['arg_1'], int):
            cell['value'] = resolve_cell(result_d[int(cell['arg_1'][1:])])
        else:
            cell['value'] = cell['arg_1']
        return cell['value']

    if not isinstance(cell['arg_1'], int):
        debug(f"{cell['arg_1']=}")
        cell['arg_1'] = resolve_cell(result_d[int(cell['arg_1'][1:])])

    if not isinstance(cell['arg_2'], int):
        debug(f"{cell['arg_2']=}")
        cell['arg_2'] = resolve_cell(result_d[int(cell['arg_2'][1:])])

    cell['value'] = oper_d[cell['operation']](cell['arg_1'], cell['arg_2'])
    return cell['value']


for c in result_d.values():
    resolve_cell(c)


for k, v in sorted(result_d.items()):
    print(v['value'])