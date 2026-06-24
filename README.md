# PHM++ — Project Hail Mary++

Analisador léxico e sintático da linguagem **PHM++**, desenvolvido para a disciplina **ECOM06A - Compiladores (UNIFEI)**.


## Sobre a linguagem

PHM++ é uma linguagem didática inspirada em astronomia, com sintaxe baseada em C/C++.

Características principais:

- Tipagem estática (tipo declarado antes do identificador)
- Case-sensitive
- Instruções encerradas por `;`
- Blocos delimitados por `{` e `}`
- Comentários de linha iniciados por `¢`

## Estrutura do projeto

```text
project-hail-mary-pp
├── codes/          # Códigos de Exemplo
├── src/            # Analisadores Léxicos e Sintáticos
├── resources/      # PDF da Linguagem PMH++
├── main.py         # Programa principal
├── README.md       # Informações do projeto
└── .gitignore          
```
## Requisitos

- Python 3.8+
- PLY (Python Lex-Yacc)

Instalação:

```bash
pip install ply
```

## Como executar

No diretório raiz do projeto:

```bash
python main.py codes\exemplo1.phm
```

O programa:

1. Gera o arquivo `<entrada>_tokens.txt` no mesmo diretório do `.phm`.
2. Executa a análise sintática e imprime a árvore (ou os erros encontrados).

## Exemplos de código (`codes/`)

### `exemplo1.phm` — Entrada e saída básica

```phm
warp universo;
electron a;
signal << a;
broadcast >> a;
```

### `exemplo2.phm` — Condicional `sun`/`moon` (if/else)

```phm
electron a;
electron b;
a = 10;
b = 20;
sun ( a > b ) {
    broadcast << a;
} moon {
    broadcast << b;
}
```

### `exemplo3.phm` — Laços `rocket` e `orbit` (for/while)

```phm
electron i;
electron total;
total = 0;

rocket ( i = 0 ; i < 10 ; i = i + 1 ) {
    total = total + i;
}

orbit ( total > 0 ) {
    total = total - 1;
}
```

## Tokens da linguagem 

### Tipos de dados

| PHM++         | Equivalente |
|---------------|-------------|
| `electron`    | `int`       |
| `atom`        | `float`     |
| `neutron`     | `char`      |
| `dark_matter` | `void`      |

### Palavras reservadas

| PHM++       | Equivalente |
|-------------|-------------|
| `sun`       | `if`        |
| `moon`      | `else`      |
| `rocket`    | `for`       |
| `orbit`     | `while`     |
| `star`      | `switch`    |
| `planet`    | `case`      |
| `escape`    | `break`     |
| `launch`    | `return`    |
| `signal`    | `cin`       |
| `broadcast` | `cout`      |
| `gravity`   | `define`    |
| `warp`      | `include`   |

### Operadores e símbolos

| Símbolo | Token | Descrição |
|---------|-------|-----------|
| `=`     | `T_ORBIT_ASSIGN` | Atribuição |
| `<`     | `T_LT` | Menor que |
| `>`     | `T_GT` | Maior que |
| `<=`    | `T_LEQ` | Menor ou igual |
| `>=`    | `T_GEQ` | Maior ou igual |
| `==`    | `T_EQ` | Igualdade |
| `!=`    | `T_NEQ` | Diferença |
| `&&`    | `T_AND` | AND lógico |
| `\|\|`  | `T_OR` | OR lógico |
| `~`     | `T_NOT` | NOT lógico |
| `+`     | `T_FUSION` | Soma |
| `-`     | `T_DECAY` | Subtração |
| `*`     | `T_COLLISION` | Multiplicação |
| `/`     | `T_SPLIT` | Divisão |
| `%`     | `T_MOD` | Resto |
| `^`     | `T_POW` | Potência |
| `(`     | `T_ORBIT_OPEN` | Abre parêntesis |
| `)`     | `T_ORBIT_CLOSE` | Fecha parêntesis |
| `{`     | `T_SYSTEM_OPEN` | Abre chaves |
| `}`     | `T_SYSTEM_CLOSE` | Fecha chaves |
| `;`     | `T_END` | Finalizador de instrução |
| `,`     | `T_COMMA` | Vírgula |
| `:`     | `T_MARK` | Dois-pontos |
| `>>`    | `T_WARP_OUT` | Saída (fluxo) |
| `<<`    | `T_WARP_IN` | Entrada (fluxo) |
| `#`     | `T_SIGNAL_MARK` | Marca de sinal |

## Gramática implementada

A análise sintática em `src/sintatico.py` implementa as seguintes regras e estruturas:

- Declaração de variáveis
- Atribuição de valores
- Expressões matemáticas e lógicas
- Condicional if/else (`sun` / `moon`)
- Laço de repetição while (`orbit`)
- Laço de repetição for (`rocket`)
- Estrutura de seleção switch/case (`star` / `planet`)
- Declaração e chamada de funções com passagem de parâmetros
- Retorno de funções (`launch`)
- Entrada de dados (`signal >>`)
- Saída de dados (`broadcast <<`)
- Diretiva de inclusão (`warp ...;`)
- Definição de constantes (`gravity`)

## Autores

> Pedro Henrique Corsini Soares Rodrigues - 2024004107  
> Pedro Henrique Moreira de Mello Balbino – 2024003988
