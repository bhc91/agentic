# Parser: Erstellt eine Struktur aus Tokens
def parse(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        token, value = tokens[i]
        if token == 'IDENT' and i+1 < len(tokens) and tokens[i+1][0] == 'ASSIGN':
            # Zuweisung
            var_name = value
            i += 2  # Überspringe IDENT und ASSIGN
            expr = []
            while i < len(tokens) and tokens[i][0] != 'NEWLINE':
                expr.append(tokens[i])
                i += 1
            ast.append(('assign', var_name, expr))
        elif token == 'IDENT' and value == 'print':
            # Ausgabe
            i += 1  # Überspringe 'print'
            expr = []
            while i < len(tokens) and tokens[i][0] != 'NEWLINE':
                expr.append(tokens[i])
                i += 1
            ast.append(('print', expr))
        else:
            i += 1
    return ast
