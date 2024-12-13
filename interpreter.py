# Wörterbuch für Operatorfunktionen
OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

def eval_expr(expr, environment):
    if len(expr) == 1 and expr[0][0] == 'NUMBER':
        return expr[0][1]
    elif len(expr) == 1 and expr[0][0] == 'IDENT':
        var_name = expr[0][1]
        if var_name in environment:
            return environment[var_name]
        else:
            raise NameError(f'Undefinierte Variable: {var_name}')
    elif len(expr) == 3:
        left = eval_expr([expr[0]], environment)
        op = expr[1][1]
        right = eval_expr([expr[2]], environment)
        if op in OPERATORS:
            return OPERATORS[op](left, right)
        else:
            raise SyntaxError(f'Unbekannter Operator: {op}')
    else:
        raise SyntaxError('Ungültiger Ausdruck')

# Interpreter: Führt die Anweisungen aus
def evaluate(ast):
    environment = {}
    for node in ast:
        if node[0] == 'assign':
            var_name = node[1]
            expr = node[2]
            value = eval_expr(expr, environment)
            environment[var_name] = value
        elif node[0] == 'print':
            expr = node[1]
            value = eval_expr(expr, environment)
            print(value)
