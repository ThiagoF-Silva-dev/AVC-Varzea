def main ():

    # ===========================================================================
    # Parte 1: Thiago - Configuração Inicial e Validação da Quantidade de Jogos
    # ===========================================================================

    # Configuração inicial do sistema do Time de Várzea. Exibe o título centralizado,
    # valida a quantidade de jogos (entre 1 e 30) com um laço while e inicializa as
    # variáveis, contadores e a lista para salvar os dados dos jogos.

    largura = 80
    print("="*largura)
    print()
    print("GERENCIADOR DE CAMPANHA - FUTEBOL DE VÁRZEA".center(largura))
    print()
    print("="*largura)
    print()

    total_jogos = int(input("Digite a quantidade de jogos da campanha de 1 a 30 jogos: \t"))

    while total_jogos < 1 or total_jogos > 30:
        print(f"Quantidade de jogos invalidos! \n")
        total_jogos = int(input("Digite a quantidade de jogos da campanha de 1 a 30 jogos: \t"))

    pontos_totais = 0
    pontos_geral = 0
    vitorias = 0
    empates = 0
    derrotas = 0
    goleadas = 0
    gols_pro_total = 0
    gols_contra_total = 0
    maior_gols = 0
    registros = []

    # ===================================================================
    # Parte 2: Douglas - laço de Repetição dos jogos e Validação de Gols
    # ===================================================================

    # Controla o fluxo de cadastro dos jogos, solicitando e validando os
    # gols marcados e sofridos (evitando valores negativos), calculando o
    # total da partida e atualizando os acumuladores gerais da campanha.

    for i in range(1, total_jogos + 1):
        print(f"\n||| PARTIDA {i} de {total_jogos} |||")

        g_time = int(input(f"Gols Marcados na Partida {i}: "))
        while g_time < 0:
            print("Valor inválido! Os gols marcados não podem ser negativos")
            g_time = int(input(f"Gols Marcados na Partida {i}: "))

        g_adversario = int(input(f"Gols Marcados na Partida {i}: "))
        while g_adversario < 0:
            print("Valor  inválido! Os gols marcados não podem ser negativos")
            g_adversario = int(input(f"Gols Marcados na Partida {i}: "))

        g_partida = g_time + g_adversario
        print(f"Total de gols marcados na partida: ", g_partida)

        gols_pro_total += g_time
        gols_contra_total += g_adversario
        pontos_geral = total_jogos * 3

    # =============================================================================
    # Parte 3: Igor - Lógica de Pontuação, Goleadas e Acumuladores (Dentro do laço)
    # =============================================================================

    # Processa o desfecho da partida atualizando o recorde de gols, determinando o
    # resultado (vitória, empate ou derrota), somando os pontos à campanha geral e
    # identificando se ocorreu goleada (diferença de 3 ou mais gols).

        if i == 1 or g_time > maior_gols:
            maior_gols - g_time

        if g_time > g_adversario:
            pontos_partida = 3
            vitorias += 1
            resultado = ("Vitória")
        elif g_time < g_adversario:
            pontos_partida = 0
            derrotas += 1
            resultado = ("Derrota")
        else:
            pontos_partida = 1
            empates += 1
            resultado = ("Empate")

        pontos_totais += pontos_partida

        if g_time > g_adversario and (g_time - g_adversario) >= 3:
            goleada = "Ocorreu uma GOLEADA"
            goleadas += 1
        else:
            goleada = "Não"
        print("Goleada na partida:", goleada)

        # ===============================================================================
        # Thiago - Guarda os dados da partida num dicionário e adicionà a lista
        # ===============================================================================

        jogo_info = {"numero": i,
                     "g_time": g_time,
                     "g_adversario": g_adversario,
                     "resultado": resultado,
                     "goleada": goleada
        }
        registros.append(jogo_info)

    # ===============================================================================
    # Parte 4: Bruno - Relatório Final, Cálculos de Aproveitamento e Situação do time
    # ===============================================================================

    # Apresenta o relatório completo de desempenho da equipe no campeonato.
    # Ele exibe as estatísticas gerais (saldo, média de gols e aproveitamento),
    # a situação final do time e o histórico de todas as partidas registradas.

    print("\n" + "=" * largura)
    print("RESUMO DA CAMPANHA".center(largura))
    print("=" * largura)

    saldo_gols =  gols_pro_total - gols_contra_total
    media_gols = gols_pro_total / total_jogos
    aproveitamento = (pontos_totais / (total_jogos * 3)) * 100

    if aproveitamento >= 70:
        situacao = "Briga pelo Titulo"
    elif aproveitamento >= 50:
        situacao = "Zona de Classificação"
    elif aproveitamento >= 30:
        situacao = "Meio de Tabela"
    else:
        situacao = "Risco de Rebaixamento"

    print("\n Lista de jogos Registrados:")
    for j in registros:
        print(f" - JOGO {j["numero"]}: {j["g_time"]} X {j["g_adversario"]} ({j["resultado"]}) | Goleada: {j["goleada"]}")

    print(f"\n Estatísticas Finais:")
    print(f" - Total de Jogos: {total_jogos}")
    print(f" - Total de pontos disputados: {pontos_geral}")
    print(f" - Pontos Conquistados: {pontos_totais}")
    print(f" - Vitórias: {vitorias} | Empates: {empates} | Derrotas: {derrotas}")
    print(f" - Goleadas: {goleadas}")
    print(f" - Gols Pró: {gols_pro_total} | Gols Contra: {gols_contra_total} | Saldo: {saldo_gols}")
    print(f" - Média de gols marcados por jogo: {media_gols}")
    print(f" - Maior número de gols marcados em um jogo: {maior_gols}")
    print(f" - Aproveitamento: {aproveitamento}%")
    print(f" - Situação: {situacao}")
    print("=" * largura)

if __name__ == "__main__":
    main()