import ply.lex as lex

# Palavras reservadas
reserved = {
    'electron': 'T_ELECTRON', # int
    'atom': 'T_ATOM', # float
    'neutron': 'T_NEUTRON', # char
    'dark_matter': 'T_DARK_MATTER', # void
    'sun': 'T_SUN', # if
    'moon': 'T_MOON', # else
    'rocket': 'T_ROCKET', # for
    'orbit': 'T_ORBIT', # orbit
    'star': 'T_STAR', # switch
    'planet': 'T_PLANET', # case
    'escape': 'T_ESCAPE', # break
    'launch': 'T_LAUNCH', # return
    'signal': 'T_SIGNAL', # cin
    'broadcast': 'T_BROADCAST', # cout
    'gravity': 'T_GRAVITY', # define
    'warp': 'T_WARP' # include
}

# Lista de Tokens
tokens = [
    'T_NUM', 'T_ID', 'T_ORBIT_ASSIGN', 'T_LEQ', 'T_GEQ', 'T_LT', 'T_GT',
    'T_NEQ', 'T_EQ', 'T_AND', 'T_OR', 'T_NOT', 'T_FUSION', 'T_DECAY',
    'T_COLLISION', 'T_SPLIT', 'T_MOD', 'T_POW', 'T_COMMA', 'T_MARK',
    'T_END', 'T_ORBIT_OPEN', 'T_ORBIT_CLOSE', 'T_SYSTEM_OPEN', 'T_SYSTEM_CLOSE',
    'T_SIGNAL_MARK', 'T_WARP_OUT', 'T_WARP_IN', 'T_COMMENT'
] + list(reserved.values())

# Expressões Regulares para tokens simples
t_T_ORBIT_ASSIGN = r'='
t_T_LEQ = r'<='
t_T_GEQ = r'>='
t_T_LT = r'<'
t_T_GT = r'>'
t_T_NEQ = r'!='
t_T_EQ = r'=='
t_T_AND = r'&&'
t_T_OR = r'\|\|'
t_T_NOT = r'~'
t_T_FUSION = r'\+'
t_T_DECAY = r'-'
t_T_COLLISION = r'\*'
t_T_SPLIT = r'/'
t_T_MOD = r'%'
t_T_POW = r'\^'
t_T_COMMA = r','
t_T_MARK = r':'
t_T_END = r';'
t_T_ORBIT_OPEN = r'\('
t_T_ORBIT_CLOSE = r'\)'
t_T_SYSTEM_OPEN = r'\{'
t_T_SYSTEM_CLOSE = r'\}'
t_T_SIGNAL_MARK = r'\#'
t_T_WARP_OUT = r'>>'
t_T_WARP_IN = r'<<'

# Ignorar espaços e tabs
t_ignore = ' \t'

# Expressões regulares complexas
def t_T_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_T_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'T_ID') # Verifica palavras reservadas
    return t

def t_T_COMMENT(t):
    r'¢.*'
    pass # Comentários são descartados pelo analisador léxico

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere Ilegal '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Constrói o lexer
lexer = lex.lex()

# Dicionário de tradução para a saída de tokens solicitada no enunciado
token_translation = {
    'T_ID': 'identificador',
    'T_NUM': 'numero',
    'T_ORBIT_ASSIGN': 'atribuicao',
    'T_EQ': 'operador relacional',
    'T_LT': 'operador relacional',
    'T_GT': 'operador relacional',
    'T_LEQ': 'operador relacional',
    'T_GEQ': 'operador relacional',
    'T_NEQ': 'operador relacional',
    'T_FUSION': 'operador aritmetico soma',
    'T_DECAY': 'operador aritmetico subtracao',
    'T_COLLISION': 'operador aritmetico multiplicacao',
    'T_SPLIT': 'operador aritmetico divisao',
    'T_SYSTEM_OPEN': 'abre chaves',
    'T_SYSTEM_CLOSE': 'fecha chaves',
    'T_ORBIT_OPEN': 'abre parenteses',
    'T_ORBIT_CLOSE': 'fecha parenteses',
    'T_SUN': 'comando condicional (if)',
    'T_MOON': 'comando condicional (else)',
    'T_ROCKET': 'comando de repeticao (for)',
    'T_ORBIT': 'comando de repeticao (while)',
    'T_SIGNAL': 'comando de entrada',
    'T_BROADCAST': 'comando de saida',
    'T_WARP': 'diretiva de inclusao',
    'T_WARP_IN': 'operador de saida',
    'T_WARP_OUT': 'operador de entrada',
    'T_END': 'finalizador de comando',
    'T_ELECTRON': 'tipo inteiro',
    'T_ATOM': 'tipo float'
}