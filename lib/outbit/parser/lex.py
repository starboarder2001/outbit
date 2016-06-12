import ply.lex as lex

# LEX tokens
tokens = ("ACTION", "OPTIONVAL", "OPTIONVALS", "OPTIONVALD", "SPACE", "EQUAL")

t_ACTION        =r'[a-zA-Z0-9_\-]+'
t_OPTIONVAL     =r'/[a-zA-Z0-9_/\-]+'
t_OPTIONVALS    =r"'[\"a-zA-Z0-9_/\s\-]+'"
t_OPTIONVALD    =r'"[\'a-zA-Z0-9_/\s\-]+"'
t_SPACE         =r'\s+'
t_EQUAL         =r'='

# Ignored characters
t_ignore = "\n"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()