import re

# Define regular expressions for SoccerScript tokens
TOKEN_SPECIFICATION = [
    ('COMMENT', r'#[^\n]*'), # Comments starting with # and continuing to the end of the line
    ('KEYWORD', r'\b(kickoff|play|shout|receive|referee|offside|assist|training|match|goal|win|lose)\b'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Variable names
    ('NUMBER', r'\d+(\.\d+)?'),  # Integer or float
    ('STRING', r'"[^"]*"'),  # Strings enclosed in double quotes
    ('SYMBOL', r'[+\-*/=():<>]'),  # Operators and delimiters
    ('LOGICAL', r'(==|>=|<=|>|<|!=)'),  # Logical operators
    ('NEWLINE', r'\n'),  # Line endings
    ('SKIP', r'[ \t]+'),  # Skip spaces and tabs
    ('MISMATCH', r'.'),  # Any other character
]

# Compile the regular expressions into a pattern
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

def scan_soccer_script(code):
    """
    Scanner for SoccerScript code.
    """
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NEWLINE':
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'COMMENT': 
            tokens.append((kind, value)) 
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        else:
            tokens.append((kind, value))
    return tokens

# Example SoccerScript code
soccer_code = """
kickoff:
    player = receive("Enter player: ")
    # iam a comment
    goals = receive("Enter goals: ")
    referee goals >= 3:
        shout("Hat-trick!")
    assist goals == 2:
        shout("Brace!")
    offside:
        shout("Keep Training")
"""

# Scan the code and print tokens
tokens = scan_soccer_script(soccer_code)
for token in tokens:
    print(token)