import re

with open("program.ss") as f:
    code = f.read()

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

for match in re.finditer(token_regex, code):

    token_type = match.lastgroup
    value = match.group()
    position = match.start()

    if token_type != "SKIP":
        print(f'{token_type}: {value!r} at pos {position}')

# ================================
# code 1
# ================================
# kickoff:
#     @play = "hello" 
#     num = 123 
#     # This is a comment

# ================================
# code 2
# ================================
# kickoff:
#     player = receive("Enter player: ")
#     # iam a comment
#     goals = receive("Enter goals: ")
#     referee goals >= 3:
#         shout("Hat-trick!")
#     assist goals == 2:
#         shout("Brace!")
#     offside:
#         shout("Keep Training")

