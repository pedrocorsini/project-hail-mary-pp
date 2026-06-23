import ply.yacc as yacc
from src.lexico import tokens

def p_programa(p):
    '''Programa : ListaInstrucoes'''
    p[0] = ('Programa', p[1])

def p_lista_instrucoes(p):
    '''ListaInstrucoes : Instrucao ListaInstrucoes
                       | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + (p[2] if p[2] else [])
    else:
        p[0] = []

def p_instrucao(p):
    '''Instrucao : DecVariavel
                 | Atribuicao
                 | Condicional
                 | Enquanto
                 | For
                 | Cin
                 | Cout
                 | Include
                 | Define
                 | Switch
                 | DecFuncao
                 | CallFuncao'''
    p[0] = p[1]

# Regras básicas e atribuições
def p_dec_variavel(p):
    '''DecVariavel : TipoVariavel T_ID T_END'''
    p[0] = ('DecVariavel', p[1], p[2])

def p_tipo_variavel(p):
    '''TipoVariavel : T_ELECTRON
                    | T_ATOM
                    | T_NEUTRON
                    | T_DARK_MATTER'''
    p[0] = p[1]

def p_atribuicao(p):
    '''Atribuicao : T_ID T_ORBIT_ASSIGN Expressao T_END'''
    p[0] = ('Atribuicao', p[1], p[3])

# Expressões aritmpéticas e lógicas
def p_expressao(p):
    '''Expressao : Expressao T_FUSION Termo
                 | Expressao T_DECAY Termo
                 | Termo'''
    if len(p) == 4:
        p[0] = ('OpBinaria', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_termo(p):
    '''Termo : Termo T_COLLISION Fator
             | Termo T_SPLIT Fator
             | Fator'''
    if len(p) == 4:
        p[0] = ('OpBinaria', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_fator(p):
    '''Fator : T_NUM
             | T_ID'''
    p[0] = p[1]

# Controle de Fluxo (if, while, for)
def p_condicional(p):
    '''Condicional : T_SUN T_ORBIT_OPEN ExpressaoRelacional T_ORBIT_CLOSE T_SYSTEM_OPEN ListaInstrucoes T_SYSTEM_CLOSE ParteElse'''
    p[0] = ('Condicional', p[3], p[6], p[8])

def p_parte_else(p):
    '''ParteElse : T_MOON T_SYSTEM_OPEN ListaInstrucoes T_SYSTEM_CLOSE
                 | empty'''
    if len(p) > 2:
        p[0] = p[3]
    else:
        p[0] = None

def p_enquanto(p):
    '''Enquanto : T_ORBIT T_ORBIT_OPEN ExpressaoRelacional T_ORBIT_CLOSE T_SYSTEM_OPEN ListaInstrucoes T_SYSTEM_CLOSE'''
    p[0] = ('Enquanto', p[3], p[6])

def p_for(p):
    '''For : T_ROCKET T_ORBIT_OPEN AtribuicaoSemFim T_END ExpressaoRelacional T_END AtribuicaoSemFim T_ORBIT_CLOSE T_SYSTEM_OPEN ListaInstrucoes T_SYSTEM_CLOSE'''
    p[0] = ('For', p[3], p[5], p[7], p[10])

def p_atribuicao_sem_fim(p):
    '''AtribuicaoSemFim : T_ID T_ORBIT_ASSIGN Expressao'''
    p[0] = ('AtribuicaoFor', p[1], p[3])

# Operações Relacionais
def p_expressao_relacional(p):
    '''ExpressaoRelacional : Expressao OperadorRelacional Expressao'''
    p[0] = ('Relacional', p[2], p[1], p[3])

def p_operador_relacional(p):
    '''OperadorRelacional : T_LT
                          | T_GT
                          | T_LEQ
                          | T_GEQ
                          | T_EQ
                          | T_NEQ'''
    p[0] = p[1]

# Entrada, Saída e Include
def p_cin(p):
    '''Cin : T_SIGNAL T_WARP_OUT T_ID T_END'''
    p[0] = ('Cin', p[3])

def p_cout(p):
    '''Cout : T_BROADCAST T_WARP_IN T_ID T_END
            | T_BROADCAST T_WARP_IN T_NUM T_END'''
    p[0] = ('Cout', p[3])

def p_include(p):
    '''Include : T_WARP T_ID T_END'''
    p[0] = ('Include', p[2])

# define
def p_define(p):
    '''Define : T_GRAVITY T_ID T_NUM T_END'''
    p[0] = ('Define', p[2], p[3])

# Switch-Case
def p_switch(p):
    '''Switch : T_STAR T_ORBIT_OPEN T_ID T_ORBIT_CLOSE T_SYSTEM_OPEN ListaCasos T_SYSTEM_CLOSE'''
    p[0] = ('Switch', p[3], p[6])

def p_lista_casos(p):
    '''ListaCasos : Caso ListaCasos
                  | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + (p[2] if p[2] else [])
    else:
        p[0] = []

def p_caso(p):
    '''Caso : T_PLANET T_NUM T_MARK ListaInstrucoes T_ESCAPE T_END'''
    p[0] = ('Caso', p[2], p[4])

# Função e return
def p_dec_funcao(p):
    '''DecFuncao : TipoVariavel T_ID T_ORBIT_OPEN ParamsDec T_ORBIT_CLOSE T_SYSTEM_OPEN ListaInstrucoes RetornoOpc T_SYSTEM_CLOSE'''
    p[0] = ('DecFuncao', p[1], p[2], p[4], p[7], p[8])

def p_retorno_opc(p):
    '''RetornoOpc : T_LAUNCH Expressao T_END
                  | empty'''
    if len(p) == 4:
        p[0] = ('Return', p[2])
    else:
        p[0] = None

# Parâmetros para declaração de funções (com tipo)
def p_params_dec(p):
    '''ParamsDec : ListaParamsDec
                 | empty'''
    p[0] = p[1] if p[1] else []

def p_lista_params_dec(p):
    '''ListaParamsDec : TipoVariavel T_ID MaisParamsDec'''
    p[0] = [(p[1], p[2])] + (p[3] if p[3] else [])

def p_mais_params_dec(p):
    '''MaisParamsDec : T_COMMA ListaParamsDec
                     | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []

# Chamada de funções
def p_call_funcao(p):
    '''CallFuncao : T_ID T_ORBIT_OPEN ParamsChama T_ORBIT_CLOSE T_END'''
    p[0] = ('CallFuncao', p[1], p[3])

# Parâmetros para chamada de funções (sem tipo)
def p_params_chama(p):
    '''ParamsChama : ListaParamsChama
                   | empty'''
    p[0] = p[1] if p[1] else []

def p_lista_params_chama(p):
    '''ListaParamsChama : Expressao MaisParamsChama'''
    p[0] = [p[1]] + (p[2] if p[2] else [])

def p_mais_params_chama(p):
    '''MaisParamsChama : T_COMMA ListaParamsChama
                       | empty'''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = []

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"Erro sintático no token '{p.value}', linha {p.lineno}")
    else:
        print("Erro sintático: Fim de arquivo inesperado")

parser = yacc.yacc()