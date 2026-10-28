# =========================================================================
    # Parte 1: Thiago - Configuração Inicial e Validação da Quantidade de Jogos
    # =========================================================================

    # Exibe o título centralizado do sistemas!

    largura = 80
    print("="*largura)
    print()
    print("CAMPANHA TIME DE VÁRZEA".center(largura))
    print()
    print("="*largura)
    print()

    # Valida a quantidade de jogos (entre 1 e 30)
    # usando laço while

    total_jogos = int(input("Digite a quantidade de jogos da campanha de 1 a 30 jogos: \n"))

    while total_jogos < 1 or total_jogos > 30:
        print(f"Quantidade de jogos invalido! \n")
        total_jogos = int(input("Digite a quantidade de jogos da campanha de 1 a 30 jogos:\n"))

    # Declaração das variáveis iniciais
    # inicializa contadores, acumuladores e a
    # lista vazia para registrar os dados dos jogos.

    pontos = 0
    vitorias = 0
    empates = 0
    derrotas = 0
    goleadas = 0
    gols_pro = 0
    gols_contra = 0
    maior_gols = 0
    registros = [] # Lista vazia para guardar os registros