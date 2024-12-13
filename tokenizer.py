import re

# Tokenizer: Zerlegt den Code in Tokens
def tokenize(code):
    keywords = {'print'}
    token_specification = [
        ('NUMBER',   r'\d+'),          # Integer
        ('IDENT',    r'[a-zA-Z_][a-zA-Z_0-9]*'),  # Identifikatoren
        ('ASSIGN',   r'='),            # Zuweisung
        ('OP',       r'[+\-*/]'),     # Operatoren
        ('NEWLINE',  r'\n'),          # Zeilenumbrüche
        ('SKIP',     r'[ \t]+'),      # Leerzeichen und Tabs
        ('MISMATCH', r'.'),            # Alles andere
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = convert_to_number(value)
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unerwartetes Zeichen: {value}')
        tokens.append((kind, value))
    return tokens

# Hilfsfunktion zur Umwandlung in Integer
def convert_to_number(value):
    return int(value)
