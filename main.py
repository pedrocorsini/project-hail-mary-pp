import sys
from src.lexico import lexer, token_translation
from src.sintatico import parser

def gerar_arquivo_tokens(codigo, nome_arquivo):
    lexer.input(codigo)
    nome_saida = nome_arquivo.replace('.phm', '_tokens.txt')
    
    with open(nome_saida, 'w', encoding='utf-8') as f:
        f.write("ARQUIVO DE RECONHECIMENTO DE TOKENS\n")
        f.write("="*40 + "\n")
        while True:
            tok = lexer.token()
            if not tok:
                break
            descricao = token_translation.get(tok.type, tok.type)
            f.write(f"{tok.value} -> {descricao}\n")
            
    print(f"[OK] Arquivo de tokens gerado: {nome_saida}")

def compilar(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return

    print(f"\n--- Analisando: {nome_arquivo} ---")
    
    gerar_arquivo_tokens(codigo, nome_arquivo)
    
    resultado = parser.parse(codigo, lexer=lexer)
    if resultado:
        print("[OK] Análise Sintática concluída com sucesso! Árvore gerada:")
        print(resultado)
    else:
        print("[FALHA] Erros encontrados durante a análise sintática.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.phm>")
    else:
        compilar(sys.argv[1])